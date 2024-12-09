
import numpy as np
import math
import torch
from scipy.spatial.distance import hamming
import matplotlib.pyplot as plt
import sys

class BeaconAnalysis:
    def __init__(self, beacon):
        self.beacon = beacon

    def query(self, proportion=1.0, leaked_genomes=0.4):
        total_columns = self.beacon.shape[1]
        known_columns_count = math.ceil(total_columns * leaked_genomes)

        queries = np.any(self.beacon, axis=1).astype(int)
        reconstructed_beacon = np.zeros_like(self.beacon)
        reconstructed_beacon[:, :known_columns_count] = self.beacon[:, :known_columns_count]

        for idx, result in enumerate(queries):
            if result == 1:
                remaining_columns = total_columns - known_columns_count
                num_ones_in_remaining_columns = np.sum(self.beacon[idx, known_columns_count:])
                if num_ones_in_remaining_columns > 0:
                    indices_to_fill = np.random.choice(
                        remaining_columns,
                        size=int(num_ones_in_remaining_columns * proportion),
                        replace=False
                    )
                    reconstructed_beacon[idx, known_columns_count + indices_to_fill] = 1

        return reconstructed_beacon
    
    
    # def query(self, proportion=1.0, known_columns_ratio=0.2):
    #     total_columns = self.beacon.shape[1]
    #     known_columns_count = math.ceil(total_columns * known_columns_ratio)

    #     queries = np.any(self.beacon, axis=1).astype(int)
    #     reconstructed_beacon = np.zeros_like(self.beacon)
    #     reconstructed_beacon[:, :known_columns_count] = self.beacon[:, :known_columns_count]

    #     for idx, result in enumerate(queries):
    #         if result == 1:
    #             remaining_columns = total_columns - known_columns_count
    #             num_ones_in_remaining_columns = np.sum(self.beacon[idx, known_columns_count:])
    #             if num_ones_in_remaining_columns > 0:
    #                 indices_to_fill = np.random.choice(
    #                     remaining_columns,
    #                     size=int(num_ones_in_remaining_columns * proportion),
    #                     replace=False
    #                 )
    #                 reconstructed_beacon[idx, known_columns_count + indices_to_fill] = 1

    #     return reconstructed_beacon

    @staticmethod
    def visualize_beacon(beacon):
        plt.imshow(beacon, cmap='gray')
        plt.xlabel('Individuals')
        plt.ylabel('SNPs')
        plt.title('Beacon')
        plt.show()

    @staticmethod
    def calculate_correlations(beacon):
        '''
        Calculates the correlations between each pair of SNPs based on the Sokal-Michener similarity.

        Parameters:
            beacon: A numpy matrix with 0's and 1's representing SNP data.

        Returns:   
            A numpy matrix with the correlations.
        '''
        # Number of individuals in the population
        N_p = beacon.shape[1]

        # Calculate the dot product between all pairs of SNPs
        correlations = beacon @ beacon.T / N_p

        return correlations


    @staticmethod
    def calculate_accuracy(beacon, new_beacon):
        true_positives = np.sum((beacon == 1) & (new_beacon == 1))
        true_negatives = np.sum((beacon == 0) & (new_beacon == 0))
        false_positives = np.sum((beacon == 0) & (new_beacon == 1))
        false_negatives = np.sum((beacon == 1) & (new_beacon == 0))
        return (true_positives + true_negatives) / (true_positives + false_positives + false_negatives + true_negatives)

    @staticmethod
    def calculate_precision(beacon, new_beacon):
        true_positives = np.sum((beacon == 1) & (new_beacon == 1))
        false_positives = np.sum((beacon == 0) & (new_beacon == 1))
        return true_positives / (true_positives + false_positives)

    @staticmethod
    def calculate_recall(beacon, new_beacon):
        true_positives = np.sum((beacon == 1) & (new_beacon == 1))
        false_negatives = np.sum((beacon == 1) & (new_beacon == 0))
        return true_positives / (true_positives + false_negatives)

    @staticmethod
    def calculate_f1(beacon, new_beacon):
        precision = BeaconAnalysis.calculate_precision(beacon, new_beacon)
        recall = BeaconAnalysis.calculate_recall(beacon, new_beacon)
        return 2 * ((precision * recall) / (precision + recall))

    @staticmethod
    def frequency_loss(reconstructed_beacon, target_frequencies):
        """
        Calculates frequency loss for the reconstructed beacon.

        Args:
            reconstructed_beacon (torch.Tensor): Reconstructed beacon matrix.
            target_frequencies (torch.Tensor): Target frequencies for each row.

        Returns:
            torch.Tensor: Frequency loss value.
        """
        current_frequencies = torch.sum(reconstructed_beacon, dim=1)
        loss = torch.mean((current_frequencies - target_frequencies) ** 2)
        return loss

    @staticmethod
    def compare_and_sort_columns(beacon, reconstructed_beacon):
        num_columns_beacon = beacon.shape[1]
        reconstructed_beacon1 = np.zeros_like(beacon)

        for i in range(num_columns_beacon):
            hamming_distances = [
                (hamming(beacon[:, i].flatten(), reconstructed_beacon[:, j].flatten()), j)
                for j in range(reconstructed_beacon.shape[1])
            ]
            _, most_similar_column = min(hamming_distances)
            reconstructed_beacon1[:, i] = reconstructed_beacon[:, most_similar_column]

        return reconstructed_beacon1
    
    def print_metrics_table(individuals, accuracies, precisions, recalls, f1_scores):
        """
        Prints the evaluation metrics in a tabular format.
        """
        print("\nResults Summary:")
        print("Individuals\tAccuracy\tPrecision\tRecall\t\tF1 Score")
        for i in range(len(individuals)):
            print(f"{individuals[i]}\t\t{accuracies[i]:.3f}\t\t{precisions[i]:.3f}\t\t{recalls[i]:.3f}\t\t{f1_scores[i]:.3f}")

    