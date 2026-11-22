
import os
import joblib
import requests
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from streamlit_autorefresh import st_autorefresh


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AIoT Smart Fruits Guard",
    page_icon="🍎",
    layout="wide",
    initial_sidebar_state="expanded"
)

st_autorefresh(
    interval=20000,
    key="refresh"
)


# =========================================================
# DARK DASHBOARD STYLE
# =========================================================

st.markdown("""
<style>

/* =====================================================
   GLOBAL
===================================================== */

.stApp {
    background: #050b16;
    color: #ffffff;
}

.block-container {
    max-width: 1500px;
    padding-top: 1.5rem;
    padding-left: 2rem;
    padding-right: 2rem;
}


/* =====================================================
   SIDEBAR
===================================================== */

section[data-testid="stSidebar"] {
    background: #081225;
    border-right: 1px solid #263653;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span {
    color: #ffffff !important;
}

section[data-testid="stSidebar"] small {
    color: #b8c7df !important;
}

section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color: #b8c7df !important;
}


/* =====================================================
   TITLES
===================================================== */

h1, h2, h3, h4, h5, h6 {
    color: #ffffff !important;
}

p {
    color: #ffffff;
}


/* =====================================================
   CAPTIONS
===================================================== */

[data-testid="stCaptionContainer"] {
    color: #b8c7df !important;
}

[data-testid="stCaptionContainer"] p {
    color: #b8c7df !important;
}


/* =====================================================
   METRIC CARDS
===================================================== */

div[data-testid="stMetric"] {
    background: #0d172a;
    border: 1px solid #263653;
    border-radius: 15px;
    padding: 18px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.30);
}

div[data-testid="stMetricLabel"] {
    color: #dce7f7 !important;
}

div[data-testid="stMetricLabel"] p {
    color: #dce7f7 !important;
}

div[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-weight: 800;
}

div[data-testid="stMetricValue"] div {
    color: #ffffff !important;
}


/* =====================================================
   ALERTS / SUCCESS / ERROR
   IMPORTANT: DARK TEXT ON LIGHT ALERT BACKGROUND
===================================================== */

div[data-testid="stAlert"] {
    border-radius: 14px;
}

/* Main alert text */
div[data-testid="stAlert"] p {
    color: #172033 !important;
    font-weight: 600 !important;
}

/* Alert spans */
div[data-testid="stAlert"] span {
    color: #172033 !important;
}

/* Alert internal text */
div[data-testid="stAlert"] div {
    color: #172033 !important;
}

/* Success alert */
div[data-testid="stAlert"][kind="success"] p {
    color: #123d28 !important;
}

/* Error alert */
div[data-testid="stAlert"][kind="error"] p {
    color: #5a1118 !important;
}


/* =====================================================
   SELECTBOX
===================================================== */

div[data-baseweb="select"] {
    color: #ffffff !important;
}

div[data-baseweb="select"] > div {
    background: #0d172a !important;
    border: 1px solid #3a4c6c !important;
    color: #ffffff !important;
}

div[data-baseweb="select"] span {
    color: #ffffff !important;
}


/* =====================================================
   TEXT INPUT
===================================================== */

div[data-testid="stTextInput"] label {
    color: #ffffff !important;
}

div[data-testid="stTextInput"] input {
    color: #ffffff !important;
    background: #0d172a !important;
    border: 1px solid #3a4c6c !important;
}


/* =====================================================
   BUTTONS
===================================================== */

.stButton > button {
    width: 100%;
    border-radius: 10px;
    border: 1px solid #263653;
    background: #0d172a;
    color: #ffffff !important;
}

.stButton > button p {
    color: #ffffff !important;
}

.stButton > button:hover {
    border-color: #35e58b;
    color: #ffffff !important;
}


/* =====================================================
   DATAFRAME
===================================================== */

div[data-testid="stDataFrame"] {
    border: 1px solid #263653;
    border-radius: 12px;
}


/* =====================================================
   EXPANDER
===================================================== */

div[data-testid="stExpander"] {
    background: #0b1426;
    border: 1px solid #263653;
    border-radius: 12px;
}

div[data-testid="stExpander"] p {
    color: #ffffff !important;
}

div[data-testid="stExpander"] span {
    color: #ffffff !important;
}


/* =====================================================
   DIVIDERS
===================================================== */

hr {
    border-color: #263653 !important;
}


/* =====================================================
   PLOTLY
===================================================== */

div[data-testid="stPlotlyChart"] {
    border-radius: 14px;
    overflow: hidden;
}


/* =====================================================
   HIDE STREAMLIT MENU
===================================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🍎 AIoT")

    st.markdown(
        "### Smart Fruits Guard"
    )

    st.caption(
        "Intelligent fruit storage monitoring"
    )

    st.divider()

    st.markdown("### 🍊 Fruit")

    fruit = st.selectbox(
        "Select fruit",
        [
            "Banana",
            "Orange",
            "Pineapple",
            "Tomato"
        ],
        label_visibility="collapsed"
    )

    st.markdown("### 🔑 ThingSpeak")

    read_api_key = st.text_input(
        "Read API Key",
        type="password"
    )

    st.caption(
        "Channel ID: 3555996"
    )

    st.divider()

    st.markdown("### 📊 Navigation")

    st.button(
        "🏠 Dashboard",
        use_container_width=True
    )

    st.button(
        "📈 Analytics",
        use_container_width=True
    )

    st.button(
        "🔔 Alerts",
        use_container_width=True
    )

    st.button(
        "⚙️ Settings",
        use_container_width=True
    )

    st.button(
        "ℹ️ About",
        use_container_width=True
    )

    st.divider()

    st.success(
        "🤖 Logistic Regression loaded"
    )


# =========================================================
# HEADER
# =========================================================

title_col, live_col = st.columns([4, 1])

with title_col:

    st.title(
        "🍎 Fruit Storage Monitoring"
    )

    st.caption(
        "Real-time monitoring using AI & IoT"
    )

with live_col:

    st.success(
        "● Live Data"
    )

st.divider()


# =========================================================
# MODEL PATH
# =========================================================

MODEL_PATH = (
    "/content/fruit_cold_storage_lr/"
    "logistic_regression_model/"
    "fruit_storage_logistic_regression.joblib"
)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():

    if not os.path.exists(
        MODEL_PATH
    ):

        raise FileNotFoundError(
            f"Model not found: {MODEL_PATH}"
        )

    return joblib.load(
        MODEL_PATH
    )


try:

    model = load_model()

except Exception as e:

    st.error(
        f"Model loading error: {e}"
    )

    st.stop()


# =========================================================
# THINGSPEAK
# =========================================================

@st.cache_data(ttl=10)
def get_thingspeak_data(
    channel_id,
    api_key
):

    url = (
        f"https://api.thingspeak.com/channels/"
        f"{channel_id}/feeds.json"
    )

    response = requests.get(
        url,
        params={
            "api_key": api_key,
            "results": 100
        },
        timeout=15
    )

    response.raise_for_status()

    feeds = response.json().get(
        "feeds",
        []
    )

    if not feeds:

        raise ValueError(
            "No readings found in ThingSpeak."
        )

    data = pd.DataFrame(
        feeds
    )

    # -----------------------------------------------------
    # FIELD 1 = TEMPERATURE
    # FIELD 2 = HUMIDITY
    # -----------------------------------------------------

    data["Temp"] = pd.to_numeric(
        data["field1"],
        errors="coerce"
    )

    data["Humid"] = pd.to_numeric(
        data["field2"],
        errors="coerce"
    )

    data["created_at"] = pd.to_datetime(
        data["created_at"],
        errors="coerce"
    )

    # -----------------------------------------------------
    # TEMPORARY MODEL INPUTS
    #
    # The trained model expects:
    # Fruit, Temp, Humid, Light, CO2
    #
    # Current ThingSpeak channel only provides
    # Temperature and Humidity.
    # -----------------------------------------------------

    data["Light"] = 5.0

    data["CO2"] = 200.0

    data = data.dropna(
        subset=[
            "Temp",
            "Humid",
            "created_at"
        ]
    )

    data = data.sort_values(
        "created_at"
    ).reset_index(
        drop=True
    )

    return data


# =========================================================
# API KEY CHECK
# =========================================================

if not read_api_key:

    st.warning(
        "👈 Enter your ThingSpeak Read API Key in the sidebar."
    )

    st.stop()


# =========================================================
# GET DATA
# =========================================================

try:

    df = get_thingspeak_data(
        "3555996",
        read_api_key
    )

except Exception as e:

    st.error(
        f"ThingSpeak connection error: {e}"
    )

    st.stop()


if df.empty:

    st.warning(
        "No valid sensor readings available."
    )

    st.stop()


# =========================================================
# CURRENT SENSOR VALUES
# =========================================================

latest = df.iloc[-1]

temperature = float(
    latest["Temp"]
)

humidity = float(
    latest["Humid"]
)

light = 5.0

co2 = 200.0


# =========================================================
# MODEL INPUT
# =========================================================

model_input = pd.DataFrame([
    {
        "Fruit": fruit,
        "Temp": temperature,
        "Humid": humidity,
        "Light": light,
        "CO2": co2
    }
])


# =========================================================
# LOGISTIC REGRESSION PREDICTION
# =========================================================

try:

    prediction = model.predict(
        model_input
    )[0]

    if hasattr(
        model,
        "predict_proba"
    ):

        probabilities = model.predict_proba(
            model_input
        )[0]

        confidence = (
            float(
                max(probabilities)
            )
            * 100
        )

    else:

        confidence = None

except Exception as e:

    st.error(
        f"Prediction error: {e}"
    )

    st.stop()


# =========================================================
# NORMALIZE PREDICTION
# =========================================================

prediction_text = (
    str(prediction)
    .strip()
    .lower()
)

if prediction_text == "good":

    ai_status = "GOOD"

else:

    ai_status = "BAD"


# =========================================================
# TOP STORAGE STATUS
# =========================================================

if ai_status == "GOOD":

    st.success(
        "🟢 STORAGE STATUS: GOOD"
    )

else:

    st.error(
        "🔴 STORAGE STATUS: ABNORMAL"
    )


# =========================================================
# LIVE SENSOR MONITORING
# =========================================================

st.subheader(
    "📡 Live Sensor Monitoring"
)

c1, c2, c3, c4 = st.columns(4)


# Temperature

with c1:

    st.metric(
        "🌡️ Temperature",
        f"{temperature:.1f} °C"
    )


# Humidity

with c2:

    st.metric(
        "💧 Humidity",
        f"{humidity:.1f} %"
    )


# Light

with c3:

    st.metric(
        "💡 Light",
        f"{light:.0f}"
    )


# CO2

with c4:

    st.metric(
        "🫧 CO₂ / Gas",
        f"{co2:.0f}"
    )


st.divider()


# =========================================================
# AI PREDICTION RESULT
# =========================================================

st.subheader(
    "🤖 AI Prediction Result"
)

p1, p2 = st.columns(
    [1.6, 1]
)


# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------

with p1:

    if ai_status == "GOOD":

        st.success(
            "🟢 GOOD\n\n"
            "The trained Logistic Regression model "
            "predicts a good storage condition."
        )

    else:

        st.error(
            "🔴 BAD\n\n"
            "The trained Logistic Regression model "
            "detected an abnormal storage condition."
        )


# ---------------------------------------------------------
# CONFIDENCE
# ---------------------------------------------------------

with p2:

    if confidence is not None:

        st.metric(
            "Model Confidence",
            f"{confidence:.2f}%"
        )

    else:

        st.info(
            "Probability unavailable."
        )

    st.caption(
        f"Current fruit: {fruit}"
    )


# =========================================================
# SENSOR TRENDS
# =========================================================

st.subheader(
    "📈 Sensor Trends"
)

g1, g2 = st.columns(2)


# =========================================================
# TEMPERATURE GRAPH
# =========================================================

with g1:

    fig_temp = go.Figure()

    fig_temp.add_trace(
        go.Scatter(
            x=df["created_at"],
            y=df["Temp"],
            mode="lines+markers",
            name="Temperature",
            line=dict(
                color="#ff4f5e",
                width=3
            ),
            marker=dict(
                size=5
            )
        )
    )

    fig_temp.update_layout(
        title="Temperature History",
        height=350,
        template="plotly_dark",
        paper_bgcolor="#0b1426",
        plot_bgcolor="#0b1426",
        font=dict(
            color="#ffffff"
        ),
        title_font=dict(
            color="#ffffff"
        ),
        xaxis=dict(
            gridcolor="#1d2c49",
            color="#ffffff"
        ),
        yaxis=dict(
            gridcolor="#1d2c49",
            color="#ffffff"
        )
    )

    st.plotly_chart(
        fig_temp,
        use_container_width=True
    )


# =========================================================
# HUMIDITY GRAPH
# =========================================================

with g2:

    fig_humid = go.Figure()

    fig_humid.add_trace(
        go.Scatter(
            x=df["created_at"],
            y=df["Humid"],
            mode="lines+markers",
            name="Humidity",
            line=dict(
                color="#28a9ff",
                width=3
            ),
            marker=dict(
                size=5
            )
        )
    )

    fig_humid.update_layout(
        title="Humidity History",
        height=350,
        template="plotly_dark",
        paper_bgcolor="#0b1426",
        plot_bgcolor="#0b1426",
        font=dict(
            color="#ffffff"
        ),
        title_font=dict(
            color="#ffffff"
        ),
        xaxis=dict(
            gridcolor="#1d2c49",
            color="#ffffff"
        ),
        yaxis=dict(
            gridcolor="#1d2c49",
            color="#ffffff"
        )
    )

    st.plotly_chart(
        fig_humid,
        use_container_width=True
    )


# =========================================================
# THINGSPEAK DATA
# =========================================================

st.subheader(
    "📡 Data from ThingSpeak"
)

display_df = df[
    [
        "created_at",
        "Temp",
        "Humid"
    ]
].tail(10).copy()

display_df.columns = [
    "Time",
    "Temperature (°C)",
    "Humidity (%)"
]

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# ALERTS & NOTIFICATIONS
# =========================================================

st.subheader(
    "🔔 Alerts & Notifications"
)

if ai_status == "GOOD":

    st.success(
        "🟢 All AI monitoring conditions are currently normal."
    )

else:

    st.error(
        "🔴 AI Alert: Logistic Regression detected "
        "an abnormal condition."
    )


# =========================================================
# DATA SENT TO MODEL
# =========================================================

with st.expander(
    "🔎 Show data sent to the AI model"
):

    st.dataframe(
        model_input,
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "Light and CO₂ currently use fixed values because "
        "the ThingSpeak channel provides Temperature and "
        "Humidity only."
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🍎 AIoT Smart Fruits Guard • "
    "ThingSpeak Live Monitoring • "
    "Logistic Regression AI"
)

st.caption(
    "Dashboard refreshes automatically every 20 seconds."
)
