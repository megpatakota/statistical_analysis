"""
Configuration file for Hotels.com Customer Churn Analysis
Contains unified colour scheme and global settings
"""

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# =============================================================================
# UNIFIED COLOUR SCHEME FOR ALL VISUALISATIONS
# =============================================================================

COLORS = {
    # Churn status colours
    'retained': '#1a5f7a',      # Deep teal blue - Retained customers
    'churned': '#e63946',       # Coral red - Churned customers
    
    # Categorical palette (for platforms, channels, etc.)
    'cat_1': '#1a5f7a',         # Deep teal
    'cat_2': '#2d8f9e',         # Medium teal
    'cat_3': '#57b8c9',         # Light teal
    'cat_4': '#a8dadc',         # Pale teal
    'cat_5': '#f1faee',         # Off-white
    
    # Risk levels
    'low_risk': '#1a5f7a',      # Deep teal - Low risk
    'medium_risk': '#f4a261',   # Orange - Medium risk
    'high_risk': '#e76f51',     # Dark coral - High risk
    'critical_risk': '#e63946', # Red - Critical risk
    
    # Feature importance / positive-negative
    'positive': '#e63946',      # Red - increases churn
    'negative': '#1a5f7a',      # Teal - decreases churn
    'neutral': '#457b9d',       # Blue-grey - neutral
    
    # Model comparison
    'model_1': '#1a5f7a',       # Logistic Regression
    'model_2': '#2a9d8f',       # Random Forest
    'model_3': '#e9c46a',       # Gradient Boosting
    
    # Background and accents
    'background': '#f8f9fa',    # Light grey background
    'grid': '#dee2e6',          # Grid lines
    'text': '#212529',          # Dark text
    'accent': '#457b9d',        # Accent blue
}

# Create colour lists for easy use
CHURN_COLORS = [COLORS['retained'], COLORS['churned']]
RISK_COLORS = [COLORS['low_risk'], COLORS['medium_risk'], COLORS['high_risk'], COLORS['critical_risk']]
MODEL_COLORS = [COLORS['model_1'], COLORS['model_2'], COLORS['model_3']]
CAT_PALETTE = [COLORS['cat_1'], COLORS['cat_2'], COLORS['cat_3'], COLORS['cat_4'], COLORS['cat_5']]

# Custom colormaps
def get_custom_cmap():
    """Returns custom colormap for correlation heatmaps (teal to white to red)"""
    return LinearSegmentedColormap.from_list('custom', 
        [COLORS['retained'], '#ffffff', COLORS['churned']])

def get_confusion_matrix_cmap():
    """Returns custom colormap for confusion matrices"""
    return LinearSegmentedColormap.from_list('custom_cm', 
        ['#ffffff', COLORS['cat_2'], COLORS['cat_1']])


def setup_plot_style():
    """Configure matplotlib defaults with unified colour scheme"""
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=CAT_PALETTE)
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['axes.edgecolor'] = COLORS['grid']
    plt.rcParams['axes.labelcolor'] = COLORS['text']
    plt.rcParams['xtick.color'] = COLORS['text']
    plt.rcParams['ytick.color'] = COLORS['text']
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 12


# Data file path
DATA_FILE = 'PIP_case_study_data.csv'

# Numerical columns for analysis
NUMERICAL_COLS = [
    'total_visit_minutes', 'total_visit_pages', 'landing_pages_count', 
    'search_pages_count', 'property_pages_count', 'bkg_confirmation_pages_count',
    'bounce_visits_count', 'searched_destinations_count', 'hotel_star_rating'
]

# Categorical columns for analysis
CATEGORICAL_COLS = ['customer_type', 'loyalty_tier', 'platform', 'marketing_channel']

# Binary flag columns
BINARY_FLAGS = [
    ('coupon_flag', 'Coupon Usage'), 
    ('pay_now_flag', 'Pay Now Option'), 
    ('cancel_flag', 'Cancellation')
]

