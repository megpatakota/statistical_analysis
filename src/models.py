"""
Machine Learning Models module for Hotels.com Churn Analysis
Contains model training, evaluation, and feature preparation functions
"""

import os
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import (classification_report, accuracy_score, precision_score, 
                             recall_score, f1_score, roc_auc_score)

# Results directory
RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'results')
os.makedirs(RESULTS_DIR, exist_ok=True)


def prepare_features(customer_df, save_feature_cols=True):
    """
    Prepare features for model training.
    
    Parameters:
    -----------
    customer_df : pd.DataFrame
        Customer-level aggregated dataframe
    save_feature_cols : bool
        Whether to save feature column names to disk
        
    Returns:
    --------
    tuple
        X (features), y (target), feature_cols, model_df_dummies
    """
    print("=" * 60)
    print("FEATURE PREPARATION FOR MODELLING")
    print("=" * 60)
    
    model_df = customer_df.copy()
    
    # Drop identifier and date columns
    model_df = model_df.drop(['email_address', 'first_booking', 'last_booking'], axis=1)
    
    # Handle NaN values
    model_df = model_df.fillna(0)
    
    # Encode categorical variables
    categorical_cols_model = ['primary_platform', 'primary_channel', 'customer_type']
    
    for col in categorical_cols_model:
        le = LabelEncoder()
        model_df[col + '_encoded'] = le.fit_transform(model_df[col].astype(str))
    
    # Create dummy variables
    model_df_dummies = pd.get_dummies(model_df, columns=categorical_cols_model, drop_first=True)
    
    # Get feature columns
    feature_cols = [col for col in model_df_dummies.columns if col != 'churned' 
                    and not col.endswith('_bookings') and col not in categorical_cols_model]
    
    X = model_df_dummies[feature_cols]
    y = model_df_dummies['churned']
    
    print(f"\n📊 Feature matrix shape: {X.shape}")
    print(f"📊 Target distribution:")
    print(f"   • Non-churned: {(y==0).sum():,} ({(y==0).mean()*100:.1f}%)")
    print(f"   • Churned: {(y==1).sum():,} ({(y==1).mean()*100:.1f}%)")
    
    if save_feature_cols:
        filepath = os.path.join(RESULTS_DIR, 'feature_cols.pkl')
        with open(filepath, 'wb') as f:
            pickle.dump(feature_cols, f)
        print(f"✓ Feature columns saved to {filepath}")
    
    return X, y, feature_cols, model_df_dummies


def split_and_scale_data(X, y, test_size=0.25, random_state=42, save_scaler=True):
    """
    Split data and scale features.
    
    Parameters:
    -----------
    X : pd.DataFrame
        Feature matrix
    y : pd.Series
        Target variable
    test_size : float
        Test set proportion
    random_state : int
        Random seed
    save_scaler : bool
        Whether to save the scaler to disk
        
    Returns:
    --------
    tuple
        X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled, scaler
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"\n✓ Train set: {len(X_train):,} samples")
    print(f"✓ Test set: {len(X_test):,} samples")
    
    if save_scaler:
        filepath = os.path.join(RESULTS_DIR, 'scaler.pkl')
        with open(filepath, 'wb') as f:
            pickle.dump(scaler, f)
        print(f"✓ Scaler saved to {filepath}")
    
    return X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled, scaler


def train_logistic_regression(X_train_scaled, y_train, X_test_scaled, y_test, save_model=True):
    """
    Train and evaluate Logistic Regression model.
    
    Parameters:
    -----------
    X_train_scaled, X_test_scaled : array
        Scaled feature matrices
    y_train, y_test : array
        Target variables
    save_model : bool
        Whether to save the model to disk
        
    Returns:
    --------
    tuple
        model, y_pred, y_prob
    """
    print("=" * 60)
    print("MODEL 1: LOGISTIC REGRESSION")
    print("=" * 60)
    
    model = LogisticRegression(max_iter=1000, random_state=42, class_weight='balanced')
    model.fit(X_train_scaled, y_train)
    
    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]
    
    _print_model_performance(y_test, y_pred, y_prob)
    
    if save_model:
        filepath = os.path.join(RESULTS_DIR, 'logistic_regression.pkl')
        with open(filepath, 'wb') as f:
            pickle.dump(model, f)
        print(f"✓ Model saved to {filepath}")
    
    return model, y_pred, y_prob


def train_random_forest(X_train, y_train, X_test, y_test, save_model=True):
    """
    Train and evaluate Random Forest model.
    
    Parameters:
    -----------
    X_train, X_test : pd.DataFrame
        Feature matrices
    y_train, y_test : array
        Target variables
    save_model : bool
        Whether to save the model to disk
        
    Returns:
    --------
    tuple
        model, y_pred, y_prob
    """
    print("=" * 60)
    print("MODEL 2: RANDOM FOREST")
    print("=" * 60)
    
    model = RandomForestClassifier(
        n_estimators=200, max_depth=15, min_samples_split=10,
        random_state=42, class_weight='balanced', n_jobs=-1
    )
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    
    _print_model_performance(y_test, y_pred, y_prob)
    
    if save_model:
        filepath = os.path.join(RESULTS_DIR, 'random_forest.pkl')
        with open(filepath, 'wb') as f:
            pickle.dump(model, f)
        print(f"✓ Model saved to {filepath}")
    
    return model, y_pred, y_prob


def train_gradient_boosting(X_train, y_train, X_test, y_test, save_model=True):
    """
    Train and evaluate Gradient Boosting model.
    
    Parameters:
    -----------
    X_train, X_test : pd.DataFrame
        Feature matrices
    y_train, y_test : array
        Target variables
    save_model : bool
        Whether to save the model to disk
        
    Returns:
    --------
    tuple
        model, y_pred, y_prob
    """
    print("=" * 60)
    print("MODEL 3: GRADIENT BOOSTING")
    print("=" * 60)
    
    model = GradientBoostingClassifier(
        n_estimators=150, max_depth=5, learning_rate=0.1,
        random_state=42, min_samples_split=10
    )
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    
    _print_model_performance(y_test, y_pred, y_prob)
    
    if save_model:
        filepath = os.path.join(RESULTS_DIR, 'gradient_boosting.pkl')
        with open(filepath, 'wb') as f:
            pickle.dump(model, f)
        print(f"✓ Model saved to {filepath}")
    
    return model, y_pred, y_prob


def _print_model_performance(y_test, y_pred, y_prob):
    """Print model performance metrics."""
    print("\n📊 Model Performance:")
    print("-" * 40)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall: {recall_score(y_test, y_pred):.4f}")
    print(f"F1-Score: {f1_score(y_test, y_pred):.4f}")
    print(f"ROC-AUC: {roc_auc_score(y_test, y_prob):.4f}")
    
    print("\n📋 Classification Report:")
    print(classification_report(y_test, y_pred, target_names=['Retained', 'Churned']))


def get_logistic_regression_odds_ratios(model, feature_names):
    """
    Calculate odds ratios from logistic regression coefficients.
    
    Parameters:
    -----------
    model : LogisticRegression
        Trained model
    feature_names : list
        Feature names
        
    Returns:
    --------
    pd.DataFrame
        Odds ratios dataframe
    """
    print("=" * 60)
    print("LOGISTIC REGRESSION - ODDS RATIOS")
    print("=" * 60)
    
    odds_ratios = pd.DataFrame({
        'Feature': feature_names,
        'Coefficient': model.coef_[0],
        'Odds_Ratio': np.exp(model.coef_[0])
    })
    odds_ratios['Abs_Coef'] = np.abs(odds_ratios['Coefficient'])
    odds_ratios = odds_ratios.sort_values('Abs_Coef', ascending=False)
    
    print("\n📊 Top 15 Most Important Features (by Odds Ratio):")
    print("-" * 60)
    print("\nInterpretation: Odds Ratio > 1 = increases churn risk")
    print("               Odds Ratio < 1 = decreases churn risk\n")
    
    for _, row in odds_ratios.head(15).iterrows():
        direction = "↑ INCREASES" if row['Odds_Ratio'] > 1 else "↓ DECREASES"
        print(f"  {row['Feature'][:35]:35} | OR: {row['Odds_Ratio']:.3f} | {direction} churn risk")
    
    return odds_ratios


def score_customers(model, X, model_df_dummies):
    """
    Score all customers with churn probability.
    
    Parameters:
    -----------
    model : trained model
        Model to use for scoring
    X : pd.DataFrame
        Feature matrix
    model_df_dummies : pd.DataFrame
        Full dataframe with target
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with churn probabilities and risk categories
    """
    customer_scores = model_df_dummies.copy()
    customer_scores['churn_probability'] = model.predict_proba(X)[:, 1]
    customer_scores['risk_category'] = pd.cut(
        customer_scores['churn_probability'], 
        bins=[0, 0.3, 0.5, 0.7, 1.0],
        labels=['Low Risk', 'Medium Risk', 'High Risk', 'Critical Risk']
    )
    
    return customer_scores


def save_models(lr_model, rf_model, gb_model, scaler, feature_cols):
    """
    Save trained models and preprocessing objects to disk.
    
    Parameters:
    -----------
    lr_model : LogisticRegression
        Trained logistic regression model
    rf_model : RandomForestClassifier
        Trained random forest model
    gb_model : GradientBoostingClassifier
        Trained gradient boosting model
    scaler : StandardScaler
        Fitted scaler
    feature_cols : list
        Feature column names
    """
    print("\n" + "=" * 60)
    print("SAVING MODELS AND PREPROCESSORS")
    print("=" * 60)
    
    models_to_save = {
        'logistic_regression': lr_model,
        'random_forest': rf_model,
        'gradient_boosting': gb_model,
        'scaler': scaler,
        'feature_cols': feature_cols
    }
    
    for name, obj in models_to_save.items():
        filepath = os.path.join(RESULTS_DIR, f'{name}.pkl')
        with open(filepath, 'wb') as f:
            pickle.dump(obj, f)
        print(f"✓ Saved {name} to {filepath}")
    
    print(f"\n✓ All models saved to {RESULTS_DIR}/")


def load_models():
    """
    Load trained models and preprocessing objects from disk.
    
    Returns:
    --------
    dict
        Dictionary containing all loaded models and objects
    """
    print("\n" + "=" * 60)
    print("LOADING SAVED MODELS")
    print("=" * 60)
    
    models = {}
    model_files = {
        'logistic_regression': 'logistic_regression.pkl',
        'random_forest': 'random_forest.pkl',
        'gradient_boosting': 'gradient_boosting.pkl',
        'scaler': 'scaler.pkl',
        'feature_cols': 'feature_cols.pkl'
    }
    
    for name, filename in model_files.items():
        filepath = os.path.join(RESULTS_DIR, filename)
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                models[name] = pickle.load(f)
            print(f"✓ Loaded {name} from {filepath}")
        else:
            print(f"⚠ {name} not found at {filepath}")
            return None
    
    print(f"\n✓ All models loaded from {RESULTS_DIR}/")
    return models


def models_exist():
    """
    Check if saved models exist.
    
    Returns:
    --------
    bool
        True if all model files exist, False otherwise
    """
    required_files = [
        'logistic_regression.pkl',
        'random_forest.pkl',
        'gradient_boosting.pkl',
        'scaler.pkl',
        'feature_cols.pkl'
    ]
    
    return all(os.path.exists(os.path.join(RESULTS_DIR, f)) for f in required_files)

