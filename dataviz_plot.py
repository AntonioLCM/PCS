from evac_model import EvacModel
from mesa.datacollection import DataCollector
import numpy as np
import matplotlib.pyplot as plt

model = EvacModel(N=5000, width=151, height=200)
model.run_model(steps=250)

data = model.datacollector.get_model_vars_dataframe()

plt.plot(data["Exit1"], label="Exit1")
plt.plot(data["Exit2"], label="Exit2")
plt.plot(data["Exit3"], label="Exit3")
plt.plot(data["Exit4"], label="Exit4")
total_exits = data["Exit1"] + data["Exit2"] + data["Exit3"] + data["Exit4"]
avg_exits = total_exits / 4
plt.plot(avg_exits, label="TotalExited")
plt.legend()
plt.xlabel("Step")
plt.ylabel("Number of People Exiting")
plt.show()
