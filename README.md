# demand-forecasting-retail
End-to-End Retail Sales Demand Forecasting System using Python &amp; Prophet
# 📊 Retail Sales Demand Forecasting System

An end-to-end Time Series Demand Forecasting solution designed to help retail and supply chain managers predict product demand, optimize inventory levels, and minimize stockout risks.

---

## 🌟 Key Features
- **Exploratory Data Analysis (EDA):** Deep analysis of historical sales trends, yearly seasonality, and day-of-week patterns.
- **Time Series Modeling:** Utilized **Meta Prophet** for high-precision time series forecasting with automated seasonality detection.
- **Model Evaluation:** Evaluated on historical test data achieving a Mean Absolute Error (**MAE**) of **0.4332** and **RMSE** of **0.5508**.
- **Interactive Dashboard:** Deployed a **Streamlit** web application for real-time visualization of 90-day future demand predictions.

---

## 🛠️ Tech Stack & Libraries
- **Language:** Python 3.10+
- **Data Manipulation:** `pandas`, `numpy`
- **Visualization:** `matplotlib`, `seaborn`
- **Time Series Modeling:** `prophet`
- **Web Framework / Dashboard:** `streamlit`
- **Model Serialization:** `joblib`

---

## 📂 Project Structure
```text
demand-forecasting-retail/
├── Demand_Forecasting_Project.ipynb  # Google Colab Data Analysis & Modeling Notebook
├── app.py                            # Streamlit Interactive Web Application
├── demand_forecast_results.csv        # 90-day forecasted demand dataset
├── demand_forecasting_model.pkl      # Trained Prophet forecasting model
└── README.md                         # Project documentation
```

---

## 🚀 Interactive Streamlit Dashboard Preview
The dashboard allows users to:
1. Filter demand predictions by custom time windows.
2. View key KPI metrics (Peak forecasted demand, Average demand, Standard deviation).
3. Download forecasted sales data as a CSV report for business intelligence integration.

---

## 📈 Model Performance & Evaluation
| Metric | Score |
| :--- | :--- |
| **MAE (Mean Absolute Error)** | `0.4332` |
| **RMSE (Root Mean Squared Error)** | `0.5508` |
| **Forecast Horizon** | 90 Days |

---

## 👤 Author
* **Hoda Asmat** - *Data Science Student & ML Enthusiast*
* **LinkedIn:** [Hoda Asmat](https://www.linkedin.com/in/hoda-asmatullah-496a4838a)
* **GitHub:** [@HodaAsmat](https://github.com/HodaAsmat)
