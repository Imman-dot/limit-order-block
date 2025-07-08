import numpy as np
import csv
from pathlib import Path

# === CONFIGURATION ===
OUT = Path("data") / "synthetic_events.csv"
OUT.parent.mkdir(exist_ok=True)

# === GENERATE PRICES ===
np.random.seed(42)
# 1000-step random walk with higher volatility
prices = 100 + np.cumsum(np.random.normal(0, 2.0, size=1000))

# === WRITE EVENTS ===
with open(OUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["price", "qty", "side"])
    for p in prices:
        # random side each event
        side = "buy" if np.random.rand() < 0.5 else "sell"
        # random quantity
        qty = np.random.choice([0.5, 1.0, 2.0])
        writer.writerow([f"{p:.2f}", qty, side])

print(f"Generated {len(prices)} synthetic events to {OUT}")


        