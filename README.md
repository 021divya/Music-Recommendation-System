# 🎵 Music Recommendation System

## 📌 Project Overview

This project is a **Music Recommendation System** that suggests songs similar to a selected song based on lyrical content.
The system uses **Natural Language Processing (NLP)** and **Cosine Similarity** to find songs with similar lyrics.

A simple and interactive **Streamlit web application** allows users to select a song and receive recommendations along with album cover images fetched from the **Spotify API**.

---

## 🚀 Features

* Select any song from the dropdown list
* Get **Top 5 recommended songs**
* Displays **album cover images**
* Uses **Spotify API** for fetching song artwork
* Interactive **Streamlit web interface**

---

## 🛠 Technologies Used

* **Python**
* **Streamlit** – for building the web interface
* **Pandas & NumPy** – for data processing
* **Scikit-learn** – for TF-IDF vectorization and cosine similarity
* **Spotipy (Spotify API)** – for fetching album artwork

---

## 📂 Dataset

The dataset used is **spotify_millsongdata.csv**, which contains song lyrics and metadata.

Main attributes include:

* Song title
* Artist
* Lyrics

---

## ⚙️ How the System Works

1. The dataset containing song lyrics is loaded.
2. Lyrics are converted into numerical vectors using **TF-IDF Vectorization**.
3. **Cosine Similarity** is computed between all songs.
4. When a user selects a song:

   * The system finds the similarity scores.
   * The **top 5 most similar songs** are recommended.

---

## 📁 Project Structure

```
music-recommendation-system
│
├── app.py                     # Streamlit application
├── df.pkl                     # Processed dataset
├── similarity.pkl             # Similarity matrix
├── spotify_millsongdata.csv   # Original dataset
├── model_training.ipynb       # Model training notebook
├── requirements.txt           # Required libraries
└── README.md                  # Project documentation
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/music-recommendation-system.git
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the application

```
streamlit run app.py
```

### 4️⃣ Open in browser

```
http://localhost:8501
```


