# 📥 HydroFetch : A Python-based Web-scrapping application for Big Hydrologic Data Extraction

This project automates the process of selecting stations and downloading groundwater data and metadata from the **[India WRIS](https://indiawris.gov.in/wris/#/timeseriesdata)** portal using Selenium and PyAutoGUI.

---

## 🔧 Features

### 1. Automatic Station Selection & Deselection

* Dynamically opens and controls Angular-based dropdown menus.
* Selects and deselects stations programmatically.

### 2. Data & Metadata Downloads

* Triggers both `Download Data` and `Download Metadata` buttons.
* Submits metadata request forms automatically with user input.

### 3. OS-level Dialog Handling

* Uses **PyAutoGUI** to handle native OS-level dialogs (like "Save As" prompts).
* Automatically clicks the "Save" button to initiate downloads without user interference.

### 4. Virtual Environment Ready

* Designed to work inside a **Python virtual environment**.
* Ensures clean dependency management and project isolation.

---

## 📁 Project Structure

```
.
├── main.py                  # Main script
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🚀 How to Run

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/automated-wris-downloader.git
cd automated-wris-downloader
```

2. **Set up a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the script**

```bash
python main.py
```

---

## 📌 Notes

* This script requires Google Chrome or Brave and a pre-configured Selenium user profile.
* The Save dialog interaction is calibrated for specific screen resolutions. Adjust `pyautogui.moveTo(x, y)` if needed.
* Best used with stations where manual download is tedious and repetitive.

---

## 🤖 Tech Stack

* **Python 3.x**
* **Selenium** for browser automation
* **PyAutoGUI** for OS-level UI control

---

## 📬 Contact

For improvements or queries, feel free to reach out or create an issue.

---

> ⚠️ This tool is intended for educational and research purposes only.
