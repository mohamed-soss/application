import streamlit as st
import base64

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Sheets Hub",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# SET BACKGROUND IMAGE WITH PARALLAX + FADE ANIMATION
# ----------------------------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    page_bg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-attachment: fixed; /* makes it move with scroll */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        animation: fadeCycle 15s infinite alternate ease-in-out;
    }}

    /* Animation for fade in/out brightness */
    @keyframes fadeCycle {{
        0% {{ filter: brightness(0.6) blur(2px); }}
        50% {{ filter: brightness(1.2) blur(0px); }}
        100% {{ filter: brightness(0.8) blur(1px); }}
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# Call function (set background)
set_bg("download.png")

# ----------------------------
# APP HEADER
# ----------------------------
st.markdown(
    """
    <style>
        .main-title {
            font-size: 42px;
            font-weight: 800;
            text-align: center;
            color: #ffffff;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
        }
        .subtitle {
            font-size: 20px;
            text-align: center;
            color: #f1f1f1;
            margin-bottom: 30px;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
        }
        .card {
            background-color: rgba(255,255,255,0.85);
            border-radius: 16px;
            padding: 20px;
            margin: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.25);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 18px rgba(0,0,0,0.35);
        }
        .card a {
            text-decoration: none;
            font-size: 20px;
            font-weight: 600;
            color: #2980b9;
        }
        .card a:hover {
            color: #1f618d;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">📊 Sheets Hub</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Click a sheet below to open it in a new tab</div>', unsafe_allow_html=True)

# ----------------------------
# SHEET LINKS
# ----------------------------
sheets = {
    "📈 Sales Report": "https://docs.google.com/spreadsheets/d/XXXX",
    "👥 Employee Data": "https://docs.google.com/spreadsheets/d/YYYY",
    "📣 Marketing Plan": "https://docs.google.com/spreadsheets/d/ZZZZ",
    "💰 Budget Tracker": "https://docs.google.com/spreadsheets/d/AAAA",
    "📦 Inventory Sheet": "https://docs.google.com/spreadsheets/d/BBBB",
    "🗓️ Project Timeline": "https://docs.google.com/spreadsheets/d/CCCC",
}

# ----------------------------
# DISPLAY CARDS
# ----------------------------
cols = st.columns(2)

i = 0
for name, url in sheets.items():
    with cols[i % 2]:
        st.markdown(
            f"""
            <div class="card">
                <a href="{url}" target="_blank">{name}</a>
            </div>
            """,
            unsafe_allow_html=True
        )
    i += 1

