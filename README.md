# StockPricePrediction Using AI

StockPricePrediction is an advanced tool leveraging Artificial Intelligence to forecast stock prices with higher accuracy. It incorporates state-of-the-art machine learning models and data analysis techniques to help users, investors, and researchers make informed decisions in the stock market.

## 🚀 Features

- **AI-Powered Predictions**: Utilizes machine learning and deep learning models (such as LSTM, GRU, or Transformer-based architectures) for time series forecasting of stock prices.
- **Historical Data Analysis**: Automatically fetches and processes historical stock data for robust predictions.
- **Interactive Visualizations**: Provides clear and interactive plots for price trends, model predictions vs actual, and performance metrics.
- **Customizable Parameters**: Users can adjust model parameters, select different stocks, date ranges, and input features.
- **Multiple Data Sources**: Supports a variety of data sources (Yahoo Finance, Alpha Vantage, etc.) for flexibility and better accuracy.
- **Evaluation Metrics**: Displays key performance indicators like RMSE, MAE, and R² for model evaluation.
- **Backtesting**: Simulate trading strategies based on the predicted prices to assess potential profitability.
- **User-Friendly Interface**: Easy-to-use interface, suitable for both technical and non-technical users.
- **Extensible Design**: Modular codebase allowing easy integration of new models or data sources.

## 🛠️ Technologies Used

- Python 3.x
- Machine Learning Libraries: TensorFlow, Keras, PyTorch, Scikit-learn
- Data Handling: Pandas, NumPy(pip install numpy)
- OpenCV(pip install opencv-python)
- Visualization: Matplotlib, Plotly, Seaborn
- Data Sourcing: yfinance, Alpha Vantage API

##You can find the dataset via the link below

https://www.kaggle.com/datasets/tarunpaparaju/apple-aapl-historical-stock-data

## 📈 Example Workflow

1. **Select Stock & Time Period**: Enter ticker symbol and date range.
2. **Fetch & Preprocess Data**: The tool retrieves and cleans historical price data.
3. **Train Model**: Fits an AI model to historical data.
4. **Predict**: Model forecasts stock prices for user-specified future dates.
5. **Visualize & Evaluate**: Shows prediction plots and evaluation metrics.

## 📊 Sample Visualization

https://drive.google.com/file/d/1CfUsDYkqJJHDdLBeQGTVSGL6se4KPWHH/view?usp=drivesdk

## 🔧 How it Runs:

1. Clone this repository:
   
   git clone https://github.com/yourusername/StockPricePrediction.git
   cd StockPricePrediction
  
2. Install dependencies:

   pip install -r requirements.txt
 
3. Run the application:
  
   python StockPricePrediction.py
   
   --A graph will be displayed showing Predicted vs Actual stock prices
   
5. To Get the Gradio UI Output (prediction via web app):
   
   Navigate to src/ folder:

cd src

6. Run the Gradio app:

python app.py

✅ A link will appear — open it in your browser

Choose days using slider and click Submit to get the predicted prices in a table


## Screenshots


![Screenshot 2025-06-08 173753](https://github.com/user-attachments/assets/07f40715-6bdc-44ab-8c13-8b1931fd99ac)

![Screenshot 2025-06-10 233620](https://github.com/user-attachments/assets/c2633a99-953c-403d-84b5-12311e45b7d5)

![Screenshot 2025-06-10 233558](https://github.com/user-attachments/assets/e9829226-0d4c-481b-82b4-6c7f5a9aeb8b)

## Created by
Niharika Dharmana - CSE[AI & ML]






