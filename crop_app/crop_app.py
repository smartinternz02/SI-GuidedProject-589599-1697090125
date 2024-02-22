from flask import Flask, render_template, request
import pickle
import pandas as pd


app = Flask(__name__)

# Load the model
model = pickle.load(open('C:\\Users\\sarvu\\Desktop\\crop_app\\model.pkl', 'rb'))

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
     Nitrogen=float(request.form['Nitrogen'])
     Phosphorus=float(request.form['Phosphorus'])
     Potassium=float(request.form['Potassium'])
     Temperature=float(request.form['Temperature'])
     Humidity=float(request.form['Humidity'])
     Ph=float(request.form['ph'])
     Rainfall=float(request.form['Rainfall'])
     
    values=[Nitrogen,Phosphorus,Potassium,Temperature,Humidity,Ph,Rainfall]
    prediction = model.predict(pd.DataFrame([[Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]], columns=['Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 'Humidity', 'Ph', 'Rainfall']))

        # You can do something with the prediction here

    return render_template('crop_predict.html', prediction=prediction[0])

if __name__ == "__main__":
    app.debug = True  # Enable debugging mode
    app.run()

    

