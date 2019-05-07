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
conf_dic = dict(
    from_addr    = 'so2_chc',
    to_addr_list = [''],
    cc_addr_list = [],
    subject      = 'instrument not measuring',
    message      = '',
    login        = 'bolivia-campaign-user@chacaltaya.edu.bo',
    password     = 'pass here',
    watch_path   = '/tmp/data',
    host         = '10.8.3.33',
    port         = 2105,
    time_interval= 2, #seconds 
    tries        = 3 # tries before sending email (time_interval*tries)

)

# %%

