# CONTRIBUTING
This project is inherently open-source and collaborative. We will structure this respository and project to faciliate volunteer contributions. Please follow the guidelines available below to get started and contribute as efficiently as possible.
Just a few quick notes:
	- Algorithms should use open-source technologies.
	- Dataset used should be open-source or easily available and trackable.


## Initial data and datasets involved
### Location data
	Coordinates of know IDP and refugee camps in Iraq.
	The coordinates can be found in [data](data).

### Satellite imagery in the public domain.
	Landsat 8, Sentinel 1, 2 (available through Google Earth Engine).


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


## Project management
We will use Github issues and [waffle.io/benvolia/unicef-innovation-settlement-monitoring/]() to organize the project.
Issues will try to divide the work into small manageable tasks to eventually folllow the project outlined above.
### Issue tracking
The [project board](https://waffle.io/benvolia/unicef-innovation-settlement-monitoring) has several columns:
	- Backlog: List of tasks and issues
	- Next: *Important tasks that needs to get done, find one that suits your skills and let's go!*
	- In Progress: *Somebody is working on it, let them know if you can help!*
	- Review: *A PR is out for this task, have a look and see if you have any comments!*
	- Done: *The associated PR has been approved and merged, good job!*
To coordinate efforts, we ask contributors to assign themselves to the tasks they are working on.

### Issue tagging
When looking for a new task to contribute, prioritize looking for tasks in `Next` before looking at issues in the Backlog.
Usually, we will try and keep issues with tags to orient contributors. Here are a few tags to lookout for:
	- `good-first-issue`: *Easier tasks that help discover the project*
	- `bug`
	- `priority`
	- `needs-help`

## Maintainer
The maintainer associated to this project is `ericboucher`. If you have any questions, you can contact him at [boucher@bayesimpact.org](mailto:boucher@bayesimpact.org)

