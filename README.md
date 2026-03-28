# 🛢️ Global Fuel Prices Analysis & 2026 Forecasting 🌍

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange.svg)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

> **An end-to-end Exploratory Data Analysis (EDA) and Machine Learning forecasting project predicting global petroleum price trajectories through 2026, accounting for macroeconomic shocks and geopolitical risk premiums.**

---

## 📖 Overview

The global fuel market is highly sensitive to geopolitical factors. Recently, shifting geological and geopolitical landscapes—including supply chain instabilities and regional tensions—have heavily impacted the market. 

This repository houses a comprehensive data science pipeline that analyzes historical petroleum price trends over the last five decades (1970–present) and utilizes state-of-the-art predictive modeling to forecast future prices. By factoring in historical shocks and modern-day "risk premiums," this project provides actionable, data-driven insights into the future of global energy economics.

## ✨ Key Features

* **📈 Comprehensive EDA:** Visual analysis of historical price trends, overlaying major global events (1973 Oil Shock, 2008 Financial Crisis, COVID-19 drop, Russia-Ukraine conflict).
* **🧠 Advanced Feature Engineering:** Implementation of time-series specific features, including temporal variables, lagged price indicators, and moving averages to capture market momentum.
* **🤖 XGBoost Forecasting:** Utilizes an `XGBRegressor` model, specifically chosen for its superior ability to handle the non-linear, shock-prone nature of commodity pricing compared to traditional ARIMA models.
* **🌍 Geopolitical Risk Integration:** A forward-looking 2026 predictive model that explicitly incorporates simulated risk premiums based on current international tensions and OPEC+ production strategies.

## 🛠️ Technology Stack

* **Language:** Python 3
* **Data Manipulation:** `pandas`, `numpy`
* **Machine Learning:** `xgboost`, `scikit-learn`
* **Data Visualization:** `matplotlib`, `seaborn`
* **Environment:** Jupyter Notebook

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed, along with the required libraries. The core dataset (`fuel_prices_1970_2026.csv`) must be located in the root directory.

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/global-fuel-prices-forecasting.git](https://github.com/your-username/global-fuel-prices-forecasting.git)
   cd global-fuel-prices-forecasting
