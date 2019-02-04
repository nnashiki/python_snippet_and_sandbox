
# coding: utf-8

# In[ ]:


bb_df


# In[ ]:


select_colum = ['year','h','name']
player_list = ['坂本 勇人','山田 哲人']

sakamoto_df = bb_df[bb_df['name'].isin(player_list)][select_colum]
display(sakamoto_df)


# In[ ]:


df_list= [bb_df[bb_df['name'] == player][select_colum] for player in player_list]

for df in df_list:
    display(df)


# In[ ]:


from bokeh.io import output_notebook, show
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
from bokeh.models import DataSource, RangeTool, HoverTool
import bokeh.palettes as bp
output_notebook()
import pandas as pd
import numpy as np
from bokeh.palettes import *

p = figure(
    title='タイトル',  # タイトルを入力
    x_axis_label='timestamp',  # x軸のラベル
    y_axis_label='EP',  # y軸のラベル
    width=1000,
    height=500,  # グラフの幅と高さの指定
)

select_colum = ['year','h','name']
player_list = ['坂本 勇人','山田 哲人','筒香 嘉智']

df_list= [bb_df[bb_df['name'] == player][select_colum] for player in player_list]

for i,df in enumerate(df_list):
    df = df.sort_values('year')
    p.line(
    x=df['year'], y=df['h'], color=Reds3[i], legend=df['name'].unique()[0])
    



show(column(p))

