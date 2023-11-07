import socket
import struct
import time

MON_KILLPID = 13
MON_EXEC = 14
MON_PEXEC = 15
MON_BABIEXEC = 16

BABILD_PORT = 17511
BABIMO_PORT = 17518
BABINFO_PORT = 17516
TIMEOUT = 1

def killpid(server, name):
	print('killpid ',server, name)
	fp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	fp.settimeout(TIMEOUT)
	try:
		fp.connect((server, BABIMO_PORT))
		length = struct.pack('i',4+len(name))
		fp.send(length)
		com = struct.pack('i',MON_KILLPID)
		fp.send(com)
		form_s = str(len(name)+5) + 's'
		bname = struct.pack(form_s,name.encode())
		fp.send(bname)
	except socket.timeout:
		print("Cant't connect to ", server)
	fp.close()
	time.sleep(1)

def execbabiproc(server, name, arg):
	print('execbabiproc ',server, name)
	fp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	fp.settimeout(TIMEOUT)
	try:
		fp.connect((server, BABIMO_PORT))
		line = name + " " + arg
		length = struct.pack('i',4+len(line))
		fp.send(length)
		com = struct.pack('i',MON_BABIEXEC)
		fp.send(com)
		form_s = str(len(line)+5) + 's'
		bline = struct.pack(form_s,line.encode())
		fp.send(bline)
	except socket.timeout:
		print("Can't connect to ", server)
	fp.close()
	time.sleep(1)

def execarg(server, arg):
	print('execarg ',server, arg)
	fp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	fp.settimeout(TIMEOUT)
	try:
		fp.connect((server, BABIMO_PORT))
		length = struct.pack('i',4+len(arg))
		fp.send(length)
		com = struct.pack('i',MON_EXEC)
		fp.send(com)
		form_s = str(len(arg)+5) + 's'
		barg = struct.pack(form_s,arg.encode())
		fp.send(barg)
	except socket.timeout:
		print("Can't connect to ", server)
	fp.close()
	time.sleep(1)

def execargr(server, arg):
	print('execargr ',server, arg)
	fp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	fp.settimeout(TIMEOUT)
	rstr = ''
	try:
		fp.connect((server, BABIMO_PORT))
		length = struct.pack('i',4+len(arg))
		fp.send(length)
		com = struct.pack('i',MON_PEXEC)
		fp.send(com)
		form_s = str(len(arg)+5) + 's'
		barg = struct.pack(form_s,arg.encode())
		fp.send(barg)

		length = fp.recv(4)
		rstr = fp.recv(1024)
	except socket.timeout:
		print("Can't connect to ", server)
	fp.close()
	time.sleep(1)
	return rstr

def restart_babild(server):
	killpid(server,'babild')
	execbabiproc(server,'babinfo','')
	execbabiproc(server,'babild','-l')

def restart_babies(server,efn):
	killpid(server,'babies')
	execbabiproc(server,'babies','-l '+str(efn))

def restart_mpvbabildes(server):
	execarg(server,'killall mpvbabildes')
	execarg(server,'/usr/bin/mpvbabildes &> /dev/null')


if __name__ == '__main__':
    print("main called")
