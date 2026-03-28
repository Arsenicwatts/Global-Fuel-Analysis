🛢️ Global Fuel Prices Analysis & 2026 Forecasting (1970 - 2026) 🌍
📖 Overview
This project provides a comprehensive Exploratory Data Analysis (EDA) and Machine Learning forecasting model for global crude oil prices. It examines historical petroleum price trends over the last five decades, contextualizes them within major geopolitical and economic events, and utilizes advanced time-series forecasting to predict 2026 price trajectories.

A unique aspect of this analysis is the incorporation of a Geopolitical Risk Premium, which accounts for contemporary supply chain instabilities and tensions in the Middle East.

✨ Key Features
Historical EDA: Visualizes the impact of major global events on oil prices, including the 1973 Oil Shock, 2008 Financial Crisis, COVID-19 pandemic, and the Russia-Ukraine conflict.

Geopolitical & Economic Context: Expert breakdowns of OPEC's influence, top global producers vs. consumers, and the drivers of price volatility.

Advanced Feature Engineering: Utilizes temporal features, lagged variables, and rolling averages to capture complex market momentum and seasonality.

XGBoost Forecasting: Employs an XGBRegressor model to handle the non-linear, shock-prone nature of commodity pricing, outperforming traditional ARIMA models in highly volatile conditions.

2026 Predictive Modeling: Generates a forward-looking forecast for 2026, explicitly incorporating simulated risk premiums based on current international tensions.

🛠️ Technologies & Libraries Used
Python 3.x

Data Manipulation: pandas, numpy

Data Visualization: matplotlib, seaborn

Machine Learning: xgboost, scikit-learn

🚀 Getting Started
Prerequisites
Ensure you have the required dataset (fuel_prices_1970_2026.csv) downloaded and placed in the same directory as the notebook.

Installation
You will need to install the required Python packages. You can do this via pip:

Bash

pip install pandas numpy matplotlib seaborn xgboost scikit-learn
Running the Project
Clone this repository or download the .ipynb file.

Open your terminal or command prompt.

Launch Jupyter Notebook or Jupyter Lab:

Bash

jupyter notebook
Open global-fuel-prices-analysis-2026-forecasting.ipynb and run the cells sequentially.

📊 Notebook Structure
Expert Analysis: Geopolitics & Fuel Prices

OPEC: Its Role & Member Countries

Global Petroleum Production: Top Producing vs. Consuming Countries

Exploratory Data Analysis (EDA): Visualizing historical trends and shocks.

Machine Learning Forecasting: Data splitting, feature engineering, and training the XGBoost model.

Future Predictions & Discussion: Generating the 2026 forecast and applying the risk premium.

Dataset QA: Common questions regarding data sourcing and methodology.

📈 Key Insights & 2026 Outlook
The machine learning model, augmented by the geopolitical tension factor, strongly indicates that as long as instability remains within critical oil-producing regions, global supply chains will price in a continuous "Risk Premium." The model anticipates prices fluctuating heavily, potentially surpassing $90-$100 per barrel during acute flare-ups in 2026.

🗄️ Data Source
The core historical data originates from the World Bank's Open Data initiatives (Commodity Price Data / The Pink Sheet).
