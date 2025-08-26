
import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="Crypto Signal Agent", layout="wide")
st.title("📈 Real-Time Crypto Signal Agent")

def generate_signals():
    pairs = ["BTC/USDT", "ETH/USDT", "SOL/USDT", "XRP/USDT"]
    directions = ["LONG", "SHORT"]
    data = []
    for pair in pairs:
        signal = {
            "Пара": pair,
            "Направление": random.choice(directions),
            "Вероятность": f"{random.uniform(80, 95):.2f}%",
            "Мин. вход": f"{random.randint(50, 200)} USDT",
            "Макс. вход": f"{random.randint(500, 2000)} USDT",
            "Обновлено": datetime.utcnow().strftime("%H:%M:%S")
        }
        data.append(signal)
    return pd.DataFrame(data)

st.caption("Обновляется каждые 10 секунд (эмуляция)")
placeholder = st.empty()

# Обновление таблицы каждые 10 секунд (на Render перезапуск через F5)
df = generate_signals()
with placeholder.container():
    st.dataframe(df, use_container_width=True)
