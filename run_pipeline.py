"""Runs steps 1-5 in order (they share variables). Step 6 needs ortools and a distance matrix."""
import matplotlib
matplotlib.use("Agg")  # no pop-up windows; remove this line to see plots
for f in ["01_load_clean_kpi", "02_eda", "03_demand_forecast", "04_inventory_policy", "05_zone_clustering"]:
    print(f"\n=== {f} ===")
    exec(open(f"{f}.py").read())
