"""
Styles Module - Professional Dark Theme
"""


def get_custom_css():
    """Return custom CSS for professional dark theme."""
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        /* Dark theme background */
        .stApp {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            font-family: 'Inter', sans-serif;
        }
        
        /* Header */
        .main-header {
            background: linear-gradient(90deg, #00d4ff 0%, #7b2cbf 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            padding: 1.5rem 0;
        }
        
        /* KPI Cards */
        .kpi-card {
            background: linear-gradient(145deg, #1e2a4a 0%, #2d3a5a 100%);
            border-radius: 16px;
            padding: 1.5rem;
            border: 1px solid rgba(0, 212, 255, 0.2);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            text-align: center;
            transition: transform 0.3s ease;
        }
        
        .kpi-card:hover {
            transform: translateY(-5px);
            border-color: rgba(0, 212, 255, 0.5);
        }
        
        .kpi-value {
            font-size: 2rem;
            font-weight: 700;
            background: linear-gradient(90deg, #00d4ff 0%, #00ff88 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .kpi-label {
            color: #a0aec0;
            font-size: 0.85rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-top: 0.5rem;
        }
        
        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f3460 0%, #1a1a2e 100%);
        }
        
        section[data-testid="stSidebar"] * {
            color: #e2e8f0 !important;
        }
        
        /* Main content text */
        .stMarkdown, .stMarkdown p, .stMarkdown span {
            color: #e2e8f0 !important;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff !important;
        }
        
        /* Hide Streamlit branding */
        #MainMenu, footer, header {visibility: hidden;}
        
        /* Buttons */
        .stButton > button {
            background: linear-gradient(90deg, #00d4ff 0%, #7b2cbf 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: 600;
        }
        
        /* Select boxes and inputs */
        .stSelectbox > div > div,
        .stMultiSelect > div > div {
            background-color: #1e2a4a !important;
            color: #e2e8f0 !important;
        }
        
        /* Metrics */
        [data-testid="stMetricValue"] {
            color: #00d4ff !important;
        }
        
        [data-testid="stMetricLabel"] {
            color: #a0aec0 !important;
        }
    </style>
    """


def create_kpi_card(value, label):
    """Create styled KPI card HTML."""
    return f"""
    <div class="kpi-card">
        <div class="kpi-value">{value}</div>
        <div class="kpi-label">{label}</div>
    </div>
    """
