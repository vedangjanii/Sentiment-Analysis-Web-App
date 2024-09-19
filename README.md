# Sentiment-Analysis-Web-App


    <h2>Overview</h2>
    <p>
        The <strong>Text Insight Hub</strong> is an interactive web-based application that allows users to analyze the sentiment of text data using a pre-trained transformer model. Built using <strong>Streamlit</strong>, it provides an intuitive interface for both single text and bulk CSV text analysis. The app performs sentiment analysis and also provides word frequency and word count information.
    </p>

    <h2>Features</h2>
    <ul>
        <li><strong>Single Text Analysis:</strong>
            <ul>
                <li>Analyze individual text input to get insights like sentiment breakdown (positive/negative), word count, and the most frequently used words.</li>
                <li>The app includes hidden "Easter eggs" triggered by specific phrases for a fun user experience.</li>
            </ul>
        </li>
        <li><strong>Bulk Text Analysis (CSV Upload):</strong>
            <ul>
                <li>Upload a CSV file containing multiple text entries and receive sentiment analysis results for each entry.</li>
                <li>Sentiment scores for both positive and negative sentiment are displayed.</li>
                <li>Download the processed results as a CSV file after analysis.</li>
            </ul>
        </li>
    </ul>

    <h2>How to Use</h2>
    <ol>
        <li><strong>Single Text Analysis:</strong>
            <ul>
                <li>Enter text in the provided text area.</li>
                <li>Click on the "Analyze" button to get sentiment results along with word count and the most common word.</li>
                <li>Special responses are triggered when you input certain phrases like "I love Chess" or "Abhinav."</li>
            </ul>
        </li>
        <li><strong>Bulk Text Analysis (CSV Upload):</strong>
            <ul>
                <li>Upload a CSV file where the second column contains the text for sentiment analysis.</li>
                <li>View the sentiment analysis results for each row and download the output as a CSV file.</li>
            </ul>
        </li>
    </ol>

    <h2>Example Use Cases</h2>
    <ul>
        <li><strong>Customer Feedback Analysis:</strong> Evaluate the overall sentiment of customer reviews.</li>
        <li><strong>Social Media Monitoring:</strong> Assess public sentiment regarding a product, event, or campaign.</li>
        <li><strong>Bulk Text Analysis:</strong> Process large datasets of textual data to extract sentiment trends and common word usage patterns.</li>
    </ul>

    <h2>Sentiment Output</h2>
    <p>
        The sentiment is categorized into <strong>Positive</strong> and <strong>Negative</strong> scores, presented as percentages. Additional insights such as word frequency and total word count are provided.
    </p>

    <h2>Special Easter Eggs</h2>
    <p>
        The app contains some surprises! If you input specific phrases like "I love Chess" or mention the name "Abhinav," you will receive unique responses. Try it out for a fun twist!
    </p>

    <h2>Requirements</h2>
    <p>
        Input text manually for single analysis or upload a CSV for bulk analysis. The app processes sentiment in English, using a transformer model fine-tuned for this task.
    </p>

    <h2>Download Results</h2>
    <p>
        After performing bulk text analysis, users can download the sentiment results as a CSV file, making it easy to integrate with further analyses or reporting tools.
    </p>
</body>
</html>
