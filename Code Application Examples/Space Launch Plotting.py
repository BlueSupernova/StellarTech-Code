import pandas as pd

file_path = 'C:\SpaceX_Launches.xlsx'

df = pd.read_excel(file_path, sheet_name='LaunchData')

import plotly.express as px

fig = px.bar(df, x='Year', y='Count', text='Count')
fig.update_layout(title='SpaceX Launches Per Year')
fig.show()

#del df['Count']

import matplotlib.pyplot as plt
#import pandas as pd

df = df.sort_values('Year', ascending=True)
df.plot(x="Year", y=['FALCON 9','FALCON HEAVY','DRAGON & FALCON 9','FALCON 1'], kind="bar", stacked=True)
plt.title('SpaceX Launch Breakdown Per Year')
plt.xlabel('Years')
plt.ylabel('Number of Launches')
plt.show()
