#HapMap for known 1000 revised frequency part
import matplotlib.pyplot as plt

# Data for x-axis
Beacon_Size = [3, 10, 25, 50, 100]

# Revised data for each line
known_20 = [0.837, 0.797, 0.748, 0.707, 0.66]
unknown_20 = [0.783, 0.74, 0.7, 0.66, 0.616]
known_40 = [0.874, 0.825, 0.785, 0.74, 0.685]
unknown_40 = [0.8, 0.77, 0.72, 0.68, 0.63]

# Centralized style parameters
line_width = 3
marker_size = 7
font_size = 25
legend_font_size = 20
tick_font_size = 23  # Tick font size
grid_width = 2.5  # Define grid line width
colors = ['#6c757d', '#e09f3e', '#b5a88f', '#82a6a6']  

# Plotting with consistent styles
plt.figure(figsize=(11, 7))
plt.plot(Beacon_Size, known_20, color=colors[0], marker='o', markersize=marker_size, linewidth=line_width, label='With Known 20%')
plt.plot(Beacon_Size, unknown_20, color=colors[1], marker='o', markersize=marker_size, linewidth=line_width, label='Without known 20%')
plt.plot(Beacon_Size, known_40, color=colors[2], marker='o', markersize=marker_size, linewidth=line_width, label='With Known 40%')
plt.plot(Beacon_Size, unknown_40, color=colors[3], marker='o', markersize=marker_size, linewidth=line_width, label='Without known 40%')

# Labels, title, and grid
plt.xlabel('Beacon Size', fontsize=font_size)
plt.ylabel('F1 Score', fontsize=font_size)
plt.ylim(0.5, 1.0)
plt.xticks(Beacon_Size, fontsize=tick_font_size)  # Set tick font size for x-axis
plt.yticks([0.5, 0.6, 0.7, 0.8, 0.9, 1.0], fontsize=tick_font_size)  # Set tick font size for y-axis
plt.legend(fontsize=legend_font_size)
plt.grid(True, linewidth=grid_width)  # Set the grid width
plt.tight_layout()

# Save the figure
plt.savefig("C:/Users/Kousar/Desktop/Results/Figures/Final_Figures/1000_known.pdf")
plt.show()


