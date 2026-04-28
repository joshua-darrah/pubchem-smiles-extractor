# 🧪 Drug2SMILES: Automated Chemical Data Enrichment Pipeline

> A Python-based tool that automatically retrieves SMILES (Simplified Molecular Input Line Entry System) strings for drug datasets by querying PubChem and enriching Excel files.

---

## 📌 Project Overview

Drug2SMILES is designed to simplify the process of mapping drug names to their corresponding molecular structures (SMILES).

Given an Excel dataset containing drug names, this tool:
- Searches each drug in PubChem
- Retrieves its Canonical SMILES
- Automatically updates the dataset with results

This is useful for:
- Computational chemistry
- Bioinformatics workflows
- Machine learning datasets
- Pharmaceutical data analysis

---

## ⚙️ Features

- Automatic SMILES retrieval from PubChem
- Handles 1000+ drug entries efficiently
- Creates SMILES column if missing
- Skips already processed entries
- Handles missing/unmatched drugs
- Saves results to a new Excel file

---

## 🛠️ Tech Stack

- Python 3
- pandas
- requests
- openpyxl

---

## 📂 Project Structure


Drug2SMILES/
│
├── main.py
├── drugs.xlsx
├── drugs_with_smiles.xlsx
├── requirements.txt
└── README.md


---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Drug2SMILES.git
cd Drug2SMILES

Install dependencies:

pip install -r requirements.txt
▶️ Usage
1. Prepare your Excel file
Name
Aspirin
Ibuprofen
Paracetamol
2. Run the script
python main.py
3. Output

A new file will be created:

drugs_with_smiles.xlsx
Name	SMILES
Aspirin	CC(=O)OC1=CC=CC=C1C(=O)O
Ibuprofen	CC(C)CC1=CC=C(C=C1)C(C)C(=O)O
Paracetamol	CC(=O)NC1=CC=C(O)C=C1
⚠️ Notes
Some drug names may return "Not Found"
PubChem may return multiple results; first match is used
Ensure drug names are accurate (prefer generic names)
Large datasets may take a few minutes
🚀 Future Improvements
Parallel API requests for faster processing
Improved name matching (synonyms + CID lookup)
Progress bar (tqdm)
Web interface (Flask)
API version of the tool
🤝 Contributing

Pull requests are welcome.

Fork the repo
Create a new branch
Commit changes
Open a pull request
📜 License

This project is open-source under the MIT License.

👨‍💻 Author

Joshua Darrah
Email: darrahjoshua551@gmail.com

LinkedIn: https://www.linkedin.com/in/joshuadarrah/