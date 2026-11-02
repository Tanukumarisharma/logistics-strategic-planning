from scipy.stats import norm
import numpy as np

def reorder_policy(daily_demand, lead_time_days, service_level=0.95):
    mu, sigma = daily_demand.mean(), daily_demand.std()
    z = norm.ppf(service_level)
    safety_stock = z * sigma * np.sqrt(lead_time_days)
    reorder_point = mu * lead_time_days + safety_stock
    return round(safety_stock), round(reorder_point)

ss, rop = reorder_policy(sku_df["quantity"], lead_time_days=5)
print(f"Safety stock: {ss} units | Reorder point: {rop} units")

def eoq(annual_demand, order_cost, holding_cost):
    return np.sqrt(2 * annual_demand * order_cost / holding_cost)
