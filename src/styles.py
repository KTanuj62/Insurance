"""
Styles Module
=============
Custom CSS for the light theme with deep slate accents.
"""


def get_custom_css():
    """Return custom CSS for the light theme with slate accents."""
    return """
    <style>
        /* Import Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        /* Main app background - Light theme */
        .stApp {
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            font-family: 'Inter', sans-serif;
        }
        
        /* Header styling */
        .main-header {
            background: linear-gradient(90deg, #1e293b 0%, #334155 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            padding: 1rem 0;
            margin-bottom: 1rem;
        }
        
        /* KPI Card styling - Light cards with slate accents */
        .kpi-card {
            background: linear-gradient(145deg, #ffffff 0%, #f1f5f9 100%);
            border-radius: 16px;
            padding: 1.5rem;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 20px rgba(30, 41, 59, 0.08);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .kpi-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(30, 41, 59, 0.15);
        }
        
        .kpi-value {
            font-size: 2rem;
            font-weight: 700;
            background: linear-gradient(90deg, #1e293b 0%, #475569 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
        }
        
        .kpi-label {
            color: #64748b;
            font-size: 0.9rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        /* Chart container */
        .chart-container {
            background: linear-gradient(145deg, #ffffff 0%, #f1f5f9 100%);
            border-radius: 16px;
            padding: 1rem;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 20px rgba(30, 41, 59, 0.08);
            margin-bottom: 1rem;
        }
        
        /* Sidebar styling - Slate sidebar */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
            border-right: 1px solid #334155;
        }
        
        section[data-testid="stSidebar"] .stMarkdown h1,
        section[data-testid="stSidebar"] .stMarkdown h2,
        section[data-testid="stSidebar"] .stMarkdown h3 {
            color: #e2e8f0;
        }
        
        section[data-testid="stSidebar"] .stMarkdown p,
        section[data-testid="stSidebar"] label {
            color: #cbd5e1 !important;
        }
        
        /* Metric styling */
        [data-testid="stMetric"] {
            background: linear-gradient(145deg, #ffffff 0%, #f1f5f9 100%);
            border-radius: 12px;
            padding: 1rem;
            border: 1px solid #e2e8f0;
        }
        
        [data-testid="stMetricValue"] {
            color: #1e293b;
            font-weight: 700;
        }
        
        [data-testid="stMetricLabel"] {
            color: #64748b;
        }
        
        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f5f9;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #94a3b8;
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #64748b;
        }
        
        /* Button styling */
        .stButton > button {
            background: linear-gradient(90deg, #1e293b 0%, #334155 100%);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            box-shadow: 0 4px 15px rgba(30, 41, 59, 0.3);
            transform: translateY(-2px);
        }
        
        /* Main content text color */
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #1e293b !important;
        }
        
        .stMarkdown p {
            color: #475569;
        }
        
        /* Divider */
        hr {
            border-color: #e2e8f0;
        }
    </style>
    """


def create_kpi_card(value, label):
    """Create HTML for a styled KPI card."""
    return f"""
    <div class="kpi-card">
        <div class="kpi-value">{value}</div>
        <div class="kpi-label">{label}</div>
    </div>
    """
