# import matplotlib.pyplot as plt

# # Define updated parameters
# params = {
#     'legend.fontsize': 41,
#     'figure.figsize': (24, 16),
#     'axes.labelsize': 42,
#     'axes.titlesize': 42,
#     'xtick.labelsize': 40,
#     'ytick.labelsize': 40,
#     'lines.linewidth': 7,
#     'grid.linewidth': 5
# }

# # Apply parameters to matplotlib
# plt.rcParams.update(params)

# # Create a single row of subplots with 2 subplots
# fig, axs = plt.subplots(1, 2, figsize=params['figure.figsize'])

# # Data and titles for subplots
# data_pairs = [
#     (f1_score_gradient_A, f1_score_baseline_A, 'A'),
#     (f1_score_gradient_B, f1_score_baseline_B, 'B'),
# ]

# # Plot each subplot
# for i, (gradient, baseline, title) in enumerate(data_pairs):
#     ax = axs[i]
#     ax.plot(Beacon_Size, gradient, color='teal', marker='o', markersize=16, linewidth=params['lines.linewidth'], label='Gradient-Based Approach')
#     ax.plot(Beacon_Size, baseline, color='orange', marker='o', markersize=16, linewidth=params['lines.linewidth'], label='Baseline')
#     ax.set_title(title, loc='left', fontsize=params['axes.titlesize'])
#     ax.set_ylim(0.2, 1.02)
#     ax.set_xticks(Beacon_Size)
#     ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
#     ax.set_xlabel('Beacon Size', fontsize=params['axes.labelsize'])
#     ax.set_ylabel('F1 Score', fontsize=params['axes.labelsize'])
#     ax.grid(True, linewidth=params['grid.linewidth'])

# # Add a single legend below the subplots
# # fig.legend(['Gradient-Based Approach', 'Baseline'], loc='lower center', fontsize=params['legend.fontsize'], bbox_to_anchor=(0.5, -0.1), ncol=2)
# fig.legend(['Optimization-Based Approach', 'Baseline'], loc='lower center', fontsize=params['legend.fontsize'], ncol=2)

# # Adjust layout and save
# plt.tight_layout(rect=[0, 0.1, 1, 0.9])  # Leave space for the legend below
# plt.savefig("C:/Users/USER/Desktop/Results/Figures/Final_Figures/OPENSNP_two_subplots.pdf")
# plt.show()


import matplotlib.pyplot as plt

# Define updated parameters
params = {
    'legend.fontsize': 41,
    'figure.figsize': (24, 16),
    'axes.labelsize': 42,
    'axes.titlesize': 42,
    'xtick.labelsize': 40,
    'ytick.labelsize': 40,
    'lines.linewidth': 7,
    'grid.linewidth': 5
}

# Apply parameters to matplotlib
plt.rcParams.update(params)

# Individuals and F1 scores
Beacon_Size = [3, 10, 25, 50, 100]
f1_score_gradient_A = [0.59, 0.54, 0.51, 0.46, 0.44]
f1_score_baseline_A = [0.48, 0.33, 0.3, 0.275, 0.26]

f1_score_gradient_B = [0.51, 0.45, 0.434, 0.36, 0.34]
f1_score_baseline_B = [0.38, 0.3, 0.262, 0.24, 0.22]


# Create a single row of subplots with 2 subplots
fig, axs = plt.subplots(1, 2, figsize=params['figure.figsize'])

# Data and titles for subplots
data_pairs = [
    (f1_score_gradient_A, f1_score_baseline_A, 'A'),
    (f1_score_gradient_B, f1_score_baseline_B, 'B'),
]

# Plot each subplot
for i, (gradient, baseline, title) in enumerate(data_pairs):
    ax = axs[i]
    ax.plot(Beacon_Size, gradient, color='teal', marker='o', markersize=16, linewidth=params['lines.linewidth'], label='Gradient-Based Approach')
    ax.plot(Beacon_Size, baseline, color='orange', marker='o', markersize=16, linewidth=params['lines.linewidth'], label='Baseline')
    ax.set_title(title, loc='left', fontsize=params['axes.titlesize'])
    ax.set_ylim(0.0, 1.02)
    ax.set_xticks(Beacon_Size)
    ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_xlabel('Beacon Size', fontsize=params['axes.labelsize'])
    ax.set_ylabel('F1 Score', fontsize=params['axes.labelsize'])
    ax.grid(True, linewidth=params['grid.linewidth'])

# Add a single legend below the subplots
# fig.legend(['Gradient-Based Approach', 'Baseline'], loc='lower center', fontsize=params['legend.fontsize'], bbox_to_anchor=(0.5, -0.1), ncol=2)
fig.legend(['Optimization-Based Approach', 'Baseline'], loc='lower center', fontsize=params['legend.fontsize'], ncol=2)

# Adjust layout and save
plt.tight_layout(rect=[0, 0.1, 1, 0.9])  # Leave space for the legend below
plt.savefig("C:/Users/Kousar/Desktop/Results/Figures/Final_Figures/Frequency_two_subplots.pdf")
plt.show()
