import numpy as np

#polynomial fit with degree = 3
model = np.poly1d(np.polyfit(x, y,3))

#add fitted polynomial line to scatterplot
polyline = np.linspace(2, 13, 13)
plt.scatter(x, y)
plt.plot(polyline, model(polyline))
plt.show()

print(model)