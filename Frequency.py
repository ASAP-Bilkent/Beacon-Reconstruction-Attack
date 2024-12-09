import pandas as pd
import numpy as np

def log_message(message):
    """
    Logs a message to indicate the current step or process.

    Parameters
    ----------
    message : str
        The message to log.
    """
    print(f"[INFO]: {message}")

def read_beacon_file(beacon_path, nrows):
    """
    Reads the beacon file and loads it into a DataFrame.

    Parameters
    ----------
    beacon_path : str
        Path to the beacon file.
    nrows : int
        Number of rows to read.

    Returns
    ----------
    pd.DataFrame
        DataFrame containing the beacon data.
    """
    log_message(f"Reading the beacon file: {beacon_path}")
    beacon = pd.read_csv(beacon_path, delim_whitespace=True, nrows=30)
    log_message(f"Beacon file loaded with shape: {beacon.shape}")
    return beacon

def read_maf_file(maf_path, nrows):
    """
    Reads the MAF file and loads it into a DataFrame.

    Parameters
    ----------
    maf_path : str
        Path to the MAF file.
    nrows : int
        Number of rows to read.

    Returns
    ----------
    pd.DataFrame
        DataFrame containing the MAF data.
    """
    log_message(f"Reading the MAF file: {maf_path}")
    maf = pd.read_csv(maf_path, delim_whitespace=True, nrows=nrows)
    log_message(f"MAF file loaded with shape: {maf.shape}")
    return maf

def determine_minor_allele(maf):
    """
    Determines the minor allele for each SNP in the MAF file.

    Parameters
    ----------
    maf : pd.DataFrame
        DataFrame containing the MAF data.

    Returns
    ----------
    pd.DataFrame
        Updated DataFrame with a 'minorAllele' column.
    """
    log_message("Determining the minor allele for each SNP.")
    maf['minorAllele'] = maf.apply(
        lambda row: row['referenceAllele'] if row['referenceAlleleFrequency'] < 0.5 else row['otherAllele'], 
        axis=1
    )
    log_message("Minor alleles determined successfully.")
    return maf

def initialize_snp_matrix(beacon):
    """
    Initializes a zero matrix for SNP data.

    Parameters
    ----------
    beacon : pd.DataFrame
        DataFrame containing the beacon data.

    Returns
    ----------
    np.ndarray
        A zero-initialized matrix for SNP data.
    """
    log_message("Initializing the SNP matrix.")
    matrix = np.zeros((beacon.shape[0], beacon.shape[1] - 1))
    log_message(f"SNP matrix initialized with shape: {matrix.shape}")
    return matrix

def populate_snp_matrix(beacon, maf, matrix):
    """
    Populates the SNP matrix with 0s and 1s based on minor allele presence.

    Parameters
    ----------
    beacon : pd.DataFrame
        DataFrame containing the beacon data.
    maf : pd.DataFrame
        DataFrame containing the MAF data.
    matrix : np.ndarray
        Zero-initialized SNP matrix to populate.

    Returns
    ----------
    np.ndarray
        Populated SNP matrix.
    """
    log_message("Populating the SNP matrix.")
    for i in range(beacon.shape[0]):
        # Get minor allele for current SNP
        mA = maf.iloc[i]["minorAllele"]
        log_message(f"Processing SNP {i + 1}/{beacon.shape[0]} with minor allele: {mA}")

        # Iterate over each individual
        for j in range(beacon.shape[1] - 1):
            genotype = beacon.iloc[i, j + 1]  # Extract genotype
            if mA in genotype:  # Check for minor allele presence
                matrix[i, j] = 1  # Set SNP matrix value to 1
                log_message(f"Individual {j + 1}/{beacon.shape[1] - 1} contains the minor allele.")
    log_message("SNP matrix population completed.")
    return matrix

def save_data(matrix, maf):
    """
    Saves the SNP matrix and minor allele frequencies to files.

    Parameters
    ----------
    matrix : np.ndarray
        SNP matrix to save.
    maf : pd.DataFrame
        DataFrame containing the MAF data.
    """
    log_message("Saving SNP matrix to file: beacon30.npy")
    np.save("beacon30.npy", matrix)
    log_message("SNP matrix saved successfully.")

    log_message("Saving minor allele frequencies to file: freq.npy")
    frequencies = maf["maf"].to_numpy()
    np.save("freq.npy", frequencies)
    log_message("Minor allele frequencies saved successfully.")

def extract_SNPs(beacon_path="Beacon_164.txt", maf_path="MAF.txt", nrows=30):
    """
    Extracts SNPs from a beacon and stores them in a numpy array, 
    along with the minor allele frequencies.

    Parameters
    ----------
    beacon_path : str
        Path to the beacon file.
    maf_path : str
        Path to the MAF file.
    nrows : int
        Number of rows to read from the files.

    Returns
    ----------
    None
    """
    log_message("Starting SNP extraction process.")
    beacon = read_beacon_file(beacon_path, nrows)
    maf = read_maf_file(maf_path, nrows)
    maf = determine_minor_allele(maf)
    matrix = initialize_snp_matrix(beacon)
    matrix = populate_snp_matrix(beacon, maf, matrix)
    save_data(matrix, maf)
    log_message("SNP extraction process completed.")

# Run the function
extract_SNPs()
