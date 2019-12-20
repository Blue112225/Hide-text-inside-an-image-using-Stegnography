import sys

if sys.argv[1] == "-e":
	try:
		with open(sys.argv[2],'a') as fil:
			fil.write("\n"+sys.argv[3])
	except Exception as e:
		print(e)
elif sys.argv[1] == "-d":
	try:
		with open(sys.argv[2],'rb') as fil:
			lines = fil.readlines()
			print(lines[len(lines)-1].decode())
	except Exception as e:
		print(e)
