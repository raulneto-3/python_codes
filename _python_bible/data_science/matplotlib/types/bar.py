import numpy as np
import matplotlib.pyplot as plt

bob = (90, 67, 87, 76)
charles = (80, 80, 47, 66)
daniel = (40, 95, 76, 89)
skills = ("Python", "Java", "Networking", "Machine Learning")

width = 0.2
index = np.arange(4)
plt.bar(index, bob,width=width, label="Bob")
plt.bar(index + width, charles, width=width, label="Charles")
plt.bar(index + width * 2, daniel,width=width, label="Daniel")

plt.xticks(index + width, skills)
plt.ylim(0,120)
plt.title("IT Skill Levels")
plt.ylabel("Skill Level")
plt.xlabel("IT Skill")
plt.legend()
plt.show()