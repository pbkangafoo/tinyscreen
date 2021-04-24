#!/usr/bin/env python
# -*- coding: utf8 -*-

"""

 _______.__               _______.
|_     _|__|.-----.--.--.|     __|.----.----.-----.-----.-----.
  |   | |  ||     |  |  ||__     ||  __|   _|  -__|  -__|     |
  |___| |__||__|__|___  ||_______||____|__| |_____|_____|__|__|
                  |_____|

Tinyscreen written by Peter Bartels
Version 0.1

Tinyscreen displays the system information. It is supposed as quick way to
see your information using theme files based on ascii art.

https://www.kangafoo.de

"""


import sys
import os
import pwd
import argparse
import platform
from datetime import timedelta


global mylist


def print_infoheader():
	""" prints the info screen

	print_infoheader() -> no return

	"""
	print(" _______.__               _______.")
	print("|_     _|__|.-----.--.--.|     __|.----.----.-----.-----.-----.")
	print("  |   | |  ||     |  |  ||__     ||  __|   _|  -__|  -__|     |")
	print("  |___| |__||__|__|___  ||_______||____|__| |_____|_____|__|__|")
	print("                  |_____| © P.Bartels - https://www.kangafoo.de\n")

def get_username():
	""" returns the current username

	get_username() -> return string

	"""
	return pwd.getpwuid(os.getuid())[0]


def get_hostname():
	""" Returns the name of the machine

	get_hostname() -> return string

	"""
	return os.uname()[1]


def get_release():
	""" Returns the kernel version aka release

	get_release() -> return string

	"""
	return os.uname()[2]


def get_machine():
	""" returns type of machine

	get_machine() -> return string

	"""
	return os.uname()[4]


def get_distribution():
	""" Returns the linux distribution + version

	get_distribution -> return string

	"""
	s = platform.system_alias()[0] + ' ' + platform.system_alias()[1]
	return s


def get_uptime():
	"""

	get_uptime() -> return string

	based on planzero.org/blog/2012/01/26/system_uptime_in_python,_a_better_way
	"""
	with open('/proc/uptime', 'r') as f:
		uptime_seconds = float(f.readline().split()[0])
		uptime_string = str(timedelta(seconds=uptime_seconds))
	return uptime_string


def get_cpuname():
	""" returns the cpu name by catching it from /proc/cpuinfo

	get_cpuname() -> return string

	"""
	with open('/proc/cpuinfo', 'r') as f:
		for line in f:
			if 'model name' in line:
				cpuname = line.split(':')[1].strip()
				cpuname = cpuname.replace('  ', '')
				break
	return cpuname


def replace_all(text, dic):
	""" replaces multiple strings based on a dictionary

	replace_all(string,dictionary) -> string

	"""
	for i, j in dic.items():
		text = text.replace(i, str(j))
	return text


def process(lines):
	""" Open the given file and process each line before output

	process(string) -> no return

	"""
	for line in lines:
		line = line.replace("\n", "")
		line = line.replace("\r", "")
		newline = replace_all(line, mylist)
		print(newline)


def create_list():
	""" Creates dictionary with keywords and functions including values

	create_list() -> dictionary

	"""
	return {"§U§": get_username(),
		"§H§": get_hostname(),
		"§UP§": get_uptime(),
		"§CPU§": get_cpuname(),
		"§R§": get_release(),
		"§M§": get_machine(),
		"§D§": get_distribution}


if __name__ == "__main__":
	parser = argparse.ArgumentParser("usage: %prog [options] arg1 arg2")
	parser.add_argument("-i", "--input", dest="ifile",
                        help="specify the artwork file for output")
	options = parser.parse_args()
	if len(sys.argv) < 2:
		print_infoheader()
		parser.print_help()
		quit()
	else:
		mylist = create_list()
		lines = open(options.ifile, "r").readlines()
		process(lines)

