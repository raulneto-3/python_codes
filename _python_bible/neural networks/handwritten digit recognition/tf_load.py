import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

model = tf.keras.models.load_model('neural networks/handwritten digit recognition/digit_recognition.model')

img = cv2.imread('neural networks/handwritten digit recognition/1.png')[:,:,0]
img = np.invert(np.array([img]))
prediction = model.predict(img)
print(f'The result is probably: {np.argmax(prediction)}')
plt.imshow(img[0])
plt.show()