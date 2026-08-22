import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ضبط إعدادات الصفحة
st.set_page_config(page_title="Retail Demand Forecasting", page_icon="📊", layout="wide")

st.title("📊 Retail Sales Demand Forecasting System")
st.markdown("هذا التطبيق يستعرض التنبؤات المستقبلية للطلب والمبيعات لمدة 90 يوماً باستخدام نموذج **Prophet** للتحليل الزمني.")

# تحميل البيانات
@st.cache_data
def load_data():
    df = pd.read_csv('demand_forecast_results.csv')
    df['ds'] = pd.to_datetime(df['ds'])
    return df

df_forecast = load_data()

# عرض مؤشرات الأداء الرئيسية (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric("أعلى طلب متوقع", f"{df_forecast['yhat'].max():.2f}")
col2.metric("متوسط الطلب اليومي", f"{df_forecast['yhat'].mean():.2f}")
col3.metric("أدنى طلب متوقع", f"{df_forecast['yhat'].min():.2f}")

st.markdown("---")

# الرسم البياني التفاعلي
st.subheader("📈 منحنى التنبؤ المستقبلي بالطلب")
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df_forecast['ds'], df_forecast['yhat'], label='Predicted Demand', color='#008080', linewidth=2)
ax.fill_between(df_forecast['ds'], df_forecast['yhat_lower'], df_forecast['yhat_upper'], color='#008080', alpha=0.2, label='Uncertainty Interval')
ax.set_xlabel("Date")
ax.set_ylabel("Demand")
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()
st.pyplot(fig)

# عرض جدول البيانات
if st.checkbox("عرض جدول التنبؤات التفصيلي"):
    st.dataframe(df_forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].rename(columns={'ds': 'Date', 'yhat': 'Forecast', 'yhat_lower': 'Lower Bound', 'yhat_upper': 'Upper Bound'}))
