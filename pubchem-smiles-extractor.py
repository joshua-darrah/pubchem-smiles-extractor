import pandas as pd
import requests
import time

# CONFIGURATION
INPUT_FILE = "drugs.xlsx"   # your Excel file
OUTPUT_FILE = "drugs_with_smiles.xlsx"
DRUG_NAME_COLUMN = "Name"   # column with drug names
SMILES_COLUMN = "SMILES"    # column to store SMILES

# FUNCTION TO GET SMILES
def get_smiles(drug_name):
    """
    Fetch Canonical SMILES from PubChem using drug name.
    Returns SMILES string or None if not found.
    """
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{drug_name}/property/CanonicalSMILES/JSON"
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            smiles = data["PropertyTable"]["Properties"][0]["CanonicalSMILES"]
            return smiles
        else:
            return None
    
    except Exception as e:
        print(f"Error fetching {drug_name}: {e}")
        return None

# MAIN SCRIPT
def main():
    # Load Excel
    df = pd.read_excel(INPUT_FILE)

    # Ensure drug name column exists
    if DRUG_NAME_COLUMN not in df.columns:
        raise ValueError(f"Column '{DRUG_NAME_COLUMN}' not found in Excel.")

    # Create SMILES column if it doesn't exist
    if SMILES_COLUMN not in df.columns:
        df[SMILES_COLUMN] = ""

    # Loop through drugs
    for i, drug in enumerate(df[DRUG_NAME_COLUMN]):
        if pd.isna(drug):
            continue

        # Skip if already filled
        if pd.notna(df.loc[i, SMILES_COLUMN]) and df.loc[i, SMILES_COLUMN] != "":
            continue

        print(f"Processing {i+1}/{len(df)}: {drug}")

        smiles = get_smiles(str(drug))

        if smiles:
            df.loc[i, SMILES_COLUMN] = smiles
        else:
            df.loc[i, SMILES_COLUMN] = "Not Found"

        # Sleep to avoid rate limiting
        time.sleep(0.2)

    # Save to new Excel file
    df.to_excel(OUTPUT_FILE, index=False)
    print(f"\nDone! Saved to {OUTPUT_FILE}")

# RUN
if __name__ == "__main__":
    main()