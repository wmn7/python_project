#!/usr/bin/env python3

filename = "/filename"

try:
	f = open(filename)
except:
	print("File not found")
finally:
	print("finally")
	f.close()
