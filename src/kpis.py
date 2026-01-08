"""
KPI Calculation Module
======================
Functions to calculate key performance indicators from insurance data.
"""


def calculate_total_claims(df):
    """Calculate total number of claims."""
    return len(df)


def calculate_total_claimed_losses(df):
    """Calculate sum of all claimed losses."""
    return df['total_claimed_losses'].sum()


def calculate_total_payments(df):
    """Calculate sum of all insurance payments."""
    return df['total_insurance_payment'].sum()


def calculate_average_claim(df):
    """Calculate average claim amount."""
    if len(df) == 0:
        return 0
    return df['total_claimed_losses'].mean()


def calculate_injury_rate(df):
    """Calculate percentage of claims involving injuries."""
    if len(df) == 0:
        return 0
    injury_count = df[df['injuryinvolved'] == 'Yes'].shape[0]
    return (injury_count / len(df)) * 100


def calculate_lawsuit_rate(df):
    """Calculate percentage of claims with lawsuits filed."""
    if len(df) == 0:
        return 0
    lawsuit_count = df[df['lawsuit_filed'] == 'Yes'].shape[0]
    return (lawsuit_count / len(df)) * 100


def calculate_payment_ratio(df):
    """Calculate ratio of payments to claims (loss ratio)."""
    total_claimed = df['total_claimed_losses'].sum()
    if total_claimed == 0:
        return 0
    total_paid = df['total_insurance_payment'].sum()
    return (total_paid / total_claimed) * 100


def format_currency(value):
    """Format number as currency with K/M/B suffixes."""
    if value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.1f}B"
    elif value >= 1_000_000:
        return f"${value / 1_000_000:.1f}M"
    elif value >= 1_000:
        return f"${value / 1_000:.1f}K"
    else:
        return f"${value:.0f}"


def format_number(value):
    """Format number with commas."""
    return f"{value:,.0f}"
