"""
=============================================================================
UNIT TESTS FOR INSURANCE DASHBOARD
=============================================================================

OVERVIEW
--------
This module contains unit tests for the Insurance Dashboard application.
Tests verify that individual components work correctly in isolation.

WHAT ARE UNIT TESTS?
--------------------
Unit tests are automated tests that verify small, isolated pieces of code.
Each test focuses on a single function or behavior.

Benefits of unit testing:
    - Catch bugs early in development
    - Provide documentation through examples
    - Enable safe refactoring
    - Required for CI/CD pipelines

HOW TO RUN TESTS
----------------
From the project root directory:

    pytest tests/ -v              # Run all tests with verbose output
    pytest tests/ -v --tb=short   # Run with shorter traceback
    pytest tests/test_dashboard.py::test_format_currency  # Run single test

TEST NAMING CONVENTION
----------------------
    test_<function_name>_<scenario>
    
Example: test_format_currency_with_thousands

=============================================================================
"""

import sys
from pathlib import Path

# Add source directory to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
import pandas as pd
from datetime import date


# =============================================================================
# KPI CALCULATION TESTS
# =============================================================================

class TestCurrencyFormatting:
    """Tests for currency formatting functions."""
    
    def test_format_currency_hundreds(self):
        """Values under 1000 should display with dollar sign."""
        from kpis import format_currency
        assert format_currency(500) == "$500"
        assert format_currency(999) == "$999"
    
    def test_format_currency_thousands(self):
        """Values in thousands should display with K suffix."""
        from kpis import format_currency
        assert format_currency(1000) == "$1.0K"
        assert format_currency(1500) == "$1.5K"
        assert format_currency(999999) == "$1000.0K"
    
    def test_format_currency_millions(self):
        """Values in millions should display with M suffix."""
        from kpis import format_currency
        assert format_currency(1000000) == "$1.0M"
        assert format_currency(1500000) == "$1.5M"
        assert format_currency(999999999) == "$1000.0M"
    
    def test_format_currency_billions(self):
        """Values in billions should display with B suffix."""
        from kpis import format_currency
        assert format_currency(1000000000) == "$1.0B"
        assert format_currency(2500000000) == "$2.5B"


class TestNumberFormatting:
    """Tests for number formatting functions."""
    
    def test_format_number_adds_commas(self):
        """Numbers should be formatted with thousand separators."""
        from kpis import format_number
        assert format_number(1000) == "1,000"
        assert format_number(1000000) == "1,000,000"
        assert format_number(123456789) == "123,456,789"


class TestClaimCalculations:
    """Tests for claim-related KPI calculations."""
    
    def test_calculate_total_claims_with_data(self):
        """Should return count of rows in dataframe."""
        from kpis import calculate_total_claims
        df = pd.DataFrame({'id': [1, 2, 3, 4, 5]})
        assert calculate_total_claims(df) == 5
    
    def test_calculate_total_claims_empty_dataframe(self):
        """Should return 0 for empty dataframe."""
        from kpis import calculate_total_claims
        df = pd.DataFrame()
        assert calculate_total_claims(df) == 0
    
    def test_calculate_injury_rate(self):
        """Should calculate percentage of claims with injuries."""
        from kpis import calculate_injury_rate
        df = pd.DataFrame({
            'injuryinvolved': ['Yes', 'Yes', 'No', 'No']
        })
        # 2 out of 4 = 50%
        assert calculate_injury_rate(df) == 50.0
    
    def test_calculate_injury_rate_all_injuries(self):
        """Should return 100% when all claims have injuries."""
        from kpis import calculate_injury_rate
        df = pd.DataFrame({
            'injuryinvolved': ['Yes', 'Yes', 'Yes']
        })
        assert calculate_injury_rate(df) == 100.0
    
    def test_calculate_injury_rate_no_injuries(self):
        """Should return 0% when no claims have injuries."""
        from kpis import calculate_injury_rate
        df = pd.DataFrame({
            'injuryinvolved': ['No', 'No', 'No']
        })
        assert calculate_injury_rate(df) == 0.0
    
    def test_calculate_injury_rate_empty_dataframe(self):
        """Should return 0 for empty dataframe to avoid division by zero."""
        from kpis import calculate_injury_rate
        df = pd.DataFrame({'injuryinvolved': []})
        assert calculate_injury_rate(df) == 0
    
    def test_calculate_lawsuit_rate(self):
        """Should calculate percentage of claims with lawsuits."""
        from kpis import calculate_lawsuit_rate
        df = pd.DataFrame({
            'lawsuit_filed': ['Yes', 'No', 'No', 'No']
        })
        # 1 out of 4 = 25%
        assert calculate_lawsuit_rate(df) == 25.0


# =============================================================================
# DATA LOADER TESTS
# =============================================================================

class TestDataLoader:
    """Tests for data loading functionality."""
    
    def test_load_data_function_exists(self):
        """Verify load_data function can be imported."""
        from data_loader import load_data
        assert callable(load_data)
    
    def test_get_column_options_function_exists(self):
        """Verify get_column_options function can be imported."""
        from data_loader import get_column_options
        assert callable(get_column_options)


# =============================================================================
# STYLES TESTS
# =============================================================================

class TestStyles:
    """Tests for styling functions."""
    
    def test_get_custom_css_returns_valid_html(self):
        """CSS output should contain proper style tags."""
        from styles import get_custom_css
        css = get_custom_css()
        
        assert isinstance(css, str)
        assert "<style>" in css
        assert "</style>" in css
    
    def test_get_custom_css_contains_required_classes(self):
        """CSS should define required CSS classes."""
        from styles import get_custom_css
        css = get_custom_css()
        
        assert "kpi-card" in css
        assert "kpi-value" in css
        assert "main-header" in css
    
    def test_create_kpi_card_returns_html(self):
        """KPI card function should return valid HTML."""
        from styles import create_kpi_card
        html = create_kpi_card("$1.5M", "Total Revenue")
        
        assert "kpi-card" in html
        assert "$1.5M" in html
        assert "Total Revenue" in html


# =============================================================================
# CHARTS TESTS
# =============================================================================

class TestCharts:
    """Tests for chart configuration and functions."""
    
    def test_color_palette_defined(self):
        """Color palette should be properly defined."""
        from charts import COLORS, CHART_COLORS
        
        assert isinstance(COLORS, dict)
        assert 'primary' in COLORS
        assert 'secondary' in COLORS
        assert 'background' in COLORS
        assert 'text' in COLORS
        
        assert isinstance(CHART_COLORS, list)
        assert len(CHART_COLORS) >= 6
    
    def test_chart_layout_configuration(self):
        """Chart layout function should return proper configuration."""
        from charts import get_chart_layout
        layout = get_chart_layout()
        
        assert isinstance(layout, dict)
        assert 'paper_bgcolor' in layout
        assert 'plot_bgcolor' in layout
        assert 'font' in layout


# =============================================================================
# FILTERS TESTS
# =============================================================================

class TestFilters:
    """Tests for filter functionality."""
    
    def test_apply_filters_returns_dataframe(self):
        """Filter function should return a pandas DataFrame."""
        from filters import apply_filters
        
        df = pd.DataFrame({
            'dateOfloss': pd.to_datetime(['2023-01-15', '2023-06-20']),
            'insurer_name': ['Geico', 'StateFarm'],
            'insuredstate': ['CA', 'TX'],
            'natureOfincident': ['Collision', 'Hit and run'],
            'injuryinvolved': ['Yes', 'No']
        })
        
        result = apply_filters(
            df,
            date_range=(date(2023, 1, 1), date(2023, 12, 31)),
            insurers=['Geico', 'StateFarm'],
            states=['CA', 'TX'],
            incidents=['Collision', 'Hit and run'],
            injury="All"
        )
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 2
    
    def test_apply_filters_with_insurer_filter(self):
        """Should filter by insurer correctly."""
        from filters import apply_filters
        
        df = pd.DataFrame({
            'dateOfloss': pd.to_datetime(['2023-01-15', '2023-06-20']),
            'insurer_name': ['Geico', 'StateFarm'],
            'insuredstate': ['CA', 'TX'],
            'natureOfincident': ['Collision', 'Hit and run'],
            'injuryinvolved': ['Yes', 'No']
        })
        
        result = apply_filters(
            df,
            date_range=(date(2023, 1, 1), date(2023, 12, 31)),
            insurers=['Geico'],  # Only Geico
            states=['CA', 'TX'],
            incidents=['Collision', 'Hit and run'],
            injury="All"
        )
        
        assert len(result) == 1
        assert result.iloc[0]['insurer_name'] == 'Geico'
    
    def test_apply_filters_with_injury_filter(self):
        """Should filter by injury status correctly."""
        from filters import apply_filters
        
        df = pd.DataFrame({
            'dateOfloss': pd.to_datetime(['2023-01-15', '2023-06-20']),
            'insurer_name': ['Geico', 'StateFarm'],
            'insuredstate': ['CA', 'TX'],
            'natureOfincident': ['Collision', 'Hit and run'],
            'injuryinvolved': ['Yes', 'No']
        })
        
        result = apply_filters(
            df,
            date_range=(date(2023, 1, 1), date(2023, 12, 31)),
            insurers=['Geico', 'StateFarm'],
            states=['CA', 'TX'],
            incidents=['Collision', 'Hit and run'],
            injury="Yes"  # Only with injuries
        )
        
        assert len(result) == 1
        assert result.iloc[0]['injuryinvolved'] == 'Yes'


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
