"""
    Team: Eight minus one
    Description: Run model a specified amount of steps and plot the data. Data is
    collected from the model's datacollector, which stores the amount of people that
    have gone through each exit and the total amount of people on the grid for each step.
"""
from evac_model import EvacModel
import matplotlib.pyplot as plt

model = EvacModel(N=18, width=151, height=200)
model.run_model(steps=215)

data = model.datacollector.get_model_vars_dataframe()

plt.plot(data["Exit1"], label="Exit1")
plt.plot(data["Exit2"], label="Exit2")
plt.plot(data["Exit3"], label="Exit3")
plt.plot(data["Exit4"], label="Exit4")
plt.plot(data["agentCount"], label="People")
plt.legend()
plt.xlabel("Step")
plt.ylabel("Number of People Exiting")
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.show()
