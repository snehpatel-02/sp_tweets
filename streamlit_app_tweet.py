import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Airline Tweets Dashboard", layout="wide")

st.title("✈️ Airline Tweets Sentiment Analysis")

# Load dataset
url = 'https://raw.githubusercontent.com/snehpatel-02/sp_tweets/refs/heads/main/Tweets.csv'

@st.cache_data
def load_data():
    df = pd.read_csv(url)
    return df

tweets = load_data()

st.subheader("Dataset Preview")
st.dataframe(tweets.head())

# Pie chart of sentiment
st.subheader("Sentiment Distribution")

sentiment_counts = tweets['airline_sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['sentiments', 'count']

fig_pie = px.pie(sentiment_counts, values='count', names='sentiments', title='Count of Tweets by Sentiment')
st.plotly_chart(fig_pie, use_container_width=True)

# Bar chart of tweet counts by airline
st.subheader("Tweet Count by Airline")

airline_counts = tweets['airline'].value_counts().reset_index()
airline_counts.columns = ['airline', 'count']

fig_bar, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='airline', y='count', hue='airline', palette='pastel', data=airline_counts, legend=False)
ax.set_xlabel('Airline')
ax.set_ylabel('Count')
ax.set_title('Count of Tweets by Airline')
st.pyplot(fig_bar)
