"""Creates a synthetic orders.csv so the scripts can be tested without a real dataset.
Values are random and NOT meaningful results. Replace with Olist / DataCo data for real analysis."""
import pandas as pd, numpy as np
rng = np.random.default_rng(0)
n = 20000
od = pd.Timestamp("2024-01-01") + pd.to_timedelta(rng.integers(0, 540, n), unit="D")
df = pd.DataFrame({"order_id": range(n), "order_date": od, "sku": rng.integers(1, 30, n),
    "dest_lat": rng.normal(40, .5, n), "dest_lon": rng.normal(-74, .5, n),
    "quantity": rng.poisson(3, n), "region": rng.choice(list("ABCD"), n),
    "postcode": rng.integers(1000, 1300, n), "distance_km": rng.uniform(1, 80, n)})
df["promised_date"] = df.order_date + pd.to_timedelta(4, unit="D")
df["delivered_date"] = df.order_date + pd.to_timedelta(rng.integers(1, 8, n), unit="D")
df.to_csv("orders.csv", index=False)
print("orders.csv created")
