from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Sample spam dataset
X_train = [
    "Win money now", "Free prize", "Call this number now",
    "Hello, how are you?", "Let's meet tomorrow", "See you later"
]
y_train = [1, 1, 1, 0, 0, 0]

# Train model
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X_train)
model = MultinomialNB()
model.fit(X_vectorized, y_train)

# Save model & vectorizer
with open("app/model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("Model trained and saved to app/model.pkl")
