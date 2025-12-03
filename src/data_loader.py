"""
Data loading and preprocessing module for Hotels.com Churn Analysis
"""

import pandas as pd
import numpy as np
from config import DATA_FILE


def load_data(filepath=DATA_FILE):
    """
    Load the customer booking data from CSV file.
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file
        
    Returns:
    --------
    pd.DataFrame
        Raw dataframe
    """
    df = pd.read_csv(filepath)
    print(f"✓ Data loaded: {df.shape[0]:,} rows × {df.shape[1]} columns")
    print(f"  Date range: {df['bk_date'].min()} to {df['bk_date'].max()}")
    return df


def preprocess_data(df):
    """
    Preprocess the booking data with feature engineering.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Raw dataframe
        
    Returns:
    --------
    pd.DataFrame
        Preprocessed dataframe with derived features
    """
    df_processed = df.copy()
    
    # Convert date columns to datetime
    df_processed['bk_date'] = pd.to_datetime(df_processed['bk_date'])
    df_processed['cancel_date'] = pd.to_datetime(df_processed['cancel_date'], errors='coerce')
    
    # Handle cancel_date - replace 'NA' with NaT
    df_processed.loc[df_processed['cancel_date'].isna(), 'cancel_date'] = pd.NaT
    
    # Convert loyalty_tier to integer
    df_processed['loyalty_tier'] = df_processed['loyalty_tier'].astype(int)
    
    # Create derived features
    # 1. Days until cancellation (if cancelled)
    df_processed['days_to_cancel'] = (df_processed['cancel_date'] - df_processed['bk_date']).dt.days
    
    # 2. Booking month and day of week
    df_processed['booking_month'] = df_processed['bk_date'].dt.month
    df_processed['booking_dayofweek'] = df_processed['bk_date'].dt.dayofweek
    
    # 3. Pages per minute engagement ratio
    df_processed['pages_per_minute'] = np.where(
        df_processed['total_visit_minutes'] > 0,
        df_processed['total_visit_pages'] / df_processed['total_visit_minutes'],
        0
    )
    
    # 4. Property page ratio
    df_processed['property_page_ratio'] = np.where(
        df_processed['total_visit_pages'] > 0,
        df_processed['property_pages_count'] / df_processed['total_visit_pages'],
        0
    )
    
    # 5. Search efficiency
    df_processed['search_efficiency'] = np.where(
        df_processed['total_visit_minutes'] > 0,
        df_processed['searched_destinations_count'] / df_processed['total_visit_minutes'],
        0
    )
    
    # Replace empty marketing_channel with 'Unknown'
    df_processed['marketing_channel'] = df_processed['marketing_channel'].replace('', 'Unknown')
    
    print(f"✓ Data preprocessed: {df_processed.shape[0]:,} rows × {df_processed.shape[1]} columns")
    return df_processed


def aggregate_to_customer_level(df_processed):
    """
    Aggregate booking-level data to customer level.
    
    Parameters:
    -----------
    df_processed : pd.DataFrame
        Preprocessed booking-level dataframe
        
    Returns:
    --------
    pd.DataFrame
        Customer-level aggregated dataframe
    """
    customer_df = df_processed.groupby('email_address').agg({
        # Booking behaviour
        'booking_id': 'count',
        'churn_flag': 'max',
        
        # Payment behaviour
        'coupon_flag': ['sum', 'mean'],
        'pay_now_flag': ['sum', 'mean'],
        'cancel_flag': ['sum', 'mean'],
        
        # Loyalty
        'loyalty_tier': 'max',
        
        # Platform preference
        'platform': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown',
        
        # Marketing channel
        'marketing_channel': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Unknown',
        
        # Customer type
        'customer_type': 'last',
        
        # Website engagement metrics
        'total_visit_minutes': 'mean',
        'total_visit_pages': 'mean',
        'search_pages_count': 'mean',
        'property_pages_count': 'mean',
        'bounce_visits_count': 'mean',
        'searched_destinations_count': 'mean',
        
        # Hotel preferences
        'hotel_star_rating': 'mean',
        
        # Derived features
        'pages_per_minute': 'mean',
        'property_page_ratio': 'mean',
        
        # Booking dates
        'bk_date': ['min', 'max']
    }).reset_index()
    
    # Flatten column names
    customer_df.columns = ['_'.join(col).strip('_') if isinstance(col, tuple) else col 
                           for col in customer_df.columns]
    
    # Rename columns for clarity
    customer_df = customer_df.rename(columns={
        'booking_id_count': 'total_bookings',
        'churn_flag_max': 'churned',
        'coupon_flag_sum': 'coupon_bookings',
        'coupon_flag_mean': 'coupon_rate',
        'pay_now_flag_sum': 'pay_now_bookings',
        'pay_now_flag_mean': 'pay_now_rate',
        'cancel_flag_sum': 'cancelled_bookings',
        'cancel_flag_mean': 'cancellation_rate',
        'loyalty_tier_max': 'max_loyalty_tier',
        'platform_<lambda>': 'primary_platform',
        'marketing_channel_<lambda>': 'primary_channel',
        'customer_type_last': 'customer_type',
        'total_visit_minutes_mean': 'avg_visit_minutes',
        'total_visit_pages_mean': 'avg_visit_pages',
        'search_pages_count_mean': 'avg_search_pages',
        'property_pages_count_mean': 'avg_property_pages',
        'bounce_visits_count_mean': 'avg_bounce_visits',
        'searched_destinations_count_mean': 'avg_destinations_searched',
        'hotel_star_rating_mean': 'avg_star_rating',
        'pages_per_minute_mean': 'avg_pages_per_minute',
        'property_page_ratio_mean': 'avg_property_ratio',
        'bk_date_min': 'first_booking',
        'bk_date_max': 'last_booking'
    })
    
    # Calculate customer tenure
    customer_df['tenure_days'] = (customer_df['last_booking'] - customer_df['first_booking']).dt.days
    
    print(f"✓ Customer-level aggregation: {len(customer_df):,} unique customers")
    print(f"  Churn rate at customer level: {customer_df['churned'].mean()*100:.2f}%")
    
    return customer_df


def get_data_summary(df):
    """Print summary statistics of the dataset."""
    print("=" * 60)
    print("DATASET SUMMARY")
    print("=" * 60)
    print(f"\nShape: {df.shape[0]:,} rows × {df.shape[1]} columns")
    print(f"\nChurn Rate: {df['churn_flag'].mean()*100:.2f}%")
    print(f"  - Retained: {(df['churn_flag']==0).sum():,}")
    print(f"  - Churned: {(df['churn_flag']==1).sum():,}")
    
    print("\n" + "-" * 40)
    print("Missing Values:")
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if len(missing) > 0:
        for col, count in missing.items():
            print(f"  {col}: {count:,} ({count/len(df)*100:.2f}%)")
    else:
        print("  None detected")

