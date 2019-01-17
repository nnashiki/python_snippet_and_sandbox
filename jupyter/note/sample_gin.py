
# coding: utf-8

# In[ ]:


import gin


# In[ ]:


@gin.configurable
class DNN(object):
  # Constructor parameters become configurable.
  def __init__(self,num_outputs=None,layer_sizes=512):
      self.num_outputs = num_outputs
      self.layer_sizes=layer_sizes


# In[ ]:


gin.parse_config_file('config.gin')


# In[ ]:


tst = DNN()


# In[ ]:


tst.layer_sizes

