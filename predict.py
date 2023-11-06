#Loading the model
import pickle
import numpy as np

from flask import Flask, request, jsonify

#predict function
def predict_f(df, dv, model):
        X_df = dv.transform(df)

        y_pred = model.predict(X_df)
        return y_pred

with open('drunk_or_not.bin', 'rb') as file_in:
    dv, model = pickle.load(file_in)

sobriety_test = Flask('sob_testing')

@sobriety_test.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    make_prediction = predict_f(customer, dv, model)

    if make_prediction == 1:
        sobriety_result = {"Sobriety test result": 'Drunk'}
    else:
         sobriety_result = {"Sobriety test result": 'Sober'}
    return jsonify(sobriety_result)




if __name__ == '__main__':
     sobriety_test.run(debug=True, host='0.0.0.0', port=9696)