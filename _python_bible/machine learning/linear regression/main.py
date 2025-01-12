import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('python_bible/4 - machine learning/student-mat.csv', sep=';')
data = data[['age', 'sex', 'studytime', 'absences', 'G1', 'G2', 'G3']]
data['sex'] = data['sex'].map({'F': 0, 'M': 1})
predict = 'G3'

# Prepare data
X = np.array(data.drop(columns=[predict]))
Y = np.array(data[predict])
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

# Train model
model = LinearRegression()
model.fit(X_train, Y_train)
accuracy = model.score(X_test, Y_test)
print(accuracy)

# Predict
X_new = np.array([[18, 1, 3, 40, 15, 16]])
Y_new = model.predict(X_new)
print(Y_new)

# In this case, the final grade would probably be 17.
# Nesse caso, a nota final provavelmente seria 17.

# Visualize 
plt.scatter(data['studytime'], data['G3'])
plt.title("Correlation")
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
plt.show()

plt.scatter(data['G2'], data['G3'])
plt.title("Correlation")
plt.xlabel("Second Grade")
plt.ylabel("Final Grade")
plt.show()
