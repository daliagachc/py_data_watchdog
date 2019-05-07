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
import random
# %%
def check_range(value_range):
    # must return a dictionary like this:
    # dict(test=True or False, message= 'to be appended to the email')
    test = True
    res = random.random()*30
    mes = ''
    if res < value_range[0] or res > value_range[1]:
        test = False
        mes = 'the error value is {}. it should be {}'.format(res,value_range)
    dic = dict(
        test=test,
        message= mes
    )
    return dic


# %%
conf_dic = dict(
    monitor_mode= 'value', # options: folder, connected, value
    from_addr    = '', # this values is not shown anywhere as of now
    to_addr_list = secret_conf.secret_dic['to_addr_list'],
    cc_addr_list = secret_conf.secret_dic['cc_addr_list'],
    subject      = 'instrument not measuring',
    message      = '',
    login        = secret_conf.secret_dic['login'],
    password     = secret_conf.secret_dic['password'],
    watch_path   = '/tmp/data', # directory that needs to be increasing. mode: folder
    host         = '10.8.3.34', # in case connection test, this is the address of the monitored computer. mode connected
    port         = 2105, # this is the port that we will check is open in the monitored computer. mode connected
    time_interval= 2, #seconds 
    tries        = 3, # tries before sending email (time_interval*tries)
    value_range  = [0, 10], # the value range to be monitored. only needed for mode value
    value_func   = check_range # function to get the value_range

)

# %%
util.watchdog(**conf_dic)

# %%


