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
from secret_conf import secret_conf

# %%
import glob, datetime
def test_so2_values(path):
    #     path = '/Users/diego/so2na/data/small/'
    pat = 'chc*.dat'
    files = glob.glob(path+pat)
    last_file = files[-1]
    with open(last_file, "r") as file:
        lastline = (list(file)[-1])
    vals = lastline.split()
    heads = ['Time','Date','Flags','so2','hiso2',
             'intt','rctt','pgast','pres','smplfl',
             'pmtv','lmpv','lmpi'];
    dic = {}
    for h,v in zip(heads,vals):
        dic[h]=v
    dt = datetime.datetime.strptime(dic['Date']+' '+dic['Time'],
                                    '%m-%d-%y %H:%M')

    dic['dt'] = dt
    kind = {
        'Flags': str,
        'so2': float,
        'hiso2': float,
        'intt': float,
        'rctt': float,
        'pgast': float,
        'pres': float,
        'smplfl': float,
        'pmtv': float,
        'lmpv': float,
        'lmpi': int}

    for k,v in kind.items():
        dic[k]=v(dic[k])

    range_vals = {
        'so2': [-2,8],
        'intt': [19,26],
        'rctt': [44,46],
        'pres': [393,397],
        'smplfl': [0.28,0.30],
        'pmtv': [-727.5,-726.5],
        'lmpv': [900,950],
        'lmpi': [92,96],
        'dt'  : [datetime.datetime.now()-datetime.timedelta(hours=4,minutes=10),
                 datetime.datetime.now()-datetime.timedelta(hours=3,minutes=59)]
    }
    equal_vals = {
        'Flags': '----LL--',
        'hiso2': 0,
        'pgast': 0,
    }

    res_dict = {}
    for k,v in range_vals.items():
        res_dict[k] = (v[0]<=dic[k]) and (v[1]>=dic[k])
    for k,v in equal_vals.items():
        res_dict[k] = v == dic[k]

    test_passed = all(res_dict.values())

    mess = [
        str(range_vals),
        str(dic),
        str(res_dict),
    ]

    mes_out = ''
    for i in mess:
        mes_out = mes_out + i + '\n'
    return dict(test=test_passed, message=mes_out)

# %%
conf_dic = dict(
    monitor_mode = 'value', # options: folder, connected, value
    from_addr    = '', # this values is not shown anywhere as of now
    to_addr_list = secret_conf.secret_dic['to_addr_list'],
    cc_addr_list = secret_conf.secret_dic['cc_addr_list'],
    subject      = 'so2 values at chc out of range. sent from amazon',
    message      = '',
    login        = secret_conf.secret_dic['login'],
    password     = secret_conf.secret_dic['password'],
    watch_path   = '/tmp/data', # directory that needs to be increasing. mode: folder
    host         = '10.8.3.34', # in case connection test, this is the address of the monitored computer. mode connected
    port         = 2105, # this is the port that we will check is open in the monitored computer. mode connected
    time_interval= 600, #seconds
    tries        = 3, # tries before sending email (time_interval*tries)
    value_range  = '/uhel_data/so2_chc/', # the value range to be monitored. only needed for mode value
    value_func   = test_so2_values # function to get the value_range

)

# %%
util.watchdog(**conf_dic)

# %%


