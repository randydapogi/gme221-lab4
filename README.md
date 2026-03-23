# GmE 221 – Laboratory Exercise 4

## Overview

---

## Environment Setup

- Python 3.x
- PostgreSQL with PostGIS
- geopandas libpysal esda matplotlib numpy sqlalchemy psycopg2-binary

## How to Run

1. Activate the virtual environment
2. Run `python analysis.py`

---

## Outputs

---

## Reflection

### Interpreting the Neighborhood Structure

1. How does the spatial weights graph represent neighborhood relationships? Explain how parcel centroids and connecting lines correspond to nodes and edges in a spatial network.
   - The spatial weights graph show the geographic adjacency of parcels with each other. The centroids represent the parcels in the form of points and the connecting lines represent the neighbors of the parcels based on the weigth used for the neighborhood generation.

2. How does the structure of the neighbor graph change?
   - Using the contiguity weights the centroids of the parcels were connected to parcels with shared edge. Using the K-nearest neighbors the parcel centroids where connected to the k nearest centroids as defined in the function. Using the distance-based weights the parcel centroids were connected to centroids which are within the threshold distance set in the function.

3. What changes do you observe in the connectivity of the spatial graph?
   - Increasing the k in KNN increased the number of connections between centroinds to k, for example, for k = 10 each centroid has 10 centroid conected to it. Increasing the distance threshold in the distance-based weights increased the connections of centroids with parcel centroids that have centroids near it having more connections compared to centroids with not so many centroids near it. This is because the condition for to centroids having a connection is the defined threshold set in the distance-based weights function.

4. Does increasing K or distance create a denser spatial network? Explain how this might affect the strength of spatial autocorrelation.
   - Increasing the K or distance threshold created a denser spatial network. Increasing k or distance threshold affects the strength of spatial autocorrelation. Having the right amount of k or distance threshold can highlight areas of local correlation however increasing the k or distance threshold too much can hide the local correlation of centroids.

5. Which spatial weights method do you think best represents the spatial relationships of parcels in your dataset? Justify your answer conceptually.
   - Since the parcels are representation of land and this land has borders and connections or paths between them, the contiguity spatial relationship best represents the parcel dataset. Contiguity spatial relationships can help use understand the relationship of the parcels in terms of their connectivity to adjacent parcels.

6. Why is it important to visualize spatial weights before computing Moran’s I? What potential analytical mistakes could occur if the neighborhood structure is incorrect?
   - Visualizing the spatial weights before computing Moran's I can help us see if we are using the right neighborhood structure for calculating the Moran's I. Having incorrect neighborhood structure can drastically change the result of Moran's I or the result the correlation between points. The result of Moran's I is only as good as the defined neigborhood structure used in the calculation.

---
