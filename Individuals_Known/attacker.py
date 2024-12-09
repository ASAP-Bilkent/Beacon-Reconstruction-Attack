import argparse
from scipy.spatial.distance import hamming
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn.functional as F
import pandas as pd
import math
import sys
from BeaconAnalysis import BeaconAnalysis

# Setup 
parser = argparse.ArgumentParser(description="Run SNP beacon optimization with adjustable parameters")
parser.add_argument("--beacon_size", type=int, nargs='+', required=True, help="List of beacon sizes (e.g., 3 5 10)")
parser.add_argument("--snp_count", type=int, required=True, help="Number of SNPs to analyze")
parser.add_argument("--corr_epoch", type=int, required=True, help="Number of epochs for correlation optimization")
parser.add_argument("--freq_epoch", type=int, required=True, help="Number of epochs for frequency optimization")
parser.add_argument("--leaked_genomes", type=float, required=True, help="Proportion of leaked genomes (0-1)")

args = parser.parse_args()

# Parameters 
Beacon_Size = args.beacon_size
snp_count = args.snp_count
corr_epoch = args.corr_epoch
freq_epoch = args.freq_epoch
leaked_genomes = args.leaked_genomes

# Timing 
# start_time = time.time()
np.random.seed(42)
torch.manual_seed(42)

# Arrays 
precisions = []
recalls = []
f1_scores = []
accuracies = []

# Load data 
beacon = np.load(r"C:\RESEARCH PROJECT\D1\beacon.npy")
print("Loaded beacon data...")
print(f"Beacon data loaded. Shape: {beacon.shape}")

for ind_count in Beacon_Size:
    print("Individual count:", ind_count)
    print("-" * 80)

    # Load 
    print("Loading correlation matrix...")
    corr1 = np.load(r"C:\RESEARCH PROJECT\D1\OpenSNP.npy")
    corr1 = corr1[:snp_count, :100]

    # Calculate 
    corr_analysis = BeaconAnalysis(corr1)
    corr = corr_analysis.calculate_correlations(corr1)
    print(corr.shape, "Initial Corr")

    # tensor
    corr = torch.tensor(corr, dtype=torch.float32, requires_grad=True)

    # Slice
    beacon = beacon[:snp_count, :ind_count]
    print(f"Beacon partitioning for {ind_count} individuals. Shape: {beacon.shape}")
    beacon_analysis = BeaconAnalysis(beacon)
    print(beacon.shape)
    number_of_ones = np.sum(beacon)
    print("Number of ones in beacon:", number_of_ones)
    print(beacon, "Initial Beacon")

    # Query 
    reconstructed_beacon = beacon_analysis.query(proportion=1.0)
    reconstructed_beacon = beacon_analysis.compare_and_sort_columns(beacon, reconstructed_beacon)
    print(reconstructed_beacon, "Initial Reconstructed Beacon")
    number_of_ones = np.sum(reconstructed_beacon)
    print("Number of ones in reconstructed_beacon:", number_of_ones)

    # Training loop 
    max_iterations = 3000
    iteration = 0
    converged = False
    target_frequencies = torch.tensor(np.sum(beacon, axis=1), dtype=torch.float32)
    prev_reconstructed_beacon = None 

    # Define
    known_columns_count = math.ceil(beacon.shape[1] * leaked_genomes)
    mask = np.ones_like(reconstructed_beacon)
    mask[:, :known_columns_count] = 0

    while iteration < max_iterations:
        iteration += 1

        # Stage 1: 
        reconstructed_beacon_tensor = torch.tensor(reconstructed_beacon, dtype=torch.float32, requires_grad=True)
        optimizer = torch.optim.Adam([reconstructed_beacon_tensor], lr=0.001)

        known_columns_tensor = torch.tensor(reconstructed_beacon[:, :known_columns_count], dtype=torch.float32)
        for epoch in range(corr_epoch):
            optimizer.zero_grad()

            remaining_columns_tensor = reconstructed_beacon_tensor[:, known_columns_count:]
            current_correlations = beacon_analysis.calculate_correlations(
                torch.cat([known_columns_tensor, remaining_columns_tensor], dim=1)
            )
            loss = torch.norm(current_correlations - corr, p='fro')
            loss.backward()

            with torch.no_grad():
                reconstructed_beacon_tensor.grad *= torch.tensor(mask, dtype=torch.float32)

            optimizer.step()
            with torch.no_grad():
                reconstructed_beacon_tensor[:, :known_columns_count] = known_columns_tensor

            if epoch % 100 == 0:
                print(f'Iteration {iteration}, Epoch {epoch}, loss {loss.item()}')

        reconstructed_beacon = reconstructed_beacon_tensor.detach().numpy()

        # Stage 2: 
        reconstructed_beacon_tensor = torch.tensor(reconstructed_beacon, dtype=torch.float32, requires_grad=True)
        optimizer = torch.optim.Adam([reconstructed_beacon_tensor], lr=0.001)

        for epoch in range(freq_epoch):
            optimizer.zero_grad()
            freq_loss = beacon_analysis.frequency_loss(
                reconstructed_beacon_tensor * (~torch.tensor(mask, dtype=torch.bool)),
                target_frequencies
            )
            freq_loss.backward()
            optimizer.step()

            with torch.no_grad():
                reconstructed_beacon_tensor[:, :known_columns_count] = torch.tensor(
                    beacon[:, :known_columns_count], dtype=torch.float32
                )

            if epoch % 100 == 0:
                print(f'Iteration {iteration}, Epoch {epoch}, Frequency loss: {freq_loss.item()}')

        reconstructed_beacon = (reconstructed_beacon_tensor.detach().numpy() > 0.5).astype(int)
       

        # Convergence 
        if prev_reconstructed_beacon is not None:
            # Count the number of flips between current and previous beacons
            flips = np.sum(reconstructed_beacon != prev_reconstructed_beacon)
            print(f"Flips: {flips}")

            # Check if flips are less than 10
            if flips < 10:
                converged = True
                print("Converged based on flip.")
                break

        # Update 
        prev_reconstructed_beacon = reconstructed_beacon.copy()


    print("Finished optimization." if converged else "Reached maximum iterations.")
    print(reconstructed_beacon, "Frequency-Optimized Reconstructed Beacon")

    new_beacon = beacon_analysis.compare_and_sort_columns(beacon, reconstructed_beacon)
    print(new_beacon, "Sorted Reconstructed Beacon")

    # Remaining 
    beacon_remaining = beacon[:, known_columns_count:]
    reconstructed_remaining = new_beacon[:, known_columns_count:]

    # Calculate metrics
    accuracy = beacon_analysis.calculate_accuracy(beacon_remaining, reconstructed_remaining)
    precision = beacon_analysis.calculate_precision(beacon_remaining, reconstructed_remaining)
    recall = beacon_analysis.calculate_recall(beacon_remaining, reconstructed_remaining)
    f1 = beacon_analysis.calculate_f1(beacon_remaining, reconstructed_remaining)

    accuracies.append(accuracy)
    precisions.append(precision)
    recalls.append(recall)
    f1_scores.append(f1)

# Timing
total_time = time.time() - start_time

# Print results in a table format
print("Beacon_Size\tAccuracy\tPrecision\tRecall\t\tF1 Score")
for i in range(len(Beacon_Size)):
    print(f"{Beacon_Size[i]}\t\t{accuracies[i]:.3f}\t\t{precisions[i]:.3f}\t\t{recalls[i]:.3f}\t\t{f1_scores[i]:.3f}")
