# 这里记录一些数据清洗时候的tricks


# 1. python中如何实现R里面的mutate效果？使用assign+lambda函数，用map遍历
import pandas as pd

df = pd.DataFrame({
    'name': ['alice','bob','charlie','daniel'],
    'age': [25,66,56,78]
})

df.assign(
    is_senior = lambda dataframe: dataframe['age'].map(lambda age: True if age >= 65 else False) 
)