from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np

def make_features(df):
    df = df.sort_values("order_date").copy()
    df["lag_7"] = df["quantity"].shift(7)
    df["lag_14"] = df["quantity"].shift(14)
    df["roll_28"] = df["quantity"].shift(1).rolling(28).mean()
    df["dow"] = df["order_date"].dt.dayofweek
    df["month"] = df["order_date"].dt.month
    return df.dropna()

sku_df = make_features(daily[daily.sku == top[0]])
features = ["lag_7", "lag_14", "roll_28", "dow", "month"]

# Time-ordered split (no shuffling, to avoid leakage)
cut = int(len(sku_df) * 0.8)
train, test = sku_df.iloc[:cut], sku_df.iloc[cut:]

baseline = LinearRegression().fit(train[features], train["quantity"])
gbr = GradientBoostingRegressor(random_state=42).fit(train[features], train["quantity"])

for name, m in [("Linear", baseline), ("GBR", gbr)]:
    pred = m.predict(test[features])
    mape = np.mean(np.abs((test["quantity"] - pred) / test["quantity"].clip(lower=1)))
    print(name, "MAE:", round(mean_absolute_error(test["quantity"], pred), 2),
          "MAPE:", f"{mape:.1%}")
