
# coding: utf-8

# In[ ]:


bb_df


# In[ ]:


bb_df['name'].unique()


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
from bokeh.layouts import column,gridplot
from bokeh.models import DataSource, RangeTool, HoverTool,ColumnDataSource,LabelSet
import bokeh.palettes as bp
output_notebook()
import pandas as pd
import numpy as np
from bokeh.palettes import *

#  ヒット数の推移




p = figure(
    title=None,  # タイトルを入力
    x_axis_label='timestamp',  # x軸のラベル
    y_axis_label='EP',  # y軸のラベル
    x_range=(2007,2018),
    y_range=(0,200),
    width=1000,
    height=500,  # グラフの幅と高さの指定
)

select_colum = ['year','h','name','hr']
player_list = ['坂本 勇人','山田 哲人','筒香 嘉智']


df_list= [bb_df[bb_df['name'] == player][select_colum] for player in player_list]

for i,df in enumerate(df_list,3):
    df = df.sort_values('year')
    p.line(
    x=df['year'], y=df['h'], color=Paired[12][i], legend=df['name'].unique()[0])

#  ヒットと打撃の散布
    
q = figure(
    title=None,  # タイトルを入力
    x_axis_label='H',  # x軸のラベル

    y_axis_label='HR',  # y軸のラベル


    width=1000,
    height=500,  # グラフの幅と高さの指定
)

for i,df in enumerate(df_list,3):
    df = df.sort_values('year')
    q.circle(
    x=df['h'], y=df['hr'], color=Paired[12][i], legend=df['name'].unique()[0],size=20,name='a')


r = figure(
    title=None,  # タイトルを入力
    x_axis_label='H',  # x軸のラベル

    y_axis_label='HR',  # y軸のラベル


    width=1000,
    height=500,  # グラフの幅と高さの指定
)

source=ColumnDataSource(bb_df)
r.circle(x='h', y='hr',source=source)
labels = LabelSet(x='h', y='hr',
              x_offset=5, y_offset=5, source=source)
#r.add_layout(labels)

s = figure(
    title=None,  # タイトルを入力
    x_axis_label='H',  # x軸のラベル

    y_axis_label='HR',  # y軸のラベル


    width=1000,
    height=500,  # グラフの幅と高さの指定
)

s.vbar(x='h', top='hr',source=ColumnDataSource(bb_df.groupby('name').max())
       ,width=0.5
      )


t = figure(
    title=None,  # タイトルを入力
    x_axis_label='timestamp',  # x軸のラベル
    y_axis_label='HR',  # y軸のラベル
    width=1000,
    height=500,  # グラフの幅と高さの指定
)

t.vbar(x='year', top='hr',source=ColumnDataSource(bb_df[bb_df['name']=='筒香 嘉智'])
       ,width=0.5
      )

t.vbar(x='year', top='hr',source=ColumnDataSource(bb_df[bb_df['name']=='坂本 勇人'])
       ,width=0.5
      )

grid = gridplot([[p],[q],[r],[s],[t]])
show(grid)


# In[ ]:


from bokeh.models import AjaxDataSource, CustomJS
adapter = CustomJS(code="""
        const result = {x: [], y: []}
        const pts = cb_data.response.points
        for (i=0; i<pts.length; i++) {
            result.x.push(pts[i][0])
            result.y.push(pts[i][1])
        }
        return result
    """)

source = AjaxDataSource(data_url='http://localhost:5050/data',
                            polling_interval=10000, adapter=adapter)

p = figure(plot_height=300, plot_width=800, background_fill_color="lightgrey",
               title="Streaming Noisy sin(x) via Ajax")
p.circle('x', 'y', source=source)

p.x_range.follow = "end"
p.x_range.follow_interval = 10
show(p)


# In[ ]:


from bokeh.models import AjaxDataSource, CustomJS
adapter = CustomJS(code="""
        const result = {x: [], y: []}
        const pts = cb_data.response.points
        for (i=0; i<pts.length; i++) {
            result.x.push(pts[i][0])
            result.y.push(pts[i][1])
        }
        return result
    """)

source = AjaxDataSource(data_url='http://localhost:5050/data2',
                            polling_interval=10000, adapter=adapter)
u = figure(plot_height=300, plot_width=800, 
           y_axis_label='HR',  # y軸のラベル
           background_fill_color="lightgrey",
               title="Streaming Noisy sin(x) via Ajax")
u.circle('x', 'y', source=source)

u.x_range.follow = "end"
u.x_range.follow_interval = 1
show(u)


# In[ ]:


select_colum = ['year','hr','name']
player_list = ['阿部 慎之助']

abe_df = bb_df[bb_df['name'].isin(player_list)][select_colum]

display(abe_df.sort_values('year').reset_index())


# In[ ]:


abe_df.sort_values('year').reset_index().hr.values

