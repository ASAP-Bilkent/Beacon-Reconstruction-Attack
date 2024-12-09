import numpy as np

# Define the data
known_20 = np.array([0.837, 0.797, 0.748, 0.707, 0.66])
known_40 = np.array([0.874, 0.825, 0.785, 0.74, 0.685])

# Calculate the F1-score gap for known data
differences_known = known_40 - known_20

# Calculate average gap for known data
average_gap_known = np.mean(differences_known)

# Convert to percentage
average_gap_known_percentage = average_gap_known * 100

# Print the differences and results
print("F1-score gap for known data (index-wise):")
for i, diff in enumerate(differences_known):
    print(f"Index {i}: {known_40[i]} - {known_20[i]} = {diff:.4f}")

print(f"\nAverage F1-score gap for known data: {average_gap_known:.4f}")
print(f"Average F1-score gap for known data (percentage): {average_gap_known_percentage:.2f}%")
