# find-my-ip-address-python-gui
Get Hostname & IP Address using Python GUI

## First install GUI Library 
```Python
pip install dearpygui
```

### Find Hostname
```Python
hostname = socket.gethostname()
```

### Find IP Address
```Python
hostname = socket.gethostname()

ipAddr = socket.gethostbyname(hostname)
```

### Complete Code
Display Hostname & IP Address in Python GUI
```Python
"""
@author: Nanosoft
@website: www.thenanosoft.com
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
```

### The Final Output Is:
![IP Address Python GUI image](https://imgur.com/99k7hXd.png)

---
> Follow Us on

[Youtube](https://youtube.com/thenanosoft) | [Facebook](https://facebook.com/thenanosoft) | [Twitter](https://twitter.com/thenanosoft) | [Instagram](https://instagram.com/thenanosoft)
