import matplotlib.pyplot as plt
import pandas as pd

# 创建一个数据框
df = pd.DataFrame({'Income group': ['Top 1%', 'Top 10%', 'Top 20%', 'Top 30%', 'Top 40%', 'Top 50%', 'Bottom 50%'], 'Share of wealth': [0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 0.1]})

# 创建一个饼图
plt.pie(df['Share of wealth'], labels=df['Income group'], autopct='%1.1f%%')

# 显示饼图
plt.show()
