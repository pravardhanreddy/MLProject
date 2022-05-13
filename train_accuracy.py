import numpy as np
import matplotlib.pyplot as plt

x = [0.25,0.5,0.75,1]
y = [95.8, 95.7, 95.4, 98.1]
z= [86.1, 86.0, 86.4, 85.9]

X_axis = np.arange(len(x))

fig, ax = plt.subplots(figsize=(8,8))

rects1 = plt.bar(X_axis - 0.1, y, 0.2, label = 'Validation_accuracy')
rects2 = plt.bar(X_axis + 0.1, z, 0.2, label = 'Test_accuracy')

plt.bar_label(rects1, padding=3)
plt.bar_label(rects2, padding=3)

plt.xticks(X_axis, x)
plt.xlabel("Training size")
plt.ylabel("Percentage")
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)
plt.show()

