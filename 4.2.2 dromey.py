import matplotlib.pyplot as plt
import numpy as np

# Array of student temp
temp = np.array([-40,-10,-25,2,3,1,0,-13,-12,-14,12,-18,2,1,3,4,-10])

# Create intervals of 10 percentile ranges
intervals = np.arange(-40, 6, 5)

# Group temp into intervals using numpy's histogram function
hist, bins = np.histogram(temp, bins=intervals)

# Create a bar plot of the histogram
plt.bar(bins[:-1], hist, width=(bins[1]-bins[0]), align='edge')

# Add labels and title
plt.xlabel('Mark Range')
plt.ylabel('Frequency')
plt.title('Histogram for average temp recorded in antarctica')

# Display the plot
plt.show()
    