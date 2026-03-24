from libpysal.weights import Rook, KNN, DistanceBand 


def contiguity_weights(gdf): 
    return Rook.from_dataframe(gdf, use_index=True)

def knn_weights(gdf, k=4): 
    # coords = [(geom.centroid.x, geom.centroid.y) for geom in gdf.geometry] 
    # return KNN(coords, k=k) 
    return KNN.from_dataframe(gdf, k=k, use_index=True, silence_warnings=True)

def distance_weights(gdf, threshold=20): 
    # coords = [(geom.centroid.x, geom.centroid.y) for geom in gdf.geometry] 
    # return DistanceBand(coords, threshold=threshold)
    return DistanceBand.from_dataframe(gdf, threshold=threshold, use_index=True, silence_warnings=True)