from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np

data = load_breast_cancer()

X = data.data
Y = data.target

# random_state=30: seed
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=30) 
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

model = SVC(kernel='linear', C=3)
model.fit(X_train, Y_train)

accuracy = model.score(X_test, Y_test)
print(accuracy)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)

knn_accuracy = knn.score(X_test, Y_test)
print(knn_accuracy)
