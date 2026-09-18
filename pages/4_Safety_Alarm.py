import streamlit as st
from services.alarm import generate_alarms

st.title("Safety Alarm System")

st.markdown("เลือกสถานะจำลองของแต่ละโมดูลเพื่อตรวจสอบการแจ้งเตือนระบบ")

col1, col2, col3 = st.columns(3)

with col1:
    temp_s = st.selectbox("Temperature Status", ["NORMAL", "WARNING", "CRITICAL"])
with col2:
    humid_s = st.selectbox("Humidity Status", ["NORMAL", "WARNING", "CRITICAL"])
with col3:
    power_s = st.selectbox("Power Status", ["NORMAL", "WARNING", "CRITICAL"])

st.divider()

try:
    alarms = generate_alarms(temp_s, humid_s, power_s)
    
    st.subheader("สถานะการแจ้งเตือนปัจจุบัน:")
    if not alarms:
        st.success("ระบบปกติ ไม่มีข้อความแจ้งเตือน")
    else:
        for alarm in alarms:
            if "CRITICAL" in alarm:
                st.error(alarm)
            else:
                st.warning(alarm)
except ValueError as e:
    st.error(f"เกิดข้อผิดพลาด: {e}")