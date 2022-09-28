#!/usr/local/bin/python3
import tkinter
import time

from requests import post
import json


def Main():
	global LifeCounter
	global GuiHelloLabel
	global GuiWindow

	logEntryJsonObject = {'logged_by_name':'MacTestOperatingLog', 'logged_by_type':'Debug Tester', 'log_entry':'Testing operating log.'}
	p = post('http://billgrace.com/ibdatatap/beacon/OperatingLog.php', data = {'operating_log_json':json.dumps(logEntryJsonObject)})
	# p = post('http://localhost/ibdatatap/beacon/OperatingLog.php', data = {'operating_log_json':json.dumps(logEntryJsonObject)})


	LifeCounter = 0
	GuiWindow = tkinter.Tk()
	GuiWindow.geometry('400x300+100+200')
	GuiWindow.configure(background='cyan')
	GuiWindow.resizable(True, True)
	GuiHelloLabel = tkinter.Label(GuiWindow, text='Hello, World!')
	GuiHelloLabel.place(anchor='nw', relx=0.00, rely=0.50)
	RefreshGui()
	GuiWindow.mainloop()

def RefreshGui():
	global LifeCounter
	global GuiHelloLabel
	global GuiWindow
	LifeCounter += 1
	GuiHelloLabel.configure(text='Hello, World! - - Is it 10 yet? ({0})'.format(LifeCounter))
	if LifeCounter > 100:
		GuiWindow.destroy()
	else:
		GuiWindow.after(1000, RefreshGui)

if __name__ == '__main__':
	Main()
