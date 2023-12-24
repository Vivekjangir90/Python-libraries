import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sn

event = pd.read_csv('athlete_events.csv')
# pd.open_csv("athlete_events.csv")

# print(event)

# print(event.head())
# print(event["Name"])
# # print(event.columns())
# print(pd.set_option('display.max_columns', None))
# print(pd.set_option('display.max_rows', 10))
# print(event)
# print(event.columns.tolist())
# print(event.row.tolist())
# print(event.columns.values)
# print(event.shape)
# print(event.shape[0])
# print(event.shape[1])
# print(event.info())
# print(event.describe())

# FETCHING ROWS AND COLUMNS USING ILOC

# print(type(event["Name"]))
# print(type(event))
# print(event.iloc[0])
# print(event.iloc[0:3])
# print(event.iloc[0:11:2])
# print(event.iloc[[0,11,2]])
# print(event.iloc[:,[4,5]])

# FILTRING DATAFRAMES ON A CONDITION


# print(pd.set_option('display.max_columns', None))
# print(pd.set_option('display.max_rows', None))
# mask = event["City"] == "London"
# print(event[mask])
# print(event["City"] == "London")


pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', 20)

# print(event['City'].value_counts())

# print(event['City'].value_counts().plot(kind='bar'))
# print(event['City'].value_counts().head().plot(kind='barh'))
# print(event['City'].value_counts().head().plot(kind='pie'))
# print(event['City'].value_counts().head().plot(kind='hist'))

# print(event['winner'].value_counts())
# print(event['City'].value_counts())
# print(event)
# print(event.sort_values('City').head())
# print(event.sort_values(['City', 'Age']).head(20))
# print(event.sort_values(['City', 'Age'],ascending=False).head(20))

# # print(event.drop_duplicates())
# print(event.drop_duplicates(['City']))
# print(event.drop_duplicates(['City']).shape)
# print(event.drop_duplicates(['City','Season']))
# print(event.drop_duplicates('Year'))
# print(event.drop_duplicates(['City'],inplace = True ))  #inplace change permanently so we don't use it
# gro = event.groupby('Team')
# print(gro.first())
# print(gro.last())
# print(gro.groups)
# print(event.iloc[5:])
# print(gro.get_group('China'))
# print(gro.sum())
# print(gro.mean())
# print(gro['Weight'].sum())

# print(event.head(10))
# print(event.groupby('Team')['Sport'].count().sort_values(ascending= False))
# mask = event['Sport'] == 'Football'
# new_event = event[mask]
# print(new_event.groupby('Medal')['City'].count())

# mask = event['Age']> 30
# new_event1 = event[mask]
# print(new_event1.groupby('Team')['Medal'].count().sort_values(ascending=False))
# print(xyz.index.tolist())
# print(xyz.values.tolist())
# event[event['City'].isin(xyz)]

# for merge two dataframes
# event.merge(data_set_name,left_on = 'col_name',right_on = 'col_name')

# print(event.pivot_table(index='Team',columns='Year',values='Medal',aggfunc='count'))

# pt=event.pivot_table(index='Team',columns='Year',values='Medal',aggfunc='count')
# print(sn.heatmap(pt))

# print(event.corr())
# print(event.rename(columns={'City':'Place'}))
# print(event.head(1))

# print(event.set_index('ID')) #set column into index
# print(event.reset_index()) #just revert last action and convert series into dataframe

# print(event.dropna()) #drop row when values are missing
# print(event.dropna(axis = 1, how='all')) #drop column when values are missing
# print(event.dropna(axis = 0,subset= ['column_name','column_name2'])) #drop row when values are missing

# print(event.fillna(0))
# print(event['column_name'].fillna('missing_value'))
# event.fillna() #ffill and bfill use case for missing values
