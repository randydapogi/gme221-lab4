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

### Global Autocorrelation Reflection

1. What does positive Moran’s I indicate?
   - Positive Moran's I indicate positive autocorrelation. This means that parcels that are close together have similar values.
2. Why is the p-value required for interpretation?
   - P-value is a check if the autocorrelation is due to relationship of values or due to randomness. P-value of < 0.05 indicates that autocorrelation is not due to Complete Spatial Randomness (CSR)
3. What would Moran’s I near zero suggest?
   - Moran's I value near zero suggest that the parcels have no discernible autocorrelation with its neighbors.
4. What is the role of the attribute in computing Moran’s I? Why the choice of attribute (e.g., ass_ass_va vs ass_market) matters.
   - The attribute selected in computing Moran's I are the values of the points that we are checking for autocorrelation. Each attribute in the parcel dataset can have different Moran's I or different autocorrelation with its neighbors.
5. How the spatial autocorrelation result might change when a different attribute is analyzed.
   - Different attribute have different autocorrelation with each other. For our parcel example, each parcel can have different assessed value to its assessed market value therefore you can have different hotspots for autocorrelation of assessed values compared to assessed market values.
6. Why Moran’s I requires both: a spatial weights matrix, and an attribute variable.
   - For calculation Moran's I the spatial weight matrix tells it where the points are and who are the neighbors of those points, the attribute variable tells it what values are being compared / autocorrelated. Moran's I calculates the values of parcels in relation to its neighbors that is why it needs both the location data of points and the attribute data for the values being compared.

### Interpreting Local Spatial Autocorrelatio

1. What is the difference between Global Moran’s I and Local Moran’s I? Explain how each statistic describes spatial autocorrelation at different spatial scales.
   - Global Moran's I looks at the autocorrelation of parcels as a whole while Local Moran's I looks at autocorrelation of each parcel and identifies other parcels similar to it. Global Moran's I looks at the macro level while Local Moran's I looks at the micro level.

2. How are hotspots and coldspots identified using Local Moran’s I? Explain how the values of the statistic and the p-value determine whether a parcel belongs to a cluster.
   - Local Moran's I identifies hotspots and coldspots by using the value of the attribute of the parcel and comparing it to the average value of the neighbors of that parcel. High value parcel with high value neighbors corresponds to hotspots. Low value parcels with low value neighbors correspnds to lowspots. The P-value is used to determine if the relationship of parcels is statistically significant or if it is just random coincidence.

3. Where do hotspots appear in your dataset? Describe the spatial location of clusters of high values. What geographic or urban factors might explain this pattern?
   - In the dataset the hotspots appear in residential areas. The spatial clusters form in areas where there are a lot of small high value parcels close together. Being a residential area with a lot of houses, the assessment value increases and having parcels with high assessment value close together makes the area a hotspot in terms of assessment value.

4. Where do coldspots appear in your dataset? Are there areas where low values cluster together? What spatial processes might explain these patterns?
   - In the dataset coldspots appear in forrested and baresoil areas. The spatial cluster form on parcel where there is little to no development.
5. Did you observe any spatial outliers? A spatial outlier occurs when a parcel has a value very different from its neighbors. Explain how such cases appear in the dataset.
   - Parcel with gid 516 is a Hotspot parcel surrounded by Not Significant parcels. This parcel has a high ass_ass_va with its neighbors also having high ass_ass_va however its neighbors have p-value > 0.05 and it has p-value < 0.05 that is why even though it is in an area with high ass_ass_va, it is the only parcel tagged as Hotspot.
6. How does changing the spatial weights method affect Local Moran’s I results? Repeat the analysis using another spatial weights method (e.g., KNN or distance). Do the hotspot locations change?
   - The hotspots using Continuity and KNN weights are relatively the same. The hotspot using Distance Threshold are more clustered in an area with the hotspot size being smaller that might have been affected by the threshold selected which is 20.
7. How does changing the attribute affect the spatial clusters? Run Local Moran’s I for: ass_ass_va, ass_market Compare the hotspot patterns. Why might these attributes produce different spatial clusters?
   - When comparing the hotspots between Local Moran's I with Continuity weight and ass_ass_va, vs ass_market we can see that using ass_market as attribute made the hotspot more contiguous. This might be because market assessment value can adjust faster than assessment value therefore areas with high values can have very similar market value when they have different assessment values.

---
