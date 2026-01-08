"""
Filters Module
==============
Functions to create sidebar filters for the dashboard.
"""

import streamlit as st
import pandas as pd


def create_date_filter(df):
    """Create a date range filter in the sidebar."""
    st.sidebar.subheader("📅 Date Range")
    
    min_date = df['dateOfloss'].min()
    max_date = df['dateOfloss'].max()
    
    # Handle NaT values
    if pd.isna(min_date):
        min_date = pd.Timestamp('2020-01-01')
    if pd.isna(max_date):
        max_date = pd.Timestamp('2025-12-31')
    
    date_range = st.sidebar.date_input(
        "Select date range",
        value=(min_date.date(), max_date.date()),
        min_value=min_date.date(),
        max_value=max_date.date(),
        key="date_filter"
    )
    
    return date_range


def create_insurer_filter(df):
    """Create a multi-select filter for insurers."""
    st.sidebar.subheader("🏢 Insurer")
    
    insurers = sorted(df['insurer_name'].unique().tolist())
    
    selected = st.sidebar.multiselect(
        "Select insurers",
        options=insurers,
        default=insurers,
        key="insurer_filter"
    )
    
    return selected


def create_state_filter(df):
    """Create a multi-select filter for states."""
    st.sidebar.subheader("📍 State")
    
    states = sorted(df['insuredstate'].unique().tolist())
    
    selected = st.sidebar.multiselect(
        "Select states",
        options=states,
        default=states,
        key="state_filter"
    )
    
    return selected


def create_incident_filter(df):
    """Create a multi-select filter for incident types."""
    st.sidebar.subheader("⚠️ Incident Type")
    
    incidents = sorted(df['natureOfincident'].unique().tolist())
    
    selected = st.sidebar.multiselect(
        "Select incident types",
        options=incidents,
        default=incidents,
        key="incident_filter"
    )
    
    return selected


def create_injury_filter(df):
    """Create a radio button filter for injury involvement."""
    st.sidebar.subheader("🏥 Injury Involved")
    
    selected = st.sidebar.radio(
        "Filter by injury",
        options=["All", "Yes", "No"],
        key="injury_filter"
    )
    
    return selected


def apply_filters(df, date_range, insurers, states, incidents, injury):
    """Apply all filters to the dataframe."""
    filtered_df = df.copy()
    
    # Apply date filter
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = filtered_df[
            (filtered_df['dateOfloss'].dt.date >= start_date) &
            (filtered_df['dateOfloss'].dt.date <= end_date)
        ]
    
    # Apply insurer filter
    if insurers:
        filtered_df = filtered_df[filtered_df['insurer_name'].isin(insurers)]
    
    # Apply state filter
    if states:
        filtered_df = filtered_df[filtered_df['insuredstate'].isin(states)]
    
    # Apply incident filter
    if incidents:
        filtered_df = filtered_df[filtered_df['natureOfincident'].isin(incidents)]
    
    # Apply injury filter
    if injury != "All":
        filtered_df = filtered_df[filtered_df['injuryinvolved'] == injury]
    
    return filtered_df
