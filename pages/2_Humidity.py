import streamlit as st
from services.humidity import classify_humidity

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Humidity Monitoring",
    page_icon="💧",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

    /* Background */
    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(0, 200, 255, 0.12), transparent 30%),
            radial-gradient(circle at 90% 90%, rgba(120, 50, 255, 0.12), transparent 30%),
            #070b14;
        color: white;
    }

    /* Main title */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0px;
        background: linear-gradient(90deg, #00eaff, #7c4dff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        color: #8c9aaa;
        font-size: 16px;
        margin-bottom: 35px;
    }

    /* Cards */
    .card {
        background: rgba(18, 25, 40, 0.75);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 28px;
        box-shadow: 0 10px 35px rgba(0,0,0,0.35);
        backdrop-filter: blur(15px);
    }

    .card-title {
        color: #8c9aaa;
        font-size: 15px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .humidity-value {
        font-size: 64px;
        font-weight: 800;
        margin-top: 8px;
        color: #00eaff;
    }

    .status {
        font-size: 28px;
        font-weight: 700;
        margin-top: 8px;
    }

    .normal {
        color: #00ff9d;
    }

    .warning {
        color: #ffd43b;
    }

    .critical {
        color: #ff4d6d;
    }

    .error {
        color: #ff4d6d;
        font-size: 30px;
        font-weight: 800;
    }

    /* Info box */
    .info-box {
        background: rgba(0, 234, 255, 0.05);
        border: 1px solid rgba(0, 234, 255, 0.15);
        border-radius: 15px;
        padding: 18px;
        margin-top: 20px;
    }

    .range {
        color: #aeb8c5;
        font-size: 14px;
        margin-top: 6px;
    }

    /* Slider */
    div[data-baseweb="slider"] {
        padding-top: 15px;
    }

</style>
""", unsafe_allow_html=True)


# =========================
# HEADER
# =========================
st.markdown(
    '<div class="main-title">💧 HUMIDITY MONITORING</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Real-time environmental humidity analysis system</div>',
    unsafe_allow_html=True
)


# =========================
# SLIDER
# =========================
st.markdown(
    '<div class="card-title">Humidity Input</div>',
    unsafe_allow_html=True
)

humidity = st.slider(
    "Humidity (%)",
    min_value=-100.0,
    max_value=200.0,
    value=50.0,
    step=1.0
)


# =========================
# CLASSIFY
# =========================
try:
    status = classify_humidity(humidity)

    if status == "NORMAL":
        status_class = "normal"
        icon = "●"
        description = "Humidity level is within the normal range."

    elif status == "WARNING":
        status_class = "warning"
        icon = "▲"
        description = "Humidity level requires attention."

    else:
        status_class = "critical"
        icon = "◆"
        description = "Humidity level is outside the recommended range."


    # =========================
    # DASHBOARD CARDS
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">Current Humidity</div>
            <div class="humidity-value">{humidity:.0f}%</div>
            <div class="range">Sensor reading</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">System Status</div>
            <div class="status {status_class}">
                {icon} {status}
            </div>
            <div class="range">{description}</div>
        </div>
        """, unsafe_allow_html=True)


    # =========================
    # STATUS INFORMATION
    # =========================
    st.markdown("""
    <div class="info-box">
        <b>Humidity Classification</b>
        <div class="range">
            40–60% → NORMAL &nbsp;&nbsp;|&nbsp;&nbsp;
            30–39% / 61–70% → WARNING &nbsp;&nbsp;|&nbsp;&nbsp;
            <30% / >70% → CRITICAL
        </div>
    </div>
    """, unsafe_allow_html=True)


except ValueError:
    st.markdown("""
    <div class="card">
        <div class="error">
            ⚠ VALUE ERROR
        </div>
        <div class="range">
            Humidity must be between 0% and 100%.
        </div>
    </div>
    """, unsafe_allow_html=True)