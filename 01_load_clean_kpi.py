import pandas as pd
import numpy as np

# 1. Load: order-level data (e.g., Olist / DataCo public datasets)
orders = pd.read_csv("orders.csv", parse_dates=["order_date", "promised_date", "delivered_date"])

# 2. Clean
orders = orders.drop_duplicates(subset="order_id")
orders = orders.dropna(subset=["order_date", "sku", "dest_lat", "dest_lon"])
orders["quantity"] = orders["quantity"].clip(lower=0)

# 3. Feature engineering
orders["lead_time_days"] = (orders["delivered_date"] - orders["order_date"]).dt.days
orders["on_time"] = (orders["delivered_date"] <= orders["promised_date"]).astype(int)
orders["dow"] = orders["order_date"].dt.dayofweek
orders["month"] = orders["order_date"].dt.month

# KPI 1: On-time delivery rate
otd = orders.loc[orders["delivered_date"].notna(), "on_time"].mean()
print(f"On-time delivery rate: {otd:.1%}")
