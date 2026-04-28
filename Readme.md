🧪 Drug2SMILES: Automated Chemical Data Enrichment Pipeline

A Python-based tool that automatically retrieves SMILES (Simplified Molecular Input Line Entry System) strings for drug datasets by querying PubChem and enriching Excel files.

📌 Project Overview

Drug2SMILES is designed to simplify the process of mapping drug names to their corresponding molecular structures (SMILES).

Given an Excel dataset containing drug names, this tool:

Searches each drug in PubChem
Retrieves its Canonical SMILES
Automatically updates the dataset with the results

This is especially useful for:

Computational chemistry projects
Bioinformatics workflows
Machine learning datasets involving molecular data
Pharmaceutical data analysis
⚙️ Features
✅ Automatic SMILES retrieval from PubChem
✅ Supports large datasets (1000+ drugs)
✅ Creates SMILES column if missing
✅ Skips already processed entries
✅ Handles missing or unmatched drugs gracefully
✅ Saves enriched dataset to a new Excel file
🛠️ Tech Stack
Python 3
pandas – data handling
requests – API calls
openpyxl – Excel file support
📂 Project Structure
Drug2SMILES/
│
├── drugs.xlsx                  # Input dataset
├── drugs_with_smiles.xlsx      # Output dataset
├── main.py                     # Main script
└── README.md                   # Project documentation
📥 Installation

Clone the repository:

git clone https://github.com/your-username/drug2smiles.git
cd drug2smiles

Install dependencies:

pip install pandas requests openpyxl
▶️ Usage
Prepare your Excel file:
Name
Aspirin
Ibuprofen
Paracetamol
Update configuration in main.py (if needed):
INPUT_FILE = "drugs.xlsx"
OUTPUT_FILE = "drugs_with_smiles.xlsx"
DRUG_NAME_COLUMN = "Name"
Run the script:
python main.py
📊 Output Example
Name	SMILES
Aspirin	CC(=O)OC1=CC=CC=C1C(=O)O
Ibuprofen	CC(C)CC1=CC=C(C=C1)C(C)C(=O)O
Paracetamol	CC(=O)NC1=CC=C(O)C=C1
⚠️ Notes & Limitations
Some drug names may not return results (marked as "Not Found")
PubChem may return multiple matches; the script selects the first result
Performance depends on dataset size and API response time
Ensure consistent drug naming (prefer generic names over brand names)
🚀 Future Improvements
Parallel API requests for faster processing
Improved matching using synonyms and CID lookup
Progress bar integration
Web interface for non-technical users
Integration with other chemical databases
🤝 Contributing

Contributions are welcome!

Fork the repo
Create a new branch
Make your changes
Submit a pull request
📜 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Joshua Darrah
Email: darrahjoshua551@gmail.com

LinkedIn: https://www.linkedin.com/in/joshuadarrah/