from flask import Flask, request, jsonify
from warnings import filterwarnings
import pickle

filterwarnings('ignore')

def importa_modelo():
    modelo = pickle.load(open('./projects/APP/modelo.pkl', 'rb'))
    return modelo

app = Flask(__name__)

modelo = importa_modelo()

@app.route('/predict', methods=['Post'])
def home():
    dados_post = request.get_json()
    dados = [dados_post[i] for i in ['Pregnancies',
                                     'Glucose', 'BloodPressure', 'Insulin', 'BMI', 'Age']]
    resultado = modelo.predict([ dados ])[0]
    print (dados)

    return jsonify(resultado = str(resultado))

app.run(
    debug=True,
    port='5000'
)
