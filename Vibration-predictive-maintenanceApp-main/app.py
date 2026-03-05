import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

# --- 1. ส่วนหัวเว็บไซต์ ---
st.set_page_config(page_title="Vibration Predictor", layout="wide")
st.title("📊 ระบบพยากรณ์ความเสียหายเครื่องจักร (ISO 10816-3)")

# --- 2. แถบเมนูข้าง (Sidebar) ---
st.sidebar.header("ตั้งค่าตัวแปร")
group = st.sidebar.selectbox("กลุ่มเครื่องจักร", ["Group 1 (Large)", "Group 2 (Medium)"])
foundation = st.sidebar.radio("ประเภทฐาน", ["Rigid", "Flexible"])
days_to_predict = st.sidebar.slider("พยากรณ์ล่วงหน้า (วัน)", 7, 60, 30)

# --- 3. ฟังก์ชันจำลองข้อมูล (Simulate Data) ---
def load_data():
    dates = [datetime.now() - timedelta(days=x) for x in range(100)]
    dates.reverse()
    # จำลองแรงสั่นสะเทือนค่อยๆ สูงขึ้น
    vals = 1.0 + np.linspace(0, 7, 100) + np.random.normal(0, 0.4, 100)
    return pd.DataFrame({'Date': dates, 'Velocity': vals})

df = load_data()

# --- 4. การคำนวณทางสถิติ (Prediction) ---
df['DayIndex'] = np.arange(len(df))
model = LinearRegression().fit(df[['DayIndex']], df['Velocity'])

# ทำนายอนาคต
future_days = np.arange(len(df), len(df) + days_to_predict).reshape(-1, 1)
preds = model.predict(future_days)
future_dates = [df['Date'].iloc[-1] + timedelta(days=i) for i in range(1, days_to_predict+1)]

# --- 5. การแสดงกราฟ (Visualization) ---
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Date'], y=df['Velocity'], name='ข้อมูลจริง'))
fig.add_trace(go.Scatter(x=future_dates, y=preds, name='ผลพยากรณ์', line=dict(dash='dash', color='red')))

# ขีดเส้นมาตรฐาน ISO (ตัวอย่าง Group 1 Rigid)
fig.add_hline(y=4.5, line_color="orange", annotation_text="เตือน (Zone C)")
fig.add_hline(y=7.1, line_color="red", annotation_text="อันตราย (Zone D)")

st.plotly_chart(fig, use_container_width=True)

# สรุปผล
st.subheader("สถานะปัจจุบันและการวิเคราะห์")
st.write(f"ค่าปัจจุบัน: {df['Velocity'].iloc[-1]:.2f} mm/s")
if preds[-1] > 7.1:
    st.error(f"⚠️ คำเตือน: เครื่องจักรมีแนวโน้มจะพังภายใน {days_to_predict} วัน!")
else:
    st.success("✅ เครื่องจักรยังอยู่ในเกณฑ์ที่วางแผนซ่อมบำรุงได้")