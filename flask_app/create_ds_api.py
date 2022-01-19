"""
Ref : https://faculty.ai/blog/creating-data-science-apis-with-flask/
"""
# Import Modules
from flask import Flask
from flask import jsonify
import numpy as np
import json
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!\n'

@app.route('/foo')
def foo():
    return 'bar\n'

@app.route('/hi/<name>')
def hi(name):
    return 'Hi {}\n'.format(name)

# Example Convert Text to Json
@app.route('/api')
def api():
    data = {
            'name':'Andrew',
            'user':'acroz'
            }
    return jsonify(data)

# Example Convert Numpy Values to Json
@app.route('/json_numpy')
def json_numpy():
    array1 = np.array([1,2,3,4])
    return json.dumps([float(v) for v in array1])

# Wrapping DS Models
X, y = make_classification(
        n_samples=100,
        n_features=2,
        n_classes=2,
        n_informative=2,
        n_redundant=0
        )
@app.route('/predict/feature_1/<feature_1>/feature_2/<feature_2>')
def predict(feature_1, feature_2):
    # Instantiate & Fit Model
    model = LogisticRegression()
    model.fit(feature_1, feature_2)
    # Convert input values from string to floats
    features = np.array([[feature_1, feature_2]])
    predicted_class = model.predict(features)[0]
    probabilities = model.predict_proba(feature)[0]

    # Prepare Response
    content = {
            'class':int(predicted_class),
            'probabilities':[
                float(p) for p in probabilities]
            }
    return jusonify(content)



# When script run as main, run app

if __name__ == '__main__':
        app.run(debug=True)
