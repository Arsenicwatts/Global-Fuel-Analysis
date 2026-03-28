import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import math
import warnings

warnings.filterwarnings('ignore')

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Global Fuel Prices Forecast",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CACHED DATA & MODEL LOADING
# ==========================================
@st.cache_data
def load_data():
    """Loads and prepares the historical dataset."""
    try:
        df = pd.read_csv('fuel_prices_1970_2026.csv', parse_dates=['Date'])
        df.set_index('Date', inplace=True)
        df.sort_index(inplace=True)
        return df
    except FileNotFoundError:
        st.error("⚠️ Error: 'fuel_prices_1970_2026.csv' not found. Please ensure it is in the same directory as this script.")
        st.stop()

def create_features(data):
    """Generates time-series features (Lags & Rolling Means)."""
    features = data.copy()
    features['Month'] = features.index.month
    features['Year'] = features.index.year
    features['Quarter'] = features.index.quarter
    
    # Lagged features
    features['Lag_1'] = features['Crude_Oil_Price'].shift(1)
    features['Lag_3'] = features['Crude_Oil_Price'].shift(3)
    features['Lag_6'] = features['Crude_Oil_Price'].shift(6)
    
    # Rolling averages
    features['Rolling_Mean_3'] = features['Crude_Oil_Price'].rolling(window=3).mean()
    features['Rolling_Mean_12'] = features['Crude_Oil_Price'].rolling(window=12).mean()
    
    return features.dropna()

@st.cache_resource
def train_xgboost(_df):
    """Trains the XGBoost model and returns the model & evaluation metrics."""
    model_df = create_features(_df)
    
    # Split train/test
    train = model_df[model_df.index < '2023-01-01']
    test = model_df[model_df.index >= '2023-01-01']
    
    FEATURES = ['Month', 'Year', 'Quarter', 'Lag_1', 'Lag_3', 'Lag_6', 'Rolling_Mean_3', 'Rolling_Mean_12']
    TARGET = 'Crude_Oil_Price'
    
    X_train, y_train = train[FEATURES], train[TARGET]
    X_test, y_test = test[FEATURES], test[TARGET]
    
    # Model definition & training
    reg = XGBRegressor(n_estimators=1000, early_stopping_rounds=50, learning_rate=0.01)
    reg.fit(X_train, y_train, eval_set=[(X_train, y_train), (X_test, y_test)], verbose=False)
    
    # Evaluation
    predictions = reg.predict(X_test)
    rmse = math.sqrt(mean_squared_error(y_test, predictions))
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    return reg, FEATURES, rmse, mae, r2

# ==========================================
# SIDEBAR UI
# ==========================================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1996/1996803.png", width=100)
st.sidebar.title("Configuration")
st.sidebar.markdown("Adjust parameters below to simulate different geopolitical scenarios.")

st.sidebar.subheader("Geopolitical Risk Premium")
st.sidebar.markdown("""
*Simulate the impact of tensions in the Middle East by applying a percentage markup to the model's baseline predictions.*
""")
risk_min = st.sidebar.slider("Minimum Premium (%)", min_value=0, max_value=20, value=5, step=1)
risk_max = st.sidebar.slider("Maximum Premium (%)", min_value=0, max_value=40, value=12, step=1)

st.sidebar.subheader("Forecast Horizon")
forecast_years = st.sidebar.number_input("Years to Forecast", min_value=1, max_value=5, value=2)

st.sidebar.markdown("---")
st.sidebar.info("Model powered by XGBoost. Built by Atharva Chauhan.")

# ==========================================
# MAIN APP UI
# ==========================================
st.title("🛢️ Global Fuel Prices Analytics & Forecasting")
st.markdown("""
Welcome to the interactive predictive dashboard. This application utilizes historical World Bank commodity data and an **XGBoost Machine Learning model** to forecast global crude oil prices, adjusting for contemporary geopolitical shocks.
""")

# Load Data & Train Model
with st.spinner("Loading data and training XGBoost model..."):
    df = load_data()
    model, feature_cols, rmse, mae, r2 = train_xgboost(df)

# Top Metrics Row
st.subheader("📊 Model Performance & Market Snapshot")
col1, col2, col3, col4 = st.columns(4)

latest_date = df.index[-1]
latest_price = df['Crude_Oil_Price'].iloc[-1]

col1.metric("Latest Recorded Price", f"${latest_price:.2f}", f"{latest_date.strftime('%b %Y')}")
col2.metric("Model RMSE", f"${rmse:.2f}", "Root Mean Square Error", delta_color="inverse")
col3.metric("Model MAE", f"${mae:.2f}", "Mean Absolute Error", delta_color="inverse")
col4.metric("Model R² Score", f"{r2:.3f}", "Accuracy Metric")

st.markdown("---")

# ==========================================
# FORECASTING ENGINE
# ==========================================
st.subheader(f"🔮 Predictive Forecast (up to {latest_date.year + forecast_years})")

# Determine frequency mapping (handling newer pandas ME vs older M/MS)
freq_str = 'MS' # Month Start to match 'YYYY-MM-01' formatting

future_dates = pd.date_range(
    start=latest_date + pd.DateOffset(months=1), 
    periods=12 * forecast_years, 
    freq=freq_str
)

future_df = pd.DataFrame(index=future_dates)
future_df['Crude_Oil_Price'] = np.nan
combined_df = pd.concat([df[['Crude_Oil_Price']], future_df])

# Recursive Forecasting Loop
progress_bar = st.progress(0)
for i, date in enumerate(future_dates):
    # Calculate features for current timeframe
    feats = create_features(combined_df.loc[:date]).iloc[-1:]
    
    # Predict baseline
    base_pred = model.predict(feats[feature_cols])[0]
    
    # Apply user-defined Risk Premium
    premium_multiplier = np.random.uniform(1 + (risk_min/100), 1 + (risk_max/100))
    pred_with_risk = base_pred * premium_multiplier
    
    combined_df.loc[date, 'Crude_Oil_Price'] = pred_with_risk
    progress_bar.progress((i + 1) / len(future_dates))

progress_bar.empty() # Clear progress bar when done

# Extract just the forecasted portion
forecast_only = combined_df.loc[future_dates]

# Display End of Forecast Metric
end_price = forecast_only['Crude_Oil_Price'].iloc[-1]
st.success(f"**Forecast Generated:** The projected price by {future_dates[-1].strftime('%B %Y')} is **${end_price:.2f}** per barrel (accounting for a {risk_min}% to {risk_max}% geopolitical risk premium).")

# ==========================================
# INTERACTIVE PLOTLY CHART
# ==========================================
st.markdown("### Historical vs. Forecasted Trajectory")

# To keep the chart readable, we will only plot from 2010 onwards by default
plot_start_date = '2010-01-01'
historical_plot_data = df[df.index >= plot_start_date]

fig = go.Figure()

# Historical Data Trace
fig.add_trace(go.Scatter(
    x=historical_plot_data.index, 
    y=historical_plot_data['Crude_Oil_Price'], 
    mode='lines',
    name='Historical Price',
    line=dict(color='#1f77b4', width=2)
))

# Forecast Data Trace
# We prepend the last historical point to the forecast so the line connects seamlessly
connecting_point = pd.DataFrame(historical_plot_data.iloc[-1:]['Crude_Oil_Price'])
forecast_plot_data = pd.concat([connecting_point, forecast_only])

fig.add_trace(go.Scatter(
    x=forecast_plot_data.index, 
    y=forecast_plot_data['Crude_Oil_Price'], 
    mode='lines',
    name='Forecasted Price (w/ Risk Premium)',
    line=dict(color='#d62728', width=2, dash='dash')
))

# Chart Formatting
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Crude Oil Price (USD / bbl)',
    hovermode='x unified',
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    margin=dict(l=0, r=0, t=40, b=0),
    template="plotly_white"
)

# Highlight major events via background shading (Plotly shapes)
fig.add_vrect(x0="2020-01-01", x1="2021-01-01", fillcolor="blue", opacity=0.1, layer="below", line_width=0, annotation_text="COVID-19 Drop", annotation_position="top left")
fig.add_vrect(x0="2022-01-01", x1="2023-01-01", fillcolor="red", opacity=0.1, layer="below", line_width=0, annotation_text="Russia-Ukraine", annotation_position="top left")

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# DATA VIEWER & EXPORT
# ==========================================
with st.expander("🔎 View & Export Raw Forecast Data"):
    st.markdown("Below is the tabular data for the generated forecast. You can download this as a CSV for further reporting.")
    
    # Format dataframe for display
    display_df = forecast_only.copy()
    display_df.index.name = 'Date'
    display_df['Crude_Oil_Price'] = display_df['Crude_Oil_Price'].apply(lambda x: f"${x:.2f}")
    
    st.dataframe(display_df, use_container_width=True)
    
    # CSV Download Button
    csv = forecast_only.to_csv().encode('utf-8')
    st.download_button(
        label="📥 Download Forecast as CSV",
        data=csv,
        file_name='2026_crude_oil_forecast.csv',
        mime='text/csv',
    )
