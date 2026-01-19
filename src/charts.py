"""
Charts Module - Plotly Visualizations with Dark Theme
"""

import plotly.express as px
import plotly.graph_objects as go

# Color palette for dark theme
COLORS = {
    'primary': '#00d4ff',
    'secondary': '#7b2cbf',
    'success': '#00ff88',
    'warning': '#ffd93d',
    'danger': '#ff6b6b',
    'info': '#4dabf7',
    'background': '#1a1a2e',
    'card': '#1e2a4a',
    'text': '#e2e8f0',
}

CHART_COLORS = ['#00d4ff', '#7b2cbf', '#00ff88', '#ffd93d', '#ff6b6b', '#4dabf7', '#f472b6', '#a78bfa']


def get_chart_layout():
    """Common layout for all charts."""
    return dict(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color=COLORS['text'], family='Inter'),
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(color=COLORS['text']))
    )


def create_claims_by_insurer(df):
    """Bar chart: Claims by insurer."""
    data = df.groupby('insurer_name').size().reset_index(name='count')
    data = data.sort_values('count', ascending=True)
    
    fig = px.bar(data, x='count', y='insurer_name', orientation='h',
                 color='insurer_name', color_discrete_sequence=CHART_COLORS,
                 title='Claims by Insurer')
    
    fig.update_layout(**get_chart_layout(), showlegend=False, height=300)
    fig.update_xaxes(gridcolor='rgba(255,255,255,0.1)', title='')
    fig.update_yaxes(gridcolor='rgba(255,255,255,0.1)', title='')
    return fig


def create_claims_by_incident_type(df):
    """Pie chart: Incident type distribution."""
    data = df.groupby('natureOfincident').size().reset_index(name='count')
    
    fig = px.pie(data, values='count', names='natureOfincident',
                 title='Incident Type Distribution',
                 color_discrete_sequence=CHART_COLORS, hole=0.4)
    
    fig.update_layout(**get_chart_layout(), height=300)
    fig.update_traces(textposition='inside', textinfo='percent+label',
                      textfont=dict(color='white'))
    return fig


def create_monthly_claims_trend(df):
    """Line chart: Monthly claims trend."""
    df_copy = df.copy()
    df_copy['month'] = df_copy['dateOfloss'].dt.to_period('M').astype(str)
    data = df_copy.groupby('month').size().reset_index(name='count')
    data = data.sort_values('month')
    
    fig = px.line(data, x='month', y='count', title='Monthly Claims Trend', markers=True)
    
    fig.update_traces(line_color=COLORS['primary'], line_width=3,
                      marker=dict(size=8, color=COLORS['primary']))
    fig.update_layout(**get_chart_layout(), height=300)
    fig.update_xaxes(gridcolor='rgba(255,255,255,0.1)', tickangle=45, title='')
    fig.update_yaxes(gridcolor='rgba(255,255,255,0.1)', title='')
    return fig


def create_claims_by_state(df):
    """Bar chart: Top 10 states by claims."""
    data = df.groupby('insuredstate').size().reset_index(name='count')
    data = data.sort_values('count', ascending=False).head(10)
    
    fig = px.bar(data, x='insuredstate', y='count',
                 color='count', color_continuous_scale='Teal',
                 title='Top 10 States by Claims')
    
    fig.update_layout(**get_chart_layout(), height=300, coloraxis_showscale=False)
    fig.update_xaxes(gridcolor='rgba(255,255,255,0.1)', title='')
    fig.update_yaxes(gridcolor='rgba(255,255,255,0.1)', title='')
    return fig


def create_payment_analysis(df):
    """Bar chart: Claims vs payments by insurer."""
    data = df.groupby('insurer_name').agg({
        'total_claimed_losses': 'sum',
        'total_insurance_payment': 'sum'
    }).reset_index()
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Claimed', x=data['insurer_name'],
                         y=data['total_claimed_losses'], marker_color=COLORS['warning']))
    fig.add_trace(go.Bar(name='Paid', x=data['insurer_name'],
                         y=data['total_insurance_payment'], marker_color=COLORS['success']))
    
    fig.update_layout(**get_chart_layout(), title='Claims vs Payments by Insurer',
                      barmode='group', height=300)
    fig.update_xaxes(gridcolor='rgba(255,255,255,0.1)')
    fig.update_yaxes(gridcolor='rgba(255,255,255,0.1)')
    return fig


def create_injury_analysis(df):
    """Pie chart: Injury involvement."""
    data = df.groupby('injuryinvolved').size().reset_index(name='count')
    
    fig = px.pie(data, values='count', names='injuryinvolved',
                 title='Injury Involvement',
                 color_discrete_sequence=[COLORS['success'], COLORS['danger']], hole=0.4)
    
    fig.update_layout(**get_chart_layout(), height=300)
    fig.update_traces(textfont=dict(color='white'))
    return fig
