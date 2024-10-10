import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

hat = pd.read_csv('singer_youtube.csv')

print(hat.head(), end="\n\n")

font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

plt.figure(figsize=(15, 10))
plt.bar(hat['name'], hat['youtube count'], color=('red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple'))

plt.title('YouTube Subscriber Count by Group')
plt.xlabel('name')
plt.ylabel('youtube count')

for i in range(len(hat)):
    plt.text(i, hat['youtube count'].iloc[i] + 50000, hat['youtube count'].iloc[i], ha='center')

plt.show()
