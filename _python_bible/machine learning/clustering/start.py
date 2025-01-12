from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.preprocessing import scale

digits = load_digits()
data = scale(digits.data)

## Training 
# clf = KMeans(n_clusters=10, init='k-means++', n_init=10) # inteligente
clf = KMeans(n_clusters=10, init='random', n_init=10)
clf.fit(data)


## Predict
