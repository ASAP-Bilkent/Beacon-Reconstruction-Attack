
#FOR HAPMAP REVISED
# import matplotlib.pyplot as plt
# params = {
#     'legend.fontsize': 90,
#     'figure.figsize': (54, 32),
#     'axes.labelsize': 55,
#     'axes.titlesize': 65,
#     'xtick.labelsize': 55,
#     'ytick.labelsize': 55,
#     'lines.linewidth': 10,
#     'grid.linewidth': 6
# }

# # Apply parameters to matplotlib
# plt.rcParams.update(params)

# Beacon_Size = [3, 10, 25, 50, 100]


# # 3x2 grid of subplots
# fig, axs = plt.subplots(3, 2, figsize=params['figure.figsize'])

# # Subplot titles
# titles = ['A', 'B', 'C', 'D', 'E']
# data_pairs = [
#     (f1_score_gradient_A, f1_score_baseline_A),
#     (f1_score_gradient_B, f1_score_baseline_B),
#     (f1_score_gradient_C, f1_score_baseline_C),
#     (f1_score_gradient_D, f1_score_baseline_D),
#     (f1_score_gradient_E, f1_score_baseline_E),
# ]

# # Plot data on subplots
# for i, ax in enumerate(axs.flat[:-1]): 
#     gradient, baseline = data_pairs[i]
#     ax.plot(Beacon_Size, gradient, color='teal', marker='o', markersize=25, linewidth=params['lines.linewidth'])
#     ax.plot(Beacon_Size, baseline, color='orange', marker='o', markersize=25, linewidth=params['lines.linewidth'])
#     ax.set_title(titles[i], loc='left', fontsize=params['axes.titlesize'])
#     ax.set_ylim(0.5, 1.02)
#     ax.set_xticks(Beacon_Size)
#     ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
#     ax.tick_params(axis='both', labelsize=params['xtick.labelsize'])
#     ax.set_xlabel('Beacon Size', fontsize=params['axes.labelsize'])
#     ax.set_ylabel('F1 Score', fontsize=params['axes.labelsize'])
#     ax.grid(True, linewidth=params['grid.linewidth'])
    

# # Turn off the last empty subplot
# axs[-1, -1].axis('off')


# fig.legend(['Optimization-Based Approach', 'Baseline'], loc='center left', bbox_to_anchor=(0.55, 0.13), fontsize=params['legend.fontsize'])


# plt.tight_layout()
# plt.savefig("C:/Users/USER/Desktop/Results/Figures/Final_Figures/HAPMAPall.pdf")
# plt.show()


#FOR OPENSNP REVISED
import matplotlib.pyplot as plt
params = {
    'legend.fontsize': 90,
    'figure.figsize': (54, 32),
    'axes.labelsize': 55,
    'axes.titlesize': 65,
    'xtick.labelsize': 55,
    'ytick.labelsize': 55,
    'lines.linewidth': 10,
    'grid.linewidth': 6
}

# Apply parameters to matplotlib
plt.rcParams.update(params)

Beacon_Size = [3, 10, 25, 50, 100]

# F1 scores 
f1_score_gradient_A = [0.967, 0.88, 0.85, 0.823, 0.784]
f1_score_baseline_A = [0.733, 0.6, 0.548, 0.502, 0.5]

f1_score_gradient_B = [0.945, 0.85, 0.792, 0.768, 0.76]
f1_score_baseline_B = [0.7, 0.592, 0.536, 0.496, 0.49]

f1_score_gradient_C = [0.863, 0.826, 0.77, 0.731, 0.715]
f1_score_baseline_C = [0.679, 0.542, 0.533, 0.52, 0.463]

f1_score_gradient_D = [0.832, 0.815, 0.754, 0.716, 0.695]
f1_score_baseline_D = [0.662, 0.504, 0.48, 0.455, 0.42]

f1_score_gradient_E = [0.764, 0.736, 0.698, 0.675, 0.636]
f1_score_baseline_E = [0.63, 0.452, 0.426, 0.42, 0.4]

# 3x2 grid of subplots
fig, axs = plt.subplots(3, 2, figsize=params['figure.figsize'])

# Subplot titles
titles = ['A', 'B', 'C', 'D', 'E']
data_pairs = [
    (f1_score_gradient_A, f1_score_baseline_A),
    (f1_score_gradient_B, f1_score_baseline_B),
    (f1_score_gradient_C, f1_score_baseline_C),
    (f1_score_gradient_D, f1_score_baseline_D),
    (f1_score_gradient_E, f1_score_baseline_E),
]

# Plot data on subplots
for i, ax in enumerate(axs.flat[:-1]): 
    gradient, baseline = data_pairs[i]
    ax.plot(Beacon_Size, gradient, color='teal', marker='o', markersize=25, linewidth=params['lines.linewidth'])
    ax.plot(Beacon_Size, baseline, color='orange', marker='o', markersize=25, linewidth=params['lines.linewidth'])
    ax.set_title(titles[i], loc='left', fontsize=params['axes.titlesize'])
    ax.set_ylim(0.5, 1.02)
    ax.set_xticks(Beacon_Size)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.tick_params(axis='both', labelsize=params['xtick.labelsize'])
    ax.set_xlabel('Beacon Size', fontsize=params['axes.labelsize'])
    ax.set_ylabel('F1 Score', fontsize=params['axes.labelsize'])
    ax.grid(True, linewidth=params['grid.linewidth'])
    

# Turn off the last empty subplot
axs[-1, -1].axis('off')


fig.legend(['Optimization-Based Approach', 'Baseline'], loc='center left', bbox_to_anchor=(0.55, 0.13), fontsize=params['legend.fontsize'])


plt.tight_layout()
plt.savefig("C:/Users/Kousar/Desktop/Results/Figures/Final_Figures/OpenSNPall.pdf")
plt.show()



