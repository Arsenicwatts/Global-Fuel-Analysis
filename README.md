🛢️ Global Fuel Prices Analytics & Interactive Forecasting 🌍

An end-to-end Machine Learning pipeline and interactive web dashboard predicting global petroleum price trajectories through 2026, accounting for macroeconomic shocks and geopolitical risk premiums.

📖 Overview

The global fuel market is highly sensitive to geopolitical factors. Recently, shifting geological and geopolitical landscapes—including supply chain instabilities and regional tensions in the Middle East—have heavily impacted the market.

This repository houses both a comprehensive Data Science Pipeline (Jupyter Notebook) and a Fully Fledged Web Application (Streamlit). It analyzes historical petroleum price trends over the last five decades (1970–present) and utilizes state-of-the-art predictive modeling to forecast future prices. By factoring in historical shocks and allowing users to dynamically adjust modern-day "risk premiums," this project provides actionable, data-driven insights into the future of global energy economics.

✨ Key Features

🖥️ Interactive Web Dashboard: A beautiful, responsive UI built with Streamlit that allows users to explore the data and model predictions in real-time.

🌍 Dynamic Geopolitical Risk Simulator: Interactive sidebar sliders allow users to simulate different global scenarios by applying percentage markups to the model's baseline predictions.

🤖 XGBoost Forecasting Engine: Utilizes an XGBRegressor model, specifically chosen for its superior ability to handle the non-linear, shock-prone nature of commodity pricing.

📊 Interactive Plotly Visualizations: Hover, zoom, and explore historical vs. forecasted trajectories, complete with background shading for major historical events (e.g., 2008 Financial Crisis, COVID-19, Russia-Ukraine).

🧠 Advanced Feature Engineering: Implementation of time-series specific features, including temporal variables, lagged price indicators, and moving averages to capture market momentum.

🛠️ Technology Stack

Language: Python 3

Web Framework: streamlit

Machine Learning: xgboost, scikit-learn

Data Manipulation: pandas, numpy

Data Visualization: plotly, matplotlib, seaborn

🚀 Getting Started

Prerequisites

Ensure you have Python installed. The core dataset (fuel_prices_1970_2026.csv) must be located in the root directory.

Installation & Running the App

Clone the repository:

git clone [https://github.com/your-username/global-fuel-prices-forecasting.git](https://github.com/your-username/global-fuel-prices-forecasting.git)
cd global-fuel-prices-forecasting



Install dependencies:

pip install streamlit pandas numpy xgboost scikit-learn plotly



Launch the Streamlit App:

streamlit run app.py



The app will automatically open in your default web browser at http://localhost:8501.

📂 Project Structure

📁 global-fuel-prices-forecasting
│
├── 📄 app.py                                          # Main Streamlit web application
├── 📄 global-fuel-prices-analysis-2026-forecasting.ipynb  # In-depth EDA & Model Training Notebook
├── 📄 fuel_prices_1970_2026.csv                       # Historical World Bank commodity dataset
└── 📄 README.md                                       # Project documentation



💡 Key Insights & 2026 Outlook

The machine learning model, augmented by our geopolitical tension factor, strongly indicates that as long as instability remains within critical oil-producing regions, global supply chains will price in a continuous "Risk Premium." The forecast anticipates heavily fluctuating prices, potentially surpassing $90–$100 per barrel during acute macro-economic or geopolitical flare-ups.

👨‍💻 Team

Team Leader

Sagun Yadav - Connect on LinkedIn

Members

Atharva Chauhan - Connect on LinkedIn

Dhyey Patel - Connect on LinkedIn

Prasang Verma - Connect on LinkedIn

Darshan Desale - Connect on LinkedIn

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
