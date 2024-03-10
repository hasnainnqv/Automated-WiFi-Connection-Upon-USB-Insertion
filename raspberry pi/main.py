import pyudev
import time
import subprocess
import psutil
from bashfile import Connect_Wifi



def usb_connected():
	context = pyudev.Context()
	monitor = pyudev.Monitor.from_netlink(context)
	monitor.filter_by(subsystem="usb")
	monitor.start()
	for device in iter(monitor.poll, None):

		if device.action == "add":
			print("connected")
			print(device.get("ID_MODEL"))			
			if device.get("ID_MODEL"):
				time.sleep(6)
				obj = Connect_Wifi()
				obj.Run_code()
				print("Network Connected")
		if device.action == "remove":
			print(f"Device {device.get('ID_MODEL')} Ejected Successfully")

usb_connected()
				


