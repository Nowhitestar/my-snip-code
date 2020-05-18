# 作图设置

# 显示中文
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] # mac
plt.rcParams['font.sans-serif']=['SimHei']  # win

# 正常显示负号-win
plt.rcParams['axes.unicode_minus']=False  

# 主题颜色设置
sns.set(style="whitegrid", palette='RdBu', font='Arial Unicode MS') # seaborn