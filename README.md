# Sentiment-Analysis-Web-App
Text Insight Hub - Sentiment Analysis App
Overview
The Text Insight Hub is an interactive web-based application that allows users to analyze the sentiment of text data using a pre-trained transformer model. Built using Streamlit, it provides an intuitive interface for both single text and bulk CSV text analysis. The app performs sentiment analysis and also provides word frequency and word count information.

Features
Single Text Analysis:

Analyze individual text input to get insights like sentiment breakdown (positive/negative), word count, and the most frequently used words.
The app includes hidden "Easter eggs" triggered by specific phrases for a fun user experience.
Bulk Text Analysis (CSV Upload):

Upload a CSV file containing multiple text entries and receive sentiment analysis results for each entry.
Sentiment scores for both positive and negative sentiment are displayed.
Download the processed results as a CSV file after analysis.
How to Use
Single Text Analysis:

Enter text in the provided text area.
Click on the "Analyze" button to get sentiment results along with word count and the most common word.
Special responses are triggered when you input certain phrases like "I love Chess" or "Abhinav."
Bulk Text Analysis (CSV Upload):

Upload a CSV file where the second column contains the text for sentiment analysis.
View the sentiment analysis results for each row and download the output as a CSV file.
Example Use Cases
Customer Feedback Analysis: Evaluate the overall sentiment of customer reviews.
Social Media Monitoring: Assess public sentiment regarding a product, event, or campaign.
Bulk Text Analysis: Process large datasets of textual data to extract sentiment trends and common word usage patterns.
Sentiment Output
The sentiment is categorized into Positive and Negative scores, presented as percentages.
Additional insights such as word frequency and total word count are provided.
Special Easter Eggs
The app contains some surprises! If you input specific phrases like "I love Chess" or mention the name "Abhinav," you will receive unique responses. Try it out for a fun twist!
Requirements
Input text manually for single analysis or upload a CSV for bulk analysis.
The app processes sentiment in English, using a transformer model fine-tuned for this task.
Download Results
After performing bulk text analysis, users can download the sentiment results as a CSV file, making it easy to integrate with further analyses or reporting tools.
