#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.24.1
#  in conjunction with Tcl version 8.6
#    Jul 17, 2019 11:32:14 AM CDT  platform: Windows NT
#    Jul 19, 2019 01:51:10 PM CDT  platform: Windows NT
#    Jul 24, 2019 04:25:14 PM CDT  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global che47
    che47 = tk.StringVar()
    global che48
    che48 = tk.StringVar()
    global che49
    che49 = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import MainUIBuilder
    MainUIBuilder.vp_start_gui()



