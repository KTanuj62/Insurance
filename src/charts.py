"""
Charts Module
=============
Functions to create Plotly visualizations for the insurance dashboard.
"""

import plotly.express as px
import plotly.graph_objects as go


# Color palette for light theme with slate accents
COLORS = {
    'primary': '#1e293b',      # Dark slate
    'secondary': '#475569',    # Medium slate
    'success': '#059669',      # Green
    'warning': '#d97706',      # Orange
    'danger': '#dc2626',       # Red
    'info': '#0891b2',         # Cyan
    'background': '#f8fafc',   # Light background
    'card': '#ffffff',         # White cards
    'text': '#1e293b',         # Dark text
}

CHART_COLORS = ['#1e293b', '#475569', '#0891b2', '#059669', '#d97706', '#dc2626', '#7c3aed', '#db2777']


def get_chart_layout():
    """Get common layout settings for all charts."""
    return dict(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color=COLORS['text']),
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(
            bgcolor='rgba(0,0,0,0)',
            font=dict(color=COLORS['text'])
        )
    )


def create_claims_by_insurer(df):
    """Create bar chart showing claims count by insurer."""
    data = df.groupby('insurer_name').size().reset_index(name='count')
    data = data.sort_values('count', ascending=True)
    
    fig = px.bar(
        data,
        x='count',
        y='insurer_name',
        orientation='h',
        color='insurer_name',
        color_discrete_sequence=CHART_COLORS,
        title='Claims by Insurer'
    )
    
    fig.update_layout(**get_chart_layout())
    fig.update_layout(showlegend=False, height=300)
    fig.update_xaxes(gridcolor='rgba(255,255,255,0.1)')
    fig.update_yaxes(gridcolor='rgba(255,255,255,0.1)')
    
    return fig


def create_claims_by_incident_type(df):
    """Create pie chart showing distribution of incident types."""
    data = df.groupby('natureOfincident').size().reset_index(name='count')
    
    fig = px.pie(
        data,
        values='count',
        names='natureOfincident',
        title='Incident Type Distribution',
        color_discrete_sequence=CHART_COLORS,
        hole=0.4
    )
    
    fig.update_layout(**get_chart_layout())
    fig.update_layout(height=300)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    
    return fig


def create_monthly_claims_trend(df):
    """Create line chart showing claims trend over time."""
    df_copy = df.copy()
    df_copy['month'] = df_copy['dateOfloss'].dt.to_period('M').astype(str)
    data = df_copy.groupby('month').size().reset_index(name='count')
    data = data.sort_values('month')
    
    fig = px.line(
        data,
        x='month',
        y='count',
        title='Monthly Claims Trend',
        markers=True
    )
    
    fig.update_traces(line_color=COLORS['primary'], line_width=3)
    fig.update_layout(**get_chart_layout())
    fig.update_layout(height=300)
    fig.update_xaxes(gridcolor='rgba(255,255,255,0.1)', tickangle=45)
    fig.update_yaxes(gridcolor='rgba(255,255,255,0.1)')
    
    return fig


def create_claims_by_state(df):
    """Create bar chart showing top 10 states by claim count."""
    data = df.groupby('insuredstate').size().reset_index(name='count')
    data = data.sort_values('count', ascending=False).head(10)
    
    fig = px.bar(
        data,
        x='insuredstate',
        y='count',
        color='count',
        color_continuous_scale='Blues',
        title='Top 10 States by Claims'
    )
    
    fig.update_layout(**get_chart_layout())
    fig.update_layout(height=300, coloraxis_showscale=False)
    fig.update_xaxes(gridcolor='rgba(255,255,255,0.1)')
    fig.update_yaxes(gridcolor='rgba(255,255,255,0.1)')
    
    return fig


def create_payment_analysis(df):
    """Create bar chart comparing claimed vs paid amounts by insurer."""
    data = df.groupby('insurer_name').agg({
        'total_claimed_losses': 'sum',
        'total_insurance_payment': 'sum'
    }).reset_index()
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Claimed',
        x=data['insurer_name'],
        y=data['total_claimed_losses'],
        marker_color=COLORS['warning']
    ))
    
    fig.add_trace(go.Bar(
        name='Paid',
        x=data['insurer_name'],
        y=data['total_insurance_payment'],
        marker_color=COLORS['success']
    ))
    
    fig.update_layout(**get_chart_layout())
    fig.update_layout(
        title='Claims vs Payments by Insurer',
        barmode='group',
        height=300
    )
    fig.update_xaxes(gridcolor='rgba(255,255,255,0.1)')
    fig.update_yaxes(gridcolor='rgba(255,255,255,0.1)')
    
    return fig


def create_injury_analysis(df):
    """Create pie chart showing injury involvement."""
    data = df.groupby('injuryinvolved').size().reset_index(name='count')
    
    fig = px.pie(
        data,
        values='count',
        names='injuryinvolved',
        title='Injury Involvement',
        color_discrete_sequence=[COLORS['success'], COLORS['danger']],
        hole=0.4
    )
    
    fig.update_layout(**get_chart_layout())
    fig.update_layout(height=300)
    
    return fig
