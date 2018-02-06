# CONTRIBUTING
This projects aims at being inherently open source. Algorithms should use open-source technologies and open-source datasets.
We aim to strusture the respository so as to faciliate volunteer contributions. Please follow the guidelines below to get started and contribute as efficiently as possible.

## Datasets involved
Satellite imagery in the public domain.
	Landsat 8, Sentinel 1, 2 (available through Google Earth Engine).

Location data
	Coordinates of know IDP and refugee camps in Iraq.
	The coordinates can be found in [data](data).

## Methods and expected tasks
Below is a tentative outline of the proposed tasks to estimate the extent and population changes in informal settlements.

### Task I - Size Estimation
Data acquisition
List of coordinates for the settlements of interest (formal or informal).
Create dataset of public satellite imagery containing each settlement
Contour detection and size estimation
Validate results visually or with existing location datasets.

### Task I-b (Optional - Not needed if results of Phase I are satisfactory)
Data augmentation
Use human input (i.e. Mechanical Turk) to create a training dataset with crowd-sourced contours.
New iteration of contour / sizing algorithms with added input for accuracy. The additional info and human input will allow the use of more complex algorithms for training.

### Task II - Population Estimation
Research settlement size estimates at different dates.
Explore algorithms to estimate settlement population including extrapolation/downscaling  of existing datasets

### Task III - Tracking
Test algorithms on “live” data, i.e. Planet or DG.
If successful, we could think about creating a change tracker if the size of settlement Z changes by more than X %.
