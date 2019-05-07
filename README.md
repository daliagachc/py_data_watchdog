# py_data_watchdog 
This python package is intended to monitor computers taking measurements

## It has the following usages:
1. folder size increment 
    - monitors that the directory with data is increasing
2. computer online 
    - monitor that a machine is connected to the internet 
3. value within range 
    - monitor that a value is within specifications 

Whenever the watchdog detects a problem, it sends a message a one or directions with 
a custom message. 
  
it uses only standard python3 libraries. Therefore no extra packages are needed

configuration parameters and code execution is controlled 
by the file run_me_[watchdog name].py

its is recommended to launch the watchdog using [supervisord](http://supervisord.org/) 
which can be easily installed in linux/mac. For Windows, cygwin is needed 
which is recommended in any case for ssh connection to the computer. 
Instructions on installing supervisord on windows can be found 
[here](https://stackoverflow.com/questions/7629813/is-there-windows-analog-to-supervisord)


