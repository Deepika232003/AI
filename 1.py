import pandas as pd
import numpy as np
data = pd.read_csv("2_1.csv")
print("Data:\n", data, "\n")
data_array = np.array(data)
d = data_array[:, :-1]
print("The attributes are:\n", d, "\n")
target = data_array[:, -1]
print("The target is:\n", target, "\n")
def train(c, t):
    specific_hypothesis = None
    for i, val in enumerate(t):
        if val == "Yes":
            specific_hypothesis = c[i].copy()
            break
    if specific_hypothesis is None:
        return "No positive examples found."
    for i, val in enumerate(c):
        if t[i] == "Yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
    return specific_hypothesis
final_hypothesis = train(d, target)
print("The final hypothesis is:\n", final_hypothesis)
