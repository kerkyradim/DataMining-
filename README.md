# Data Mining — Oscar Winner Prediction

University assignment for the **Data Mining** course (Harokopio University of Athens, Department of Informatics and Telematics).

**Task:** predict whether a film is an **Oscar winner** from movie metadata (critics/audience scores, genre, box office, budget, release date, and related features).
  
**Author:** [Kerkyra Dimisianou](https://github.com/kerkyradim)  
**Repository:** [kerkyradim/DataMining-](https://github.com/kerkyradim/DataMining-)

*Standalone Data Mining course assignment — separate from the MSc thesis repo.*

---

## What this project does

1. **Load & explore** the training set (`movies.xlsx`) and anonymous test set (`movies_test _anon.xlsx`).
2. **Clean & engineer features** — missing values, duplicates, column types, `%` and currency fields, multi-label **genre** encoding, date parsing.
3. **Train classifiers** on a binary Oscar-winner label (highly imbalanced):
   - **PyTorch** feed-forward network (section 3.2)
   - **Decision Tree** with custom **class weights** and **cross-validation** (section 3.3)
4. **Export test predictions** to `predictions_results.csv` (`id`, `prediction`).

The full workflow is in **`Data_mining_assignment.ipynb`**. The original submitted archive is kept as **`Assigment_Data_Mining.zip`**.

---

## Repository contents

| File | Description |
|------|-------------|
| `Data_mining_assignment.ipynb` | Main notebook (outputs cleared for GitHub) |
| `movies.xlsx` | Training dataset |
| `movies_test _anon.xlsx` | Test dataset (labels hidden) |
| `predictions_results.csv` | Model predictions on the test set |
| `Assigment_Data_Mining.zip` | Original assignment bundle (as submitted) |

---

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
jupyter lab Data_mining_assignment.ipynb
```

Place the Excel files in the repo root (already included). Run the notebook from top to bottom; section **3** builds models and produces predictions.

**Note:** The notebook imports **PyTorch** for the neural-network experiment. CPU is sufficient; GPU is optional.

---

## Tools & libraries

- **Python:** pandas, NumPy, Matplotlib, Seaborn  
- **ML:** scikit-learn (`train_test_split`, `DecisionTreeClassifier`, `Pipeline`, `StandardScaler`, `cross_validate`)  
- **Deep learning:** PyTorch (optional path in the assignment)

---

## License

Academic coursework — use for reference with attribution. Dataset terms depend on the course provider.
