import joblib

def predict_diabetes(input):
    model = joblib.load('saved/dmodel_diabetes.pkl')

    result = model.predict(input)

    return result