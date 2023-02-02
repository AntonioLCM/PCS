"""
    Team: Eight minus one
    Description: Run model a specified amount of steps and plot the data. Data is
    collected from the model's datacollector, which stores the amount of people that
    have went through each exit and the total amount of people on the grid for each step.
"""
from evac_model import EvacModel
import matplotlib.pyplot as plt

model = EvacModel(N=5000, width=151, height=200)
model.run_model(steps=215)

data = model.datacollector.get_model_vars_dataframe()

plt.bar(data.index, data["Exit1"], label="Exit1")
plt.bar(data.index, data["Exit2"], label="Exit2", bottom=data["Exit1"])
plt.bar(data.index, data["Exit3"], label="Exit3",
        bottom=data["Exit1"] + data["Exit2"])
plt.bar(data.index, data["Exit4"], label="Exit4",
        bottom=data["Exit1"] + data["Exit2"] + data["Exit3"])
plt.legend()
plt.xlabel("Step")
plt.ylabel("Number of People Exiting")
plt.show()
