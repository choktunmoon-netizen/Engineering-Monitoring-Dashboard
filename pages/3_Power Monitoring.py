import sys
from pathlib import Path

# แก้ไข Path เพื่อให้ค้นหาโฟลเดอร์ services เจอ ไม่ว่าจะรันจากโฟลเดอร์ไหน
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

import streamlit as st
from services.power import calculate_power, classify_power

# ตั้งค่าหน้าเว็บ Streamlit
st.set_page_config(
    page_title="Power Monitoring",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ ระบบคำนวณและจำแนกกำลังไฟฟ้า")
st.write("คำนวณและตรวจสอบระดับกำลังไฟฟ้าตามเงื่อนไขแรงดันและกระแส")

st.divider()

# สร้างแถบ Slider สำหรับรับค่าแรงดันและกระแส
col1, col2 = st.columns(2)

with col1:
    voltage = st.slider(
        "แรงดันไฟฟ้า (Voltage - V)",
        min_value=0.0,
        max_value=500.0,
        value=220.0,
        step=0.1,
        help="ค่า Voltage ต้องมากกว่า 0"
    )

with col2:
    current = st.slider(
        "กระแสไฟฟ้า (Current - A)",
        min_value=0.0,
        max_value=50.0,
        value=2.0,
        step=0.1,
        help="ค่า Current ต้องมากกว่าหรือเท่ากับ 0"
    )

st.divider()

# ส่วนคำนวณและแสดงผลลัพธ์
try:
    # เรียกใช้ฟังก์ชันคำนวณและจำแนกสถานะ
    power = calculate_power(voltage, current)
    status = classify_power(power)

    # แสดงผลค่ากำลังไฟฟ้า
    st.metric(
        label="กำลังไฟฟ้าที่คำนวณได้ (Power)",
        value=f"{power:,.2f} W"
    )

    # แสดงสถานะพร้อมสีการแจ้งเตือนตามระดับ
    if status == "NORMAL":
        st.success(f"สถานะ: **{status}** (น้อยกว่า 500 W)")
    elif status == "WARNING":
        st.warning(f"สถานะ: **{status}** (500 - 1000 W)")
    elif status == "CRITICAL":
        st.error(f"สถานะ: **{status}** (มากกว่า 1000 W)")

except ValueError as e:
    st.error(f"⚠️ เกิดข้อผิดพลาดทางเงื่อนไข: {e}")