import matplotlib.pyplot as plt

daily = (orders.set_index("order_date")
               .groupby("sku")["quantity"]
               .resample("D").sum()
               .reset_index())

# Demand trend and seasonality for the top-10 SKUs
top = daily.groupby("sku")["quantity"].sum().nlargest(10).index
for sku in top[:3]:
    s = daily[daily.sku == sku].set_index("order_date")["quantity"]
    s.rolling(7).mean().plot(label=str(sku))
plt.title("7-day rolling demand, top SKUs"); plt.legend(); plt.show()

# Delay analysis by region and weekday
print(orders.groupby("region")["on_time"].mean().sort_values())
print(orders.groupby("dow")["lead_time_days"].describe())
print(orders[["quantity", "distance_km", "lead_time_days"]].corr())
