#!/usr/bin/env python
#coding:utf-8

import time
import pynotify
import gtk

class Warning:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(32)
        self.window.set_title("Eye Guard")
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_keep_above(True)
        self.button = gtk.Button("Ok, let me back to work!")
        self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
        self.window.add(self.button)
        self.button.show()
        self.window.show()
    def run(self):
        gtk.main()
    def destroy(self, widget):
        gtk.main_quit()

def Notify():
    pynotify.init("eye-guard")
    msg = pynotify.Notification("Eye Guard", "You have been worked for 30 minutes!\n\
            Rest for a while!")
    msg.show()

def main():
    print "Eye Guard is now running!"
    while True:
        #default 30 minutes, change it for your own habbit
        time.sleep(30 * 60)
        Notify()
        warning = Warning()
        warning.run()

if __name__ == "__main__":
    main()
