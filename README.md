# 🎵 AI Music Genre Classifier

A user-friendly machine learning web app that predicts the **genre of a music track** based on pre-extracted audio features. Built using **Streamlit**, trained using the **GTZAN dataset**, and deployed online.

---

## 🚀 Live Demo

👉 [Click here to try the app](https://musicgenre-fxj97pxequravucf8jswam.streamlit.app/)  


---

## 💡 Features

- Upload a CSV file with extracted audio features
- Instantly predict the **genre** of the song (e.g., pop, rock, blues, classical)
- Simple interface – just upload and get results!
- Built using:
  - `pandas`, `joblib`, `sklearn`
  - Deployed with `Streamlit`

---

## 📁 Files in this Repo

| File                        | Description |
|----------------------------|-------------|
| `app.py`                   | Main Streamlit app |
| `music_genre_classifier.pkl` | Trained ML model |
| `test_samples.csv`         | Sample feature file for testing |
| `requirements.txt`         | All necessary Python packages |

---

## 🧠 Model Info

- Dataset: GTZAN genre classification dataset (pre-extracted features)
- Model: Random Forest Classifier
- Input: Audio features such as `chroma`, `rms`, `spectral_centroid`, etc.
- Output: Predicted **genre** label

---

## 📦 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/music-genre-classifier.git
   cd music-genre-classifier
<img width="1914" height="1025" alt="image" src="https://github.com/user-attachments/assets/8bf6c320-df4b-4cf7-ac91-a16a385e611d" />
