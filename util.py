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
import smtplib
import os
import socket
from contextlib import closing
import time

# %%
def sendemail(*,from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587',**keywords):
	header  = 'From: %s\n' % from_addr
	header += 'To: %s\n' % ','.join(to_addr_list)
	header += 'Cc: %s\n' % ','.join(cc_addr_list)
	header += 'Subject: %s\n\n' % subject
	message = header + message

	server = smtplib.SMTP(smtpserver)
	server.starttls()
	server.login(login,password)
	problems = server.sendmail(from_addr, to_addr_list, message)
	server.quit()
	return problems

# %%
def get_size(*,watch_path,**keyword):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(watch_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


# %%


def check_socket(*,host, port, **keyword):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            ret=True
        else:
            ret=False
    return ret

# %%
def watchdog(**conf_dic):
    mode = conf_dic['monitor_mode']
    if mode is 'folder':
        res = watchdog_folder(**conf_dic)
    if mode is 'connected':
        res = watchdog_connected(**conf_dic)
    if mode is 'value':
        res = watchdog_value(**conf_dic)
    else:
        res = False

    return res

# %%

def watchdog_folder(**conf_dic):
    size1 = get_size(**conf_dic)
    time.sleep(conf_dic['time_interval'])
    tries = conf_dic['tries']
    attempt = 1
    while True:
        size2 = get_size(**conf_dic)
        size_dif = size2 - size1
        size1 = size2
        if size_dif <= 0:
            print('error',attempt)
            if attempt>=tries:
                print('sending email')
                sendemail(**conf_dic)
                attempt = 1
            else: attempt = attempt + 1
        else:
            attempt = 1
            print('fine')
        time.sleep(conf_dic['time_interval'])

# %%

def watchdog_connected(**conf_dic):
    tries = conf_dic['tries']
    attempt = 1
    while True:

        if check_socket(**conf_dic) is False:
            print('error',attempt)
            if attempt>=tries:
                print('sending email')
                sendemail(**conf_dic)
                attempt = 1
            else: attempt = attempt + 1
        else:
            attempt = 1
            print('fine')
        time.sleep(conf_dic['time_interval'])

def watchdog_value(**conf_dic):
    tries = conf_dic['tries']
    attempt = 1
    fun = conf_dic['value_func']
    arg = conf_dic['value_range']

    while True:
        fun_res = fun(arg)
        test = fun_res['test']
        message = fun_res['message']

        if test is False:
            print('error',attempt)
            print(message)
            if attempt>=tries:
                mod_conf_dic = conf_dic.copy()
                mod_conf_dic['message'] = mod_conf_dic['message'] + '\n' + message

                print('sending email')
                sendemail(**mod_conf_dic)
                attempt = 1
            else: attempt = attempt + 1
        else:
            attempt = 1
            print('fine')
        time.sleep(conf_dic['time_interval'])

