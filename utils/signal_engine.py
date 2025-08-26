import pandas as pd
import random

def generate_signals():
    # Эмуляция: список торговых пар
    symbols = ["BTC/USDT", "ETH/USDT", "SOL/USDT", "XRP/USDT", "DOGE/USDT"]
    signals = []

    for symbol in symbols:
        will_trigger = random.choice([True, False, False])
        if will_trigger:
            direction = random.choice(["LONG", "SHORT"])
            probability = random.randint(80, 98)
            minutes_left = random.randint(1, 15)
            comment = random.choice(["RSI пересечение", "EMA сигнал", "MACD дивергенция"])
            percent_target = round(random.uniform(1.0, 3.5), 2)

            signals.append({
                "Пара": symbol,
                "Направление": direction,
                "Вероятность": f"{probability}%",
                "Осталось": f"{minutes_left} мин",
                "Цель": f"{percent_target}%", 
                "Комментарий": comment
            })

    df = pd.DataFrame(signals)
    df = df[df["Цель"].str.replace('%', '').astype(float) >= 1.0]
    return df.sort_values("Вероятность", ascending=False).reset_index(drop=True)