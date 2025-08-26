import streamlit as st
from utils.signal_engine import generate_signals

st.set_page_config(page_title="Crypto Signal Agent", layout="wide")
st.title("📈 Crypto Signal Agent")
st.caption("Прогноз импульса в ближайшие 15 минут")

data = generate_signals()

st.dataframe(data, use_container_width=True)