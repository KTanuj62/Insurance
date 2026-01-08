"""
Data Loader Module
==================
This module handles loading and caching the insurance data.
"""

import pandas as pd
import streamlit as st
from pathlib import Path


@st.cache_data
def load_data():
    """
    Load the insurance CSV data with caching.
    
    Streamlit's @cache_data decorator means this function only runs once,
    then the result is cached for subsequent calls - much faster!
    """
    # Get the path relative to this file's location
    data_path = Path(__file__).parent.parent / "data" / "auto_insurance_data.csv"
    
    df = pd.read_csv(data_path)
    
    # Convert date column to datetime
    df['dateOfloss'] = pd.to_datetime(df['dateOfloss'], errors='coerce')
    
    return df


def get_column_options(df, column):
    """Get unique values from a column for filter dropdowns."""
    return sorted(df[column].dropna().unique().tolist())
