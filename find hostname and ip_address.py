# -*- coding: utf-8 -*-
"""
@author: Nanosoft
@website: www.thenanosoft.com
@github: https://github.com/thenanosoft/find-my-ip-address-python-gui
"""


from dearpygui.dearpygui import *
import socket

#get hostname
hostname = socket.gethostname()

#get host ip address
ipAddr = socket.gethostbyname(hostname)

# display text in gui window
add_text("Hostname: - " + hostname)
add_text("My Ip Address: - " + ipAddr)


#Title of the GUI window
set_main_window_title("IP Address - Python GUI")

#gui width & high size (w,h)
set_main_window_size(250, 100)

# user can't reset the window size on runtime
set_main_window_resizable(False)


start_dearpygui()