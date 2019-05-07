# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 0.8.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import util
import importlib
importlib.reload(util);

# %%
conf_dic = dict(
    monitor_mode= 'connected', # options: folder, connected, value
    from_addr    = '', # this values is not shown anywhere as of now
    to_addr_list = ['daliaga@chacaltaya.edu.bo'],
    cc_addr_list = [],
    subject      = 'instrument not measuring',
    message      = '',
    login        = 'bolivia-campaign-user@chacaltaya.edu.bo',
    password     = 'chacaltaya_5240masl',
    watch_path   = '/tmp/data', # directory that needs to be increasing. mode: folder
    host         = '10.8.3.33', # in case connection test, this is the address of the monitored computer. mode connected
    port         = 2105, # this is the port that we will check is open in the monitored computer. mode connected
    time_interval= 2, #seconds 
    tries        = 3, # tries before sending email (time_interval*tries)
    value_range  = [0, 10] # the value range to be monitored. only needed for mode value

)

# %%
util.check_socket(**conf_dic)

# %%
import random
random.random()

# %%

