from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# załadowanie przykładowego modelu AI - regresja liniowa
try:
    model = joblib.load('model.pkl')
except:
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit([[0], [1], [2], [3]], [0, 1, 2, 3])  # Prosty model uczący się zależności y=x
    joblib.dump(model, 'model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # pobranie danych JSON
        data = request.get_json()
        values = data['values']

        # konwersja danych do tablicy NumPy
        input_data = np.array(values).reshape(-1, 1)

        # predykcja wyników
        predictions = model.predict(input_data)

        # zwrot odpowiedzi JSON
        return jsonify({'predictions': predictions.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)})

# endpoint testowy
@app.route('/', methods=['GET'])
def home():
    return "AI Prediction Service is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
