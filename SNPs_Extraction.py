import pandas as pd
import os
import glob
import re

# Function to log progress for debugging or tracking
def log_step(message):
    """
    Logs a message for tracking progress.

    Parameters:
        message (str): The message to log.
    """
    print(f"[INFO]: {message}")


# Function to calculate allele counts
def calculate_allele_counts(allele_data, reference_allele, other_allele):
    """
    Calculate allele counts for reference and other alleles.

    Parameters:
        allele_data (list): List of genotype data for individuals.
        reference_allele (str): The reference allele.
        other_allele (str): The alternate allele.

    Returns:
        tuple: A tuple containing counts for reference and other alleles.
    """
    reference_count = 0  # Initialize reference allele count
    other_count = 0  # Initialize other allele count

    # Iterate over each genotype in allele data
    for genotype in allele_data:
        if genotype == reference_allele * 2:  
            reference_count += 2 
        elif genotype == other_allele * 2:  
            other_count += 2  
        elif reference_allele + other_allele in genotype: 
            reference_count += 1 
            other_count += 1  

    # Return the calculated counts
    return reference_count, other_count


# Function to process a single line of the input file
def process_line(line):
    """
    Processes a single line to extract and calculate allele information.

    Parameters:
        line (str): A single line from the input file.

    Returns:
        list: A list of processed allele frequency data, or None for invalid lines.
    """
    log_step("Splitting line into parts.")
    parts = line.strip().split()  

    # Validation checks for the line
    if not parts:  
        log_step("Empty line detected, skipping.")
        return None
    if parts[0].startswith("rs#"):  
        log_step("Header line detected, skipping.")
        return None
    if len(parts) < 12:  
        log_step("Malformed line detected, skipping.")
        return None

    # Extract marker information
    marker_id = parts[0]
    log_step(f"Extracted marker ID: {marker_id}")
    alleles = parts[1].split("/")  
    chrom = re.sub("chr", "", parts[2])  
    pos = parts[3]  

    # Extract reference and alternate alleles
    reference_allele = alleles[0] if len(alleles) > 0 else None
    other_allele = alleles[1] if len(alleles) > 1 else None

    if not reference_allele or not other_allele:
        log_step(f"Missing alleles for marker {marker_id}, skipping.")
        return None

    # Extract allele data
    allele_data = parts[12:]
    log_step(f"Processing genotype data for marker {marker_id}.")

    # Calculate allele counts
    reference_count, other_count = calculate_allele_counts(allele_data, reference_allele, other_allele)
    log_step(f"Allele counts calculated: Reference={reference_count}, Other={other_count}")

    # Calculate total alleles
    total_alleles = 2 * len(allele_data)
    log_step(f"Total alleles calculated: {total_alleles}")

    # Calculate frequencies
    reference_allele_freq = reference_count / total_alleles
    other_allele_freq = other_count / total_alleles
    log_step(f"Frequencies calculated: Reference={reference_allele_freq}, Other={other_allele_freq}")

    # Determine minor allele frequency (MAF)
    maf = min(reference_allele_freq, other_allele_freq)
    log_step(f"MAF calculated: {maf}")

    # Return processed data
    return [
        chrom, pos, marker_id, reference_allele, reference_allele_freq,
        other_allele, other_allele_freq, maf
    ]


# Function to process an entire file
def process_file(filename):
    """
    Processes an input file to extract allele frequency data.

    Parameters:
        filename (str): The path to the input file.

    Returns:
        DataFrame: A DataFrame containing processed data for the file.
    """
    log_step(f"Opening file: {filename}")
    processed_data = []  

    # Open and read the file line by line
    with open(filename, 'r') as file:
        for line in file:
            log_step("Reading a new line.")
            processed_line = process_line(line)  
            if processed_line:  
                processed_data.append(processed_line)

    # Create a DataFrame from processed data
    columns = [
        "chromosome", "position", "markerId", "referenceAllele",
        "referenceAlleleFrequency", "otherAllele", "otherAlleleFrequency", "maf"
    ]
    df = pd.DataFrame(processed_data, columns=columns)
    log_step(f"File processed successfully: {filename}")

    return df


# Main script to process all files and combine results
base_directory = r"C:\Users\Kousar\Downloads\Data_Processing\For_text"
all_data = []

log_step(f"Searching for files in base directory: {base_directory}")
for filepath in glob.glob(os.path.join(base_directory, '**', '*.txt'), recursive=True):
    log_step(f"Found file: {filepath}")
    df = process_file(filepath)  # Process the file
    all_data.append(df)  # Add DataFrame to list

log_step("Combining all processed DataFrames.")
combined_df = pd.concat(all_data, ignore_index=True)

# Save combined data to a CSV file
output_path = os.path.join(base_directory, "MAF_combined.csv")
log_step(f"Saving combined data to: {output_path}")
combined_df.to_csv(output_path, index=False)

log_step("Processing completed successfully.")
