# ✨ DataSnap – Interactive Data Validation & Reporting Engine

**DataSnap** is a lightweight Python-based engine created to detect data inconsistencies and generate dynamic, interactive HTML reports using Sweetviz.

Crafted with ❤️ by **Vaishnavii S**

---

## 🚀 Features

- Detects columns with inconsistent or mixed data types
- Reports missing/null value distributions across columns
- Provides correlation matrix for numeric features
- Automatically generates a shareable HTML profiling report
- Scales well with datasets having **10M+ rows** and **250+ columns**
- Designed for **QA teams, data validation, and ETL testing**

---

## 🛠️ Setup & Usage

### 1. Install dependencies

```bash
pip install pandas matplotlib sweetviz
```

---

### 2. Provide your dataset path

Download or place your `.csv` file in a folder and update the path in the script:

```python
csv_path = "data/your_data_file.csv"
```

---

### 3. Run the script

Execute the Python script using the following command:

```bash
python detect_data_shift_correct_new.py
```

---

### 📊 Output

**Console Output:**

- Initial inspection (head, info)
- Inconsistent data types across columns
- Null value counts per column
- Value distribution per column
- Correlation matrix of numeric fields

---

**📝 HTML Report:**

- Automatically saved as: `your_report.html`
- Can be opened in **any browser** for detailed exploration

---

### ⚙️ Built With

- Python 🐍  
- Pandas  
- Matplotlib  
- NumPy  
- Sweetviz
