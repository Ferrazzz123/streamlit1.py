import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("Asimov/customer reviews.csv")
df_top100 = pd.read_csv("Asimov/Top-100 Trending Books.csv")

books = df_top100["book title"].unique()
book = st.sidebar.selectbox("Books", books)

df_book = df_top100[df_top100["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book["book price"].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)
col1, col2, col3 = st.columns(3)

col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year)

st.divider()

for line in df_reviews_f.values:
    message = st.chat_message(f"{line[4]}")
    message.write(f"**{line[2]}**")
    message.write(line[5])




