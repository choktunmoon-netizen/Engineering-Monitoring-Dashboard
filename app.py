import streamlit as st

st.set_page_config(
    page_title="Engineering Monitoring Dashboard",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Engineering Monitoring Dashboard")
st.write("A team dashboard for monitoring temperature, humidity, power, and safety conditions.")

st.markdown("---")

st.subheader("Project overview")

st.write("This project simulates system monitoring using Streamlit sliders and logic functions.")
st.write("Each module classifies values as NORMAL, WARNING, or CRITICAL and warns the user when the system needs attention.")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🌡️ Temperature\n\nMonitors thermal status")
with col2:
    st.info("💧 Humidity\n\nMonitors moisture level")
with col3:
    st.info("⚡ Power\n\nCalculates power from voltage and current")
with col4:
    st.info("🚨 Safety Alarm\n\nShows urgent alerts from all modules")

st.markdown("---")

st.subheader("Members and roles")

member_data = [
    ("Narilak Yawan", "Temperature Monitoring"),
    ("Kitthisak Kampheang & Kitipan Sukam", "Humidity Monitoring"),
    ("Kunakorn Keawkar", "Power Monitoring"),
    ("Peerapat Inchai", "Safety Alarm"),
    ("Thanawat Tanmoon", "System Summary + QA")
]

for name, role in member_data:
    st.write(f"- **{name}**: {role}")

st.markdown("---")

st.subheader("Available pages")

st.write("Use the left sidebar to open:")
st.write("- Temperature Monitoring")
st.write("- Humidity Monitoring")
st.write("- Power Monitoring")
st.write("- Safety Alarm")
st.write("- System Summary")

st.markdown("---")

st.caption("This dashboard follows the course requirement for separate logic, UI pages, tests, and Git workflow review.")
