import pickle
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

data = load_breast_cancer()
X = data.data
Y = data.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

# Load the model
with open('4 - machine learning/optmizing/model.pickle', 'rb') as file:
    model = pickle.load(file)
    prediction = model.predict(X_test)

    print(f'Prediction: {prediction}')
    print(f'Actual: {Y_test}')
    print(f'Score: {model.score(X_test, Y_test)}')