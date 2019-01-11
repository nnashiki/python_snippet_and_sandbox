
# coding: utf-8

# In[ ]:


bb_df


# In[ ]:


sakamoto_df = bb_df[bb_df['name'] == '坂本 勇人'][['h','year']]
display(sakamoto_df)


# In[ ]:


from bokeh.io import output_notebook, show
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
from bokeh.models import DataSource,RangeTool,HoverTool
import bokeh.palettes as bp
output_notebook()
import pandas as pd
import numpy as np


p = figure(title='タイトル',         # タイトルを入力
           x_axis_label='timestamp', # x軸のラベル
           y_axis_label='EP',        # y軸のラベル
           width=1000 ,height=500,     # グラフの幅と高さの指定
          )

p.line(x=sakamoto_df['year'],y=sakamoto_df['h'],color='red',legend='sakamoto')

show(column(p))

