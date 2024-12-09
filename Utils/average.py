import numpy as np

# Define the data
known_20 = np.array([0.837, 0.797, 0.748, 0.707, 0.66])
unknown_20 = np.array([0.783, 0.74, 0.7, 0.66, 0.616])
known_40 = np.array([0.874, 0.825, 0.785, 0.74, 0.685])
unknown_40 = np.array([0.8, 0.77, 0.72, 0.68, 0.63])

# Calculate individual differences for 20% and 40%
differences_20 = known_20 - unknown_20
differences_40 = known_40 - unknown_40

# Print differences for 20% index-wise
print("Differences for p = 20% (index-wise):")
for i, diff in enumerate(differences_20):
    print(f"Index {i}: {known_20[i]} - {unknown_20[i]} = {diff}")

# Print differences for 40% index-wise
print("\nDifferences for p = 40% (index-wise):")
for i, diff in enumerate(differences_40):
    print(f"Index {i}: {known_40[i]} - {unknown_40[i]} = {diff}")

# Calculate average improvement for 20% and 40%
improvement_20 = np.mean(differences_20)
improvement_40 = np.mean(differences_40)

# Calculate the overall average improvement in percentage
xyz = ((improvement_20 + improvement_40) / 2) * 100

# Output the calculations step by step
result = {
    "differences_20": differences_20.tolist(),
    "average_improvement_20": improvement_20,
    "differences_40": differences_40.tolist(),
    "average_improvement_40": improvement_40,
    "overall_average_improvement_percentage": xyz
}

print("\nResult Summary:")
print(result)
