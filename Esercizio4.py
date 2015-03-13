#!/usr/bin/python

#include dependencies
import pyudev
import dbus, gobject, os
import time

class Colors :
        red = "\033[1;31m"
        blue = "\033[1;34m"
        pink = "\033[1;35m"
        green = "\033[1;32m"
        end = "\033[0m"


#mount device
def mount(device, fs):
	res = ''
	_bus = dbus.SystemBus();
	_proxy = _bus.get_object('org.freedesktop.UDisks','/org/freedesktop/UDisks')
	_iface = dbus.Interface(_proxy, 'org.freedesktop.UDisks')
	print _iface
	for _dev in _iface.EnumerateDevices():
		_dev_obj = _bus.get_object('org.freedesktop.UDisks', _dev)
		_dev_prop = dbus.Interface(_dev_obj, 'org.freedesktop.DBus.Properties')
		if _dev_prop.Get('','DeviceFile')==device:
			_idev = dbus.Interface(_dev_obj, 'org.freedesktop.DBus.UDisks.Device')
			res = _idev.get_dbus_method('FilesystemMount', dbus_interface='org.freedesktop.UDisks.Device')(fs,[])
	#FIXME sarebbe figo dire come si chiama la cartella creata in /media
	print " "
	print Colors.blue + "Il device montato in /media/.." + Colors.end
	print Colors.blue + "IMPORTANTE: usa il comando" + Colors.end + Colors.red + " umount " + device + Colors.end  + Colors.blue + " per smontare il device" + Colors.end
	quit()

#no need to comment this :)
def print_device(_path, _type, _fs):
	print " "
	print Colors.green + "Rilevata nuova partizione !!" + Colors.end
	print Colors.green + "Partizione: " + Colors.end + " " + Colors.red + _path + Colors.end
	print Colors.green + "Tipo      : " + Colors.end + " " + Colors.red + _type + Colors.end
	print Colors.green + "FileSystem: " + Colors.end + " " + Colors.red + _fs   + Colors.end 
	print " "
	check_premount(_path, _fs)

#call mount if needed, exit otherwise
def check_premount(_path,fs):
	scelta = input(Colors.green + "Sei sicuro di voler montare(1/0): " + Colors.end )
	if (scelta == 1):
		mount(_path, _fs)
	else:
		print "Non monto ..."
		quit()	

#short message to welcome users
def splash():
	print Colors.green + "Questo script rileva automaticamente quando viene collegata una chiavetta o un device." + Colors.end
	print Colors.green + "Se hai gia' collegato la chiavetta, SCOLLEGALA prima di avviare lo script." + Colors.end
	print " "
	raw_input(Colors.green + "Premi INVIO per avviare lo script..." + Colors.end )
	print " "
	print Colors.blue + "Cerco device..." + Colors.end
	print " "


if __name__ == '__main__':
	print " "
	print Colors.green + "Versione pyudev: " + Colors.end +  " " + Colors.red  + pyudev.__version__ + Colors.end
	print " "
	#prompt user
	splash()
	#monitor devices
	_context = pyudev.Context()
	monitor = pyudev.Monitor.from_netlink(_context)
	monitor.filter_by(subsystem = 'block', device_type = 'partition' )
	monitor.filter_by(subsystem = 'input')
	#when a device is plugged in, call print_device to ask if it is to be mounted
	for action, device in monitor:
		_path = device.device_node
		_type = device.device_type
		_fs   = device.get('ID_FS_TYPE')
		#properties
		print_device(_path, _type, _fs)
		

