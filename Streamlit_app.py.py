import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
from collections import Counter
import pandas as pd
import re
from nltk.corpus import stopwords
import nltk

# Download stopwords if not already available
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load tokenizer and model for sentiment analysis
MODEL = "distilbert-base-uncased-finetuned-sst-2-english"  # Smaller model
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

# Set up Streamlit app configuration
st.set_page_config(page_title="Text Insight Hub", page_icon="🌟", layout="wide")
st.title("Sentiment Analysis")

# Sidebar for navigation and options
st.sidebar.title("Navigation")
st.sidebar.write("Choose an option below:")
option = st.sidebar.radio("", ["Single Text Analysis", "Bulk Text Analysis (CSV Upload)"])

# Instructions Section
with st.expander("How to use this app 📖"):
    st.write("""
        - Enter your text in the box below and click 'Analyze' to see the sentiment and word count.
        - You can upload a CSV file with text data for bulk analysis.
        - Make sure that the text column is the second column in your CSV file.
        - Look for Easter eggs hidden in special phrases! 🎉
    """)


# Function to perform sentiment analysis
def analyze_sentiment(text):
    encoded_text = tokenizer(text, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    
    # Adjusted for a model with only two outputs: negative and positive
    return {
        'Negative': round(scores[0] * 100, 2),
        'Positive': round(scores[1] * 100, 2)
    }


# Single Text Analysis
if option == "Single Text Analysis":
    default_text = """Hey guys! I’ve created this web app that performs sentiment analysis on your text. It will tell you the word count, most repeated word, and provide a summary of the text. There’s also an Easter egg for you! If you write "I love Chess," you'll get something interesting as the output. 😄"""
    input_text = st.text_area("📝 Enter your text:", value=default_text, height=200)

    if st.button("Analyze"):
        with st.spinner('Analyzing... 🕵️‍♂️'):
            try:
                lower_text = input_text.lower()

                if "abhinav" in lower_text:
                    st.write("Abhinav Katiyan is the one who created this web app. Here's a joke for you:")
                    st.write("What do you call an intelligent USA citizen?")
                    st.write("An immigrant! 😄")
                elif "i love chess" in lower_text:
                    st.write("🎉 Something interesting 🎉")
                else:
                    scores_dict = analyze_sentiment(input_text)
                    st.write(f"Sentiment Analysis: {scores_dict}")

                    words = [word for word in re.findall(r'\w+', input_text.lower()) if word not in stop_words]
                    word_counts = Counter(words)
                    if word_counts:
                        most_common_word, frequency = word_counts.most_common(1)[0]
                        st.write(f"Most common word: '{most_common_word}' used {frequency} times")

                    total_word_count = len(re.findall(r'\w+', input_text))
                    st.write(f"Total number of words (including stopwords): {total_word_count}")

                    if total_word_count > 300:
                        st.warning("⚠️ Caution: Your text is quite long! It may take a bit longer to process. ⚠️")
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Bulk Text Analysis
if option == "Bulk Text Analysis (CSV Upload)":
    st.subheader("Upload a CSV file containing your text data")

    # Provide a sample file download button
    sample_data = {
        'ID': [1, 2, 3],
        'Text': [
            "I love this product! It's amazing.",
            "I am not happy with the service.",
            "The experience was okay, nothing special."
        ]
    }
    sample_df = pd.DataFrame(sample_data)
    sample_csv = sample_df.to_csv(index=False).encode('utf-8')
    
    # Green download button for sample CSV
    st.download_button(label="📥 Download Sample CSV File", 
                       data=sample_csv,
                       file_name='sample_text_data.csv',
                       mime='text/csv',
                       key='download_sample_csv')

    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)

            # Check if there are at least two columns
            if df.shape[1] < 2:
                st.error("The CSV file should contain at least two columns, with the second column containing the text.")
            else:
                st.write("CSV uploaded successfully! Displaying the first few rows:")
                st.dataframe(df.head())

                # Initialize columns for sentiment scores
                df['Negative'] = 0.0
                df['Positive'] = 0.0

                # Apply sentiment analysis to each row in the second column
                for index, row in df.iterrows():
                    text = str(row.iloc[1])  # Convert to string in case of non-string values
                    sentiment_scores = analyze_sentiment(text)
                    df.at[index, 'Negative'] = sentiment_scores['Negative']
                    df.at[index, 'Positive'] = sentiment_scores['Positive']

                st.write("Sentiment analysis complete! Here are the results:")
                st.dataframe(df)

                # Provide an option to download the results
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(label="Download Results as CSV", data=csv,
                                   file_name='sentiment_analysis_results.csv', mime='text/csv')

        except Exception as e:
            st.error(f"An error occurred while processing the file: {e}")
