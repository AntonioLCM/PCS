# Agent-based evacuation model based on lab42
## Overview
In this project our goal is to find a configuration of emergency arrows that leads to a faster evacuation compared to the current configuration of arrows. The pathfinding algorithm used in our evacuation model is the a* algorithm, the visualization of the simulation is done with mesa.
## Dependencies 
Make sure you have the following dependencies installed :

[mesa](https://pypi.org/project/Mesa/) - pip install mesa    

[matplotlib](https://matplotlib.org/stable/users/installing/index.html) - pip install matplotlib

[pillow]() - pip install pillow

## Running mesa visualization 
1. Clone the repository 
2. Navigate to the cloned project directory
3. To run the mesa visualization with the improved arrow configuration you can run the evac_model_viz.py file. ($ python3 evac_model_viz.py)
4. Press start on the top right corner to run the simulation.
5. (optional) Change the slider to 20 for a faster simulation.

## Reproducing representative image
To reproduce the representative image "representative_img.png" follow these steps:
1. Navigate to the cloned project directory
2. Run the dataviz_plot.py file ($ python3 dataviz_plot.py)

This plot shows the amount of people that have gone through each exit and the total amount of people on the grid for each step.