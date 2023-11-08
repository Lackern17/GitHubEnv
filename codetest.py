# code to create an array

import numpy as np

a = np.array([2, 3, 4])

print('This is an array')
print(a)

# code to create a dataframe

import pandas as pd

df = pd.DataFrame({'num_legs': [2, 4, 8, 0],

                   'num_wings': [2, 0, 0, 0],

                   'num_specimen_seen': [10, 2, 1, 8]},

                  index=['falcon', 'dog', 'spider', 'fish'])

print('This is a dataframe')
print(df)


# code to show a plot

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

# this line is not goint to show anything
plt.show()
