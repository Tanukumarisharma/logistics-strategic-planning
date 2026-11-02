from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Cluster delivery zones by location and demand density
zones = orders.groupby("postcode").agg(
    lat=("dest_lat", "mean"), lon=("dest_lon", "mean"),
    orders=("order_id", "count"), avg_qty=("quantity", "mean")).reset_index()

X = StandardScaler().fit_transform(zones[["lat", "lon", "orders", "avg_qty"]])

best_k, best_score = None, -1
for k in range(2, 9):
    labels = KMeans(n_clusters=k, n_init=10, random_state=42).fit_predict(X)
    score = silhouette_score(X, labels)
    if score > best_score:
        best_k, best_score = k, score

zones["cluster"] = KMeans(n_clusters=best_k, n_init=10, random_state=42).fit_predict(X)
print("Chosen k:", best_k, "silhouette:", round(best_score, 3))
