import streamlit as st
from services.temperature import classify_temperature


# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Temperature Monitoring",
    page_icon="🌡️",
    layout="centered"
)


# -----------------------------
# Minimal style
# -----------------------------
st.markdown("""
<style>

.stApp {
    background-color: #faf9f6;
    color: #374151;
}

.block-container {
    max-width: 650px;
    padding-top: 3rem;
}

/* Title */
h1 {
    text-align: center;
    color: #374151;
    font-size: 32px !important;
    font-weight: 650 !important;
    letter-spacing: -1px;
    margin-bottom: 4px;
}

.subtitle {
    text-align: center;
    color: #9ca3af;
    font-size: 14px;
    margin-bottom: 30px;
}

/* Temperature card */
.temp-card {
    background: #ffffff;
    border: 1px solid #eeeae4;
    border-radius: 20px;
    padding: 28px;
    text-align: center;
    margin-bottom: 20px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
}

.temp-label {
    font-size: 12px;
    color: #9ca3af;
    letter-spacing: 0.8px;
    margin-bottom: 8px;
}

.temp-value {
    font-size: 52px;
    font-weight: 650;
    color: #374151;
    letter-spacing: -2px;
}

/* Metric */
div[data-testid="stMetric"] {
    background: transparent;
    border: none;
    padding: 0;
}

div[data-testid="stMetricLabel"] {
    color: #9ca3af;
}

div[data-testid="stMetricValue"] {
    color: #374151;
}

/* Slider */
div[data-baseweb="slider"] {
    margin-top: 12px;
    margin-bottom: 8px;
}

/* Status */
.status-title {
    font-size: 12px;
    color: #9ca3af;
    margin-bottom: 8px;
    letter-spacing: 0.8px;
}

/* Alerts */
div[data-testid="stAlert"] {
    border-radius: 14px;
    border: none;
}

/* Footer */
.footer {
    text-align: center;
    color: #c4c1bb;
    font-size: 11px;
    margin-top: 35px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------
st.markdown("""
<h1>🌡️ Temperature</h1>
<div class="subtitle">
    Simple temperature monitoring
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Temperature card
# -----------------------------
st.markdown("""
<div class="temp-card">
    <div class="temp-label">CURRENT TEMPERATURE</div>
""", unsafe_allow_html=True)


temp = st.slider(
    "Temperature (°C)",
    min_value=-20.0,
    max_value=80.0,
    value=28.0,
    step=0.5
)

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# Classification
# -----------------------------
status = classify_temperature(temp)


# -----------------------------
# Current value
# -----------------------------
st.metric(
    "Current temperature",
    f"{temp:.1f} °C"
)


# -----------------------------
# Status
# -----------------------------
st.markdown(
    '<div class="status-title">CURRENT STATUS</div>',
    unsafe_allow_html=True
)

if status == "NORMAL":
    st.success("🌱 Normal")

elif status == "WARNING":
    st.warning("☀️ Warning")

else:
    st.error("🔥 Critical")


# -----------------------------
# Footer
# -----------------------------
st.markdown("""
<div class="footer">
    Temperature Monitoring · TEMP-01
</div>
""", unsafe_allow_html=True)