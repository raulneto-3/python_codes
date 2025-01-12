import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer 

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

data = load_breast_cancer()
X = np.array(data.data)
Y = np.array(data.target)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

clf1 = KNeighborsClassifier(n_neighbors=5)
clf2 = GaussianNB()
clf3 = LogisticRegression()
clf4 = DecisionTreeClassifier()
clf5 = RandomForestClassifier()

clf1.fit(X_train, Y_train)
clf2.fit(X_train, Y_train)
clf3.fit(X_train, Y_train)
clf4.fit(X_train, Y_train)
clf5.fit(X_train, Y_train)

accuracy1 = clf1.score(X_test, Y_test)
accuracy2 = clf2.score(X_test, Y_test)
accuracy3 = clf3.score(X_test, Y_test)
accuracy4 = clf4.score(X_test, Y_test)
accuracy5 = clf5.score(X_test, Y_test)

print(f"KNeighborsClassifier: {accuracy1}")
print(f"GaussianNB: {accuracy2}")
print(f"LogisticRegression: {accuracy3}")
print(f"DecisionTreeClassifier: {accuracy4}")
print(f"RandomForestClassifier: {accuracy5}")

## Predict
# X_new = np.array([[...]])
# Y_new = clf1.predict(X_new)