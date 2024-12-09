import matplotlib.pyplot as plt

# Data for Beacon_Size and time (in hours) for different SNP counts
Beacon_Size = [3, 10, 25, 50, 100]
time_30 = [0.001, 0.085, 0.6239, 1.2714, 2.6]
time_50 = [1.002, 1.2, 1.8, 2.8, 3.9]
time_100 = [2.06, 2.6, 3.26, 5.0071, 6.2]
time_500 = [2.7, 3.5, 4.5, 6.2, 7.6]
time_1000 = [3.2, 4.3, 5.7, 7.8, 8.5]
time_2000 = [4.2, 5.3, 6.9, 8.9, 10.03]

# Define colors and marker size
colors = ['teal', 'orange', '#4C72B0', '#55A868', '#C44E52', '#8172B3']
marker_size = 3

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(Beacon_Size, time_30, label='SNP Count 30', marker='o', color=colors[0], markersize=marker_size)
plt.plot(Beacon_Size, time_50, label='SNP Count 50', marker='o', color=colors[1], markersize=marker_size)
plt.plot(Beacon_Size, time_100, label='SNP Count 100', marker='o', color=colors[2], markersize=marker_size)
plt.plot(Beacon_Size, time_500, label='SNP Count 500', marker='o', color=colors[3], markersize=marker_size)
plt.plot(Beacon_Size, time_1000, label='SNP Count 1000', marker='o', color=colors[4], markersize=marker_size)
plt.plot(Beacon_Size, time_2000, label='SNP Count 2000', marker='o', color=colors[5], markersize=marker_size)

# Customizing the plot
plt.xlabel('Beacon_Size', fontsize=12)
plt.ylabel('Time (in hours)', fontsize=12)
plt.ylim(-1, 10)  # Set y-axis scale from -1 to 21
plt.xticks(fontsize=8)  # Set font size for x-axis numbers
plt.yticks(range(-1, 12, 1), fontsize=8)  # Set font size for y-axis numbers
plt.legend(loc='upper left', fontsize=8)

# Save and display the plot
plt.savefig("C:/Users/Kousar/Desktop/Results/Figures/Time_Analysis_Adam.pdf")  # Save at high resolution
plt.show()
