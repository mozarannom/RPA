import pandas as pd
import matplotlib.pyplot as plt

hat = pd.read_csv('ch4-2.csv')
print(hat.describe(), end="\n\n")

plt.figure(figsize=(8,10))
plt.boxplot(hat.weight)
plt.title('B hatchery chick weight box', fontsize =17)
plt.ylabel('weight(g)')
plt.show()