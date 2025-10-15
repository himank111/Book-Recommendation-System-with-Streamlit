# 📚 Book Recommendation System (Streamlit)

An interactive **Book Recommendation System** built using **Streamlit**.  
The app recommends books based on **popularity** and **item-based collaborative filtering**.  
It features a clean dashboard with tabs for both recommendation modes, styled using custom CSS.

---

## 📌 Overview
This project demonstrates a simple **content-based recommender** deployed as a web app.  
It uses pre-computed data (stored in `.pkl` files) and provides:
- **Top 50 most popular books** with their ratings and vote counts  
- **Personalized book recommendations** based on similarity between items  

---

## ⚙️ Features
- 🏆 **Top 50 Books (Popularity)** → displays most-liked books in a grid  
- 🤝 **Collaborative Filtering** → recommends similar books for a selected title  
- 🎨 **Custom UI** → cards, hover animations, and themed colors  
- ⚠️ **Graceful error handling** → detects missing model files  

---

## 🧠 How It Works

### 1️⃣ Popularity-Based Recommender
Displays top 50 books ranked by **average rating** and **vote count**.

### 2️⃣ Collaborative Filtering
- User selects a book title  
- App finds similar books using **cosine similarity** from `similarity_scores.pkl`  
- Shows **top 5 similar books** with title, author, and image  

---

## 🧰 Tech Stack
- **Frontend:** Streamlit  
- **Data Handling:** pandas, numpy  
- **Similarity:** scikit-learn (cosine similarity)  
- **Storage:** Pickle (`.pkl` files)

---
