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

# secret_conf.secret_conf is the location of the secret_conf file. u can have
# multiple ones, just edit the following lines
import secret_conf.secret_conf as secret_conf
# %%
conf_dic = dict(
    monitor_mode= 'connected', # options: folder, connected, value
    from_addr    = '', # this values is not shown anywhere as of now
    to_addr_list = secret_conf.secret_dic['to_addr_list'],
    cc_addr_list = secret_conf.secret_dic['cc_addr_list'],
    subject      = 'so2 analyzer at chc not connected to internet',
    message      = '',
    login        = secret_conf.secret_dic['login'],
    password     = secret_conf.secret_dic['password'],
    watch_path   = '/tmp/data', # directory that needs to be increasing. mode: folder
    host         = '10.8.3.33', # in case connection test, this is the address of the monitored computer. mode connected
    port         = 2105, # this is the port that we will check is open in the monitored computer. mode connected
    time_interval= 2, #seconds 
    tries        = 3, # tries before sending email (time_interval*tries)
    value_range  = [0, 10], # the value range to be monitored. only needed for mode value
    value_func   = None # function to get the value_range

)

# %%
util.watchdog(**conf_dic)

# %%


