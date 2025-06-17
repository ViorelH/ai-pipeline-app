from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

# Loading model
with open("model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

class Message(BaseModel):
    text: str

@app.post("/predict")
async def predict(msg: Message):
    X = vectorizer.transform([msg.text])
    prediction = model.predict(X)[0]
    return {"spam": bool(prediction)}
