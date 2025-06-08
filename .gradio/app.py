import gradio as gr
import numpy as np
from src.model import load_data, build_and_train
from keras.models import load_model

# Load and train or load existing model
X, y, scaler = load_data('data/apple_stock.csv')
model = build_and_train(X, y)  # or model = load_model('lstm_model.h5')

def predict_future(days: int):
    seq = X[-1]
    preds = []
    for _ in range(days):
        p = model.predict(seq.reshape(1, seq.shape[0], 1))[0][0]
        preds.append(p)
        seq = np.append(seq[1:], [[p]], axis=0)
    return scaler.inverse_transform(np.array(preds).reshape(-1,1)).flatten().tolist()

gr.Interface(fn=predict_future,
             inputs=gr.Slider(1, 60, label="Days to Predict"),
             outputs="chart").launch()
