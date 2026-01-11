# HarmonySales-Music-Analysis-
Streamlit Application

<p align="center">
    <img src="icons/icon1.png" alt="Music Icon" width="60" height="60">
</p>

<h2 align="center"><strong>HarmonySales Music Analysis - Streamlit Application</strong></h2>


### 📜 Description

This interactive application helps a music production company determine which music style maximizes sales. It includes a homepage and a dashboard with insightful visualizations.


### 💡 Key Features

- Discover the popularity of different music genres.
- Analyze characteristics like energy, danceability, and tempo by genre.
- Gain insights to make data-driven decisions in the music industry.


---
### 🛠️ How to Install and Run

#### 1. Clone the repository
```bash
  git clone https://github.com/SamarKri/HarmonySales.git

  cd HarmonySales/TP2-Musical  
```

#### 2. Install dependencies using Poetry
```bash
  poetry install

  If you encounter dependency issues, try reinstalling the dependencies :
  poetry install --no-cache

  An alternative to Poetry (pip install -r requirements.txt)
```

#### 3. Activate the virtual environment
```bash
  poetry shell

  If you encounter issues, try : poetry env activate
```

#### 4. Run the application
```bash
  streamlit run app.py
```

#### 5. You can now view your Streamlit app in your browser.
```bash
  Local URL: http://localhost:8501

  Network URL: http://192.168.1.134:8501
```

---
### 📌Prerequisites

- Python 3.12.6+
- [Poetry](https://python-poetry.org/) for dependency management.
- Hugging Face Dataset: [Spotify Tracks Dataset](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset)

### 🎯 Dependencies

- Pandas
- Seaborn
- Matplotlib
- Poetry
- Sphinx
- Streamlit

### 🔑 Languages

- Python
- JavaScript
- CSS 
- HTML 

### 🌍 Deployment
You can deploy the app on platforms like Hugging Face Spaces or Streamlit Cloud.
```bash
Open your web browser and go to : https://harmony-sales.streamlit.app/
```
---

### 📂 Project Structure

```plaintext
HarmonySales/
│── _build/                 # Files generated after compiling the documents
│   ├── doctrees/           # Temporary files for Sphinx
│   ├── html/               # Generated HTML files
│── .vscode/                # VS Code specific configuration
│── icons/                  # Contains icons in the Readme
│── ScreenShots/            # Contains images that showcase key features of the application
│── TP2-Musical/            # Main folder for the TP2 music assignment
│   ├── data/               # Contains the datasets
│   │   ├── musical_dataset.ipynb            # Analysis data exploring genres, popularity, and tempo
│   │   ├── Spotify_HuggingFace_Dataset.csv  # Musical dataset
│   ├── app.py               # Main file for the Streamlit application
│   ├── requirements.txt     # List of dependencies (alternative to Poetry)
│── .gitignore               # Files to exclude from Git tracking
│── conf.py                  # Sphinx configuration file
│── index.rst                # Sphinx indexing file
│── make.bat                 # Build script for Windows
│── Makefile                 # Build script for Unix/Linux
│── poetry.lock              # Dependency version lock file for Poetry
│── pyproject.toml           # Project configuration file for Poetry
│── README.md                # Project documentation
```
