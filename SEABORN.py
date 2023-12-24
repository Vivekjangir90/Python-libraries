import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# days = [1,2,3,4,5]
# temp1 = [15.2,52.1,23.5,31.4,32.8]
# temp_df = pd.DataFrame({'days':days,"temp":temp1})
# sns.lineplot(x = "days",y = "temp",data = temp_df)
# plt.show()

# tips = sns.load_dataset("tips.csv")
# tips = pd.read_csv("https://github.com/mwaskom/seaborn-data/raw/master/tips.csv")
tips = pd.read_csv('C:/Users/ISO/Downloads/tips.csv')

print(tips)