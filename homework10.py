
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
lst = ['1'] * 10
lst += ['0'] * 10
random.shuffle(lst)
lst1 = ['1'] * 10
lst1 += ['0'] * 10
random.shuffle(lst1)
data = pd.DataFrame({'robot':lst,'human':lst1})
data.head()

print(data)


