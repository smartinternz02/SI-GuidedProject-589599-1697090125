from flask import Flask, render_template, request
import pickle
import pandas as pd



app = Flask(__name__)

# Load the model
model = pickle.load(open('C:\\Users\\kapil\\Desktop\\rakesh\\model.pkl', 'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/details')
def pred():
    return render_template('details.html')

@app.route('/Crop_predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get input data from the form
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Make a prediction using the loaded model
        prediction = model.predict(pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]], columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']))

        # You can do something with the prediction here

        return render_template('result.html', prediction=prediction[0])

    return render_template('crop_predict.html')

if __name__ == "__main__":
    app.debug = True  # Enable debugging mode
    app.run()