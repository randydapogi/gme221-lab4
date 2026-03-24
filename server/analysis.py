import geopandas as gpd 
from sqlalchemy import create_engine 
from spatial_weights import contiguity_weights, knn_weights, distance_weights 
from visualization import visualize_neighbors
from moran import calculate_global_morans_I 

host = "localhost" 
port = "5432" 
dbname = "gme221_exer4"
user = "postgres" 
password = "admin" 

conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}" 

engine = create_engine(conn_str) 

sql_query = """ SELECT gid, ass_ass_va, ass_market, geom FROM public.assessed_parcels; """ 

gdf = gpd.read_postgis(sql_query, engine, geom_col="geom") 

# print(gdf.head()) 
# print("CRS:", gdf.crs)


w_cont = contiguity_weights(gdf) 
# visualize_neighbors(gdf, w)

w_knn = knn_weights(gdf, k=4) 
# visualize_neighbors(gdf, w)

w_dist = distance_weights(gdf, threshold=20) 
# visualize_neighbors(gdf, w)


def run_moran(gdf, w, attribute, label):
    moran_I, p_value = calculate_global_morans_I(gdf, w_cont, attribute) 
    print(f"Global Moran's I for ({label}) - [{attribute}]: {moran_I} with p-value: {p_value}")


attribute1 = "ass_ass_va" 
attribute2 = "ass_market" 

run_moran(gdf, w_cont, attribute1, label="Cont")
run_moran(gdf, w_cont, attribute2, label="Cont")
print("")

run_moran(gdf, w_knn, attribute1, label="KNN")
run_moran(gdf, w_knn, attribute2, label="KNN")
print("")

run_moran(gdf, w_dist, attribute1, label="DistThres")
run_moran(gdf, w_dist, attribute2, label="DistThres")
print("")
