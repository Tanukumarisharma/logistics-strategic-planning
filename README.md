# Strategic Planning and Data Exploration in Logistics

Week 1 task: a strategic plan and Python illustrations for a data-driven logistics project.

**Scenario:** SwiftCart Logistics (fictional regional e-commerce distributor) with two problems: inventory imbalance and costly, late deliveries.

**KPIs:** on-time delivery rate, cost per delivery, distance per route, stockout rate, inventory turnover, forecast accuracy.

## Contents
- `docs/Logistics_Strategic_Planning_Report.docx` – full report (scenario, KPIs, research, roadmap, conclusion)
- `src/01_load_clean_kpi.py` – loading, cleaning, feature engineering, on-time delivery KPI
- `src/02_eda.py` – exploratory analysis of demand and delays
- `src/03_demand_forecast.py` – linear regression vs gradient boosting forecast
- `src/04_inventory_policy.py` – safety stock, reorder point, EOQ
- `src/05_zone_clustering.py` – K-Means delivery zones with silhouette score
- `src/06_route_optimization_ortools.py` – capacitated VRP with Google OR-Tools
- `src/generate_sample_data.py` – synthetic data for testing

## How to run
```bash
pip install -r requirements.txt
cd src
python generate_sample_data.py
python run_pipeline.py
```

## Data
Sample data is synthetic, so outputs are not real findings. For real analysis use public datasets such as Olist Brazilian E-Commerce, DataCo Smart Supply Chain or M5 Forecasting (all on Kaggle), and adjust column names to match.

## Status
Planning phase (Week 1). Scripts 1-5 were tested on synthetic data; script 6 follows the standard OR-Tools routing pattern and needs `pip install ortools` and a distance matrix.
