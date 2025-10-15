import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load the pre-processed data and models
try:
    with open('popularity_df.pkl', 'rb') as f:
        popularity_df = pickle.load(f)
    with open('pt.pkl', 'rb') as f:
        pt = pickle.load(f)
    with open('books.pkl', 'rb') as f:
        books = pickle.load(f)
    with open('similarity_scores.pkl', 'rb') as f:
        similarity_scores = pickle.load(f)
except FileNotFoundError:
    st.error("Model files not found. Please run the data processing script first.")
    st.stop()


# --- Streamlit App ---

st.set_page_config(page_title="Book Recommender System", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    /* Main background */
    .main {
        background-color: #F5F5F5;
    }

    /* --- Heading and Title Styling --- */
    h1, h2 {
        color: #333333;
        text-align: center;
    }

    /* --- Book Card Styling --- */
    .book-card {
        background-color: white;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.2s;
        color: #333333; 
    }
    .book-card:hover {
        transform: scale(1.05);
    }
    .book-title {
        font-size: 1rem;
        font-weight: bold;
        margin-top: 0.5rem;
    }
    .book-author {
        font-size: 0.9rem;
        color: #555;
    }
    .book-image {
        width: 100%;
        max-width: 150px;
        height: auto;
        border-radius: 5px;
        margin-bottom: 0.5rem;
    }

    /* --- Tab Styling --- */
    /* Unselected tab */
    .st-emotion-cache-12w0qpk button {
        color: #4F4F4F; /* <-- Darker grey for unselected tab text */
        font-weight: bold;
    }
    /* Selected tab */
    .st-emotion-cache-12w0qpk button[aria-selected="true"] {
        color: #FFFFFF; 
        background-color: #C71585;
        font-weight: bold;
    }

</style>
""", unsafe_allow_html=True)


st.title("📚 Book Recommender System")

# --- Tabs for different sections ---
tab1, tab2 = st.tabs(["Top 50 Books (Popularity)", "Recommend Books (Collaborative)"])

with tab1:
    st.header("Top 50 Most Popular Books")
    
    # Display top 50 books in a grid
    cols = st.columns(5)
    for i in range(50):
        with cols[i % 5]:
            card = popularity_df.iloc[i]
            st.markdown(f"""
            <div class="book-card">
                <img src="{card['Image-URL-M']}" class="book-image" alt="Book Cover">
                <div class="book-title">{card['title']}</div>
                <div class="book-author">{card['author']}</div>
                <div>Votes: {card['num_ratings']}</div>
                <div>Rating: {card['avg_ratings']:.2f}</div>
            </div>
            """, unsafe_allow_html=True)


with tab2:
    st.header("Get Book Recommendations")
    
    # User input: select a book
    book_list = pt.index.values
    selected_book = st.selectbox("Type or select a book you like:", book_list)

    if st.button("Recommend"):
        if selected_book:
            try:
                # Recommendation logic
                book_index = np.where(pt.index == selected_book)[0][0]
                similar_items = sorted(list(enumerate(similarity_scores[book_index])), key=lambda x: x[1], reverse=True)[1:6]

                st.subheader(f"Recommendations for '{selected_book}':")
                
                rec_cols = st.columns(5)
                for i, item in enumerate(similar_items):
                    with rec_cols[i]:
                        temp_df = books[books['title'] == pt.index[item[0]]]
                        rec_book_title = temp_df.drop_duplicates('title')['title'].values[0]
                        rec_book_author = temp_df.drop_duplicates('title')['author'].values[0]
                        rec_book_image = temp_df.drop_duplicates('title')['Image-URL-M'].values[0]

                        st.markdown(f"""
                        <div class="book-card">
                            <img src="{rec_book_image}" class="book-image" alt="Book Cover">
                            <div class="book-title">{rec_book_title}</div>
                            <div class="book-author">{rec_book_author}</div>
                        </div>
                        """, unsafe_allow_html=True)

            except IndexError:
                st.error(f"Could not find recommendations for '{selected_book}'. It might not have enough data.")
        else:
            st.warning("Please select a book.")
