import numpy as np
import matplotlib.pyplot as plt

labels = ('American', 'German', 'French', 'Other')
values = (47, 23, 20, 10)

plt.pie(values,labels=labels, autopct="%.2f%%", shadow=True)
plt.title("Student Nationalities")
plt.show()
