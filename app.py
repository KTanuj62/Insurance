"""
Insurance Claims Analytics Dashboard
=====================================
Main Streamlit application that orchestrates all modules.

This app provides visualization and analysis of auto insurance claims data.
"""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

import streamlit as st

# Import our modules
from data_loader import load_data
from kpis import (
    calculate_total_claims,
    calculate_total_claimed_losses,
    calculate_total_payments,
    calculate_average_claim,
    calculate_injury_rate,
    calculate_lawsuit_rate,
    calculate_payment_ratio,
    format_currency,
    format_number
)
from charts import (
    create_claims_by_insurer,
    create_claims_by_incident_type,
    create_monthly_claims_trend,
    create_claims_by_state,
    create_payment_analysis,
    create_injury_analysis
)
from filters import (
    create_date_filter,
    create_insurer_filter,
    create_state_filter,
    create_incident_filter,
    create_injury_filter,
    apply_filters
)
from styles import get_custom_css, create_kpi_card


# Page configuration
st.set_page_config(
    page_title="Insurance Claims Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)


def main():
    """Main application function."""
    
    # Load data
    df = load_data()
    
    # Sidebar
    st.sidebar.markdown("# 🛡️ Insurance Dashboard")
    st.sidebar.markdown("---")
    
    # Create filters
    date_range = create_date_filter(df)
    insurers = create_insurer_filter(df)
    states = create_state_filter(df)
    incidents = create_incident_filter(df)
    injury = create_injury_filter(df)
    
    # Apply filters
    filtered_df = apply_filters(df, date_range, insurers, states, incidents, injury)
    
    # Show filter status
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Showing:** {len(filtered_df):,} of {len(df):,} claims")
    
    # Main content
    st.markdown('<h1 class="main-header">Insurance Claims Analytics</h1>', unsafe_allow_html=True)
    
    # KPI Row
    st.markdown("### 📊 Key Metrics")
    
    kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5, kpi_col6 = st.columns(6)
    
    with kpi_col1:
        st.markdown(
            create_kpi_card(format_number(calculate_total_claims(filtered_df)), "Total Claims"),
            unsafe_allow_html=True
        )
    
    with kpi_col2:
        st.markdown(
            create_kpi_card(format_currency(calculate_total_claimed_losses(filtered_df)), "Total Claimed"),
            unsafe_allow_html=True
        )
    
    with kpi_col3:
        st.markdown(
            create_kpi_card(format_currency(calculate_total_payments(filtered_df)), "Total Paid"),
            unsafe_allow_html=True
        )
    
    with kpi_col4:
        st.markdown(
            create_kpi_card(format_currency(calculate_average_claim(filtered_df)), "Avg. Claim"),
            unsafe_allow_html=True
        )
    
    with kpi_col5:
        st.markdown(
            create_kpi_card(f"{calculate_injury_rate(filtered_df):.1f}%", "Injury Rate"),
            unsafe_allow_html=True
        )
    
    with kpi_col6:
        st.markdown(
            create_kpi_card(f"{calculate_payment_ratio(filtered_df):.1f}%", "Payment Ratio"),
            unsafe_allow_html=True
        )
    
    st.markdown("---")
    
    # Charts Row 1
    st.markdown("### 📈 Claims Analysis")
    
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.plotly_chart(create_claims_by_insurer(filtered_df), use_container_width=True)
    
    with chart_col2:
        st.plotly_chart(create_claims_by_incident_type(filtered_df), use_container_width=True)
    
    # Charts Row 2
    chart_col3, chart_col4 = st.columns(2)
    
    with chart_col3:
        st.plotly_chart(create_monthly_claims_trend(filtered_df), use_container_width=True)
    
    with chart_col4:
        st.plotly_chart(create_claims_by_state(filtered_df), use_container_width=True)
    
    # Charts Row 3
    st.markdown("### 💰 Payment Analysis")
    
    chart_col5, chart_col6 = st.columns(2)
    
    with chart_col5:
        st.plotly_chart(create_payment_analysis(filtered_df), use_container_width=True)
    
    with chart_col6:
        st.plotly_chart(create_injury_analysis(filtered_df), use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; color: #64748b; padding: 1rem;">
            <p>Insurance Claims Analytics Dashboard | Built with Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
