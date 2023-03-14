import matplotlib.pyplot as plt
import numpy as np

# Array of student marks
marks = np.array([78, 90, 85, 65, 70, 80, 92, 88, 75, 83, 72, 68, 90, 95, 87, 80, 85, 92, 76, 85])

# Create intervals of 10 percentile ranges
intervals = np.arange(0, 101, 10)

# Group marks into intervals using numpy's histogram function
hist, bins = np.histogram(marks, bins=intervals)

# Create a bar plot of the histogram
plt.bar(bins[:-1], hist, width=(bins[1]-bins[0]), align='edge')

# Add labels and title
plt.xlabel('Mark Range')
plt.ylabel('Frequency')
plt.title('Histogram of Student Marks with 10 Percentile Ranges')

# Display the plot
plt.show()
