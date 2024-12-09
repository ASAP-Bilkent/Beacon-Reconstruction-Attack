#For KNOWN-UNKNOWN according to revised frequency part
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
params = {
    'legend.fontsize': 63,
    'figure.figsize': (54, 32),
    'axes.labelsize': 55,
    'axes.titlesize': 65,
    'xtick.labelsize': 55,
    'ytick.labelsize': 55,
    'lines.linewidth': 6,
    'grid.linewidth': 5
}

# Apply parameters to matplotlib
plt.rcParams.update(params)

Beacon_Size = [3, 10, 25, 50, 100]


# Updated data
known_20_A = [1, 0.852, 0.84, 0.81, 0.78]
unknown_20_A = [0.923, 0.80, 0.775, 0.754, 0.72]
known_40_A = [1, 0.91, 0.874, 0.838, 0.81]
unknown_40_A = [0.966, 0.816, 0.794, 0.775, 0.74]

# Updated data for subplot B
known_20_B = [0.93, 0.83, 0.8, 0.774, 0.762]
unknown_20_B = [0.88, 0.778, 0.756, 0.727, 0.7]
known_40_B = [1, 0.856, 0.837, 0.804, 0.785]
unknown_40_B = [0.905, 0.795, 0.774, 0.74, 0.73]

# Updated data for subplot C
known_20_C = [0.89, 0.813, 0.77, 0.734, 0.723]
unknown_20_C = [0.836, 0.75, 0.71, 0.688, 0.67]
known_40_C = [0.954, 0.845, 0.814, 0.76, 0.742]
unknown_40_C = [0.853, 0.78, 0.741, 0.712, 0.69]

# Updated data for subplot D
known_20_D = [0.853, 0.804, 0.76, 0.717, 0.7]
unknown_20_D = [0.813, 0.75, 0.7, 0.658, 0.645]
known_40_D = [0.908, 0.834, 0.799, 0.743, 0.73]
unknown_40_D = [0.831, 0.775, 0.723, 0.68, 0.667]

# Updated data for subplot E
known_20_E = [0.802, 0.764, 0.716, 0.68, 0.645]
unknown_20_E = [0.754, 0.705, 0.67, 0.637, 0.59]
known_40_E = [0.85, 0.793, 0.751, 0.71, 0.679]
unknown_40_E = [0.778, 0.727, 0.686, 0.656, 0.615]


# 3x2 grid of subplots
fig, axs = plt.subplots(3, 2, figsize=params['figure.figsize'])

# Subplot titles
titles = ['A', 'B', 'C', 'D', 'E']
data_pairs = [
    ([known_20_A, unknown_40_A, known_40_A, unknown_20_A], "A"),
    ([known_20_B, unknown_40_B, known_40_B, unknown_20_B], "B"),
    ([known_20_C, unknown_40_C, known_40_C, unknown_20_C], "C"),
    ([known_20_D, unknown_40_D, known_40_D, unknown_20_D], "D"),
    ([known_20_E, unknown_40_E, known_40_E, unknown_20_E], "E"),
]

# Plot data on subplots
for i, ax in enumerate(axs.flat[:-1]):
    known_20, unknown_40, known_40, unknown_20 = data_pairs[i][0]
    title = data_pairs[i][1]

    # ax.plot(Beacon_Size, known_20, label="Known 20%", color='#f4a261', marker='o', markersize=20, linewidth=params['lines.linewidth'])  # Muted Orange
    # ax.plot(Beacon_Size, unknown_20, label="Unknown 20%", color='#a3c4dc', marker='o', markersize=20, linewidth=params['lines.linewidth'])  # Muted Green
    # ax.plot(Beacon_Size, unknown_40, label="Unknown 40%", color='#82a6a6', marker='o', markersize=20, linewidth=params['lines.linewidth'])  # Muted Teal
    # ax.plot(Beacon_Size, known_40, label="Known 40%", color='#b5a88f', marker='o', markersize=20, linewidth=params['lines.linewidth'])  # Muted Beige

    ax.plot(Beacon_Size, known_20, label="Known 20%", color='#6c757d', marker='o', markersize=18, linewidth=params['lines.linewidth'])  # Muted Orange
    ax.plot(Beacon_Size, unknown_20, label="Unknown 20%", color='#e09f3e', marker='o', markersize=18, linewidth=params['lines.linewidth'])  # Muted Green
    ax.plot(Beacon_Size, unknown_40, label="Unknown 40%", color='#82a6a6', marker='o', markersize=18, linewidth=params['lines.linewidth'])  # Muted Teal
    ax.plot(Beacon_Size, known_40, label="Known 40%", color='#b5a88f', marker='o', markersize=18, linewidth=params['lines.linewidth'])  # Muted Beige


    

    ax.set_title(title, loc='left', fontsize=params['axes.titlesize'])
    ax.set_ylim(0.5, 1.02)
    ax.set_xticks(Beacon_Size)
    ax.set_yticks([0.5,0.6, 0.7, 0.8, 0.9, 1.0])
    ax.tick_params(axis='both', labelsize=params['xtick.labelsize'])
    ax.set_xlabel('Beacon Size', fontsize=params['axes.labelsize'])
    ax.set_ylabel('F1 score', fontsize=params['axes.labelsize'])
    ax.grid(True, linewidth=params['grid.linewidth'])

# Turn off last empty subplot
axs[-1, -1].axis('off')

from matplotlib.lines import Line2D

#combined legend handles
custom_handles = [
    Line2D([0, 1], [0, 0], color='#6c757d', lw=params['lines.linewidth'], marker='o', markersize=18, label='With Known 20%'),
    Line2D([0, 1], [0, 0], color='#e09f3e', lw=params['lines.linewidth'], marker='o', markersize=18, label='Without known 20%'),
    Line2D([0, 1], [0, 0], color='#b5a88f', lw=params['lines.linewidth'], marker='o', markersize=18, label='With Known 40%'),
    Line2D([0, 1], [0, 0], color='#82a6a6', lw=params['lines.linewidth'], marker='o', markersize=18, label='Without known 40%')
]


# Add the legend with 2 columns
fig.legend(
    handles=custom_handles, 
    labels=['With Known 20%', 'Without known 20%', 'With Known 40%', 'Without known 40%'],  
    loc='center left', 
    # bbox_to_anchor=(0.515, 0.17),
    bbox_to_anchor=(0.515, 0.19),   
    fontsize=params['legend.fontsize'],  
    ncol=2  
)


# Adjust layout and save the plot
plt.tight_layout()
plt.savefig("C:/Users/Kousar/Desktop/Results/Figures/Final_Figures/KNOWNall2.pdf")
plt.show()