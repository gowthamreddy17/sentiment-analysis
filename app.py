from flask import Flask, render_template, request
import os
import pickle
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Get the absolute path to the directory containing your Flask application
base_dir = os.path.abspath(os.path.dirname(__file__))

# Define the absolute path to the model.pkl file
model_path = os.path.join(base_dir, 'model.pkl')

# Define the absolute path to the vectorizer.pkl file
vectorizer_path = os.path.join(base_dir, 'vectorizer.pkl')

# Load the model and vectorizer
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

with open(vectorizer_path, 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

def predict_sentiment(text):
    # Vectorize the text
    text_vectorized = vectorizer.transform([text])
    # Predict sentiment
    prediction = model.predict(text_vectorized)
    return prediction[0]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        review = request.form['review']
        prediction = predict_sentiment(review)
        return render_template('result.html', prediction=prediction)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
