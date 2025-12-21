import matplotlib.pyplot as plt

# line Plot
plt.plot([1, 2, 3], [10, 20, 30], label="Trend")
plt.title("Line Plot") # to label the graph
plt.xlabel("x-axis") # to label the x axis of the graph
plt.ylabel("y-axis") # to label the y axis of the graph
plt.legend() # it creates a visual for the plotted data set, calling with no params creates a legend assigned to the plotted data
plt.show()