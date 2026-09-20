import streamlit as st

st.set_page_config(
    page_title="System Summary",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Engineering Monitoring Dashboard")
st.write("ระบบติดตามสถานะของอุปกรณ์และสภาพแวดล้อมแบบรวมศูนย์")

st.markdown("---")

st.subheader("Modules in this dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🌡️ Temperature\n\n- NORMAL: ≤ 30°C\n- WARNING: > 30 to 35°C\n- CRITICAL: > 35°C")

with col2:
    st.info("💧 Humidity\n\n- NORMAL: 40–60%\n- WARNING: 30–39% or 61–70%\n- CRITICAL: < 30% or > 70%")

with col3:
    st.info("⚡ Power\n\n- NORMAL: < 500 W\n- WARNING: 500–1000 W\n- CRITICAL: > 1000 W")

with col4:
    st.info("🚨 Safety Alarm\n\n- Shows warnings for WARNING or CRITICAL states\n- Checks Temperature, Humidity and Power together")

st.markdown("---")

st.subheader("How to use")

st.write("1. Open each page from the left sidebar menu.")
st.write("2. Adjust the slider values to simulate real conditions.")
st.write("3. Check whether each module is NORMAL, WARNING, or CRITICAL.")
st.write("4. Review the Safety Alarm page to see system alerts.")

st.markdown("---")

st.subheader("Team roles")
team = {
    "Temperature Monitoring": "Builds the temperature logic and page",
    "Humidity Monitoring": "Builds the humidity logic and page",
    "Power Monitoring": "Builds the power calculation and page",
    "Safety Alarm": "Combines all statuses into alert messages",
    "Summary + QA": "Creates the overview page and checks project quality"
}

for member, task in team.items():
    st.write(f"- {member}: {task}")

st.markdown("---")

st.caption("This project follows the assignment workflow: separate logic, page UI, tests, and Git review before merge.")