# Beacon Reconstruction Attack
>This repository contains the implementation of a novel beacon reconstruction attack that exploits genomic data-sharing beacons by using single nucleotide polymorphism (SNP) correlations and summary statistics. The attack uncovers critical privacy vulnerabilities, allowing the reconstruction of genomic data for individuals in a beacon database. The study demonstrates the feasibility of such attacks and emphasizes the need for enhanced privacy-preserving mechanisms in genomic data sharing.

> **Keywords**: Genome Reconstruction Attacks, [Genomic Data Sharing Beacons](https://en.wikipedia.org/wiki/Global_Alliance_for_Genomics_and_Health), [ Genome Privacy](https://en.wikipedia.org/wiki/Genetic_privacy), [Single-nucleotide polymorphism](https://en.wikipedia.org/wiki/Single-nucleotide_polymorphism)

> ---

## Authors

Kousar Kousar, A. Ercument Cicek, and Sinem Sav  

---

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage Instructions](#usage-instructions)
- [Citations](#citations)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Features

- **Baseline Reconstruction Algorithm**: A greedy approach to reconstruct genomic data without accounting for SNP correlations.
- **Gradient-Based Optimization**: An advanced algorithm alternating between minimizing SNP correlation loss and allele frequency matching.
- **Flexible Configurations**: Allows customization of beacon size, SNP subset size, and attacker knowledge (e.g., leaked genomes).
- **Performance Evaluation**: Detailed analysis of reconstruction effectiveness under various scenarios.

---
## Getting Started

1. Clone the repository, then:
   ```bash
   cd Beacon-Reconstruction-Attack
---

## Installation

You need to install the following dependencies in Python3 for this project:

``bash
pip3 install numpy scipy matplotlib torch pandas argparse==1.4.0

---

## Usage Instructions
### Running Baseline Simulations
- Use the `baseline.py` script to execute the baseline beacon reconstruction attack. Parameters allow you to configure beacon size and SNP count.
   ```bash
   python baseline.py --beacon_Size 50 --snp_count 30

### Key Arguments

- `--Beacon_Size`: Number of individuals targeted for reconstruction.
- `--snp_count`: Size of the SNP subset in the beacon.
 
### Running Optimization Simulations
- Use the `simulate.py` script to execute the beacon reconstruction attack. Parameters allow you to configure beacon size, SNP count, correlation and frequency epoch.
   ```bash
   python simulate.py --beacon_Size 50 --snp_count 30 --corr_epoch 1001 --freq_epoch 501

### Key Arguments

- `--Beacon_Size`: Number of individuals targeted for reconstruction.
- `--snp_count`: Size of the SNP subset in the beacon.
- `--corr_epoch`: Stage 1 of optimization for correlation loss.
- `--freq_epoch`: Stage 2 of optimization for frequency loss.

---
## License

[CC BY-NC-SA 2.0](https://creativecommons.org/licenses/by-nc-sa/2.0/)


© 2024 Beacon Defender Framework.

**For commercial use, please contact.**


---

## Acknowledgments

We would like to thank Göktuğ Gürbüztürk, Efe Erkan, Deniz Aydemir, İrem Aydın, Kerem Ayöz, and Erman Ayday for their contributions to this project.
