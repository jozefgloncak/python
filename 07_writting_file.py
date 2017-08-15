from sys import argv
filename = argv[1]

f_descr = open(filemane,"w")

while line != "end":
  line = raw_input()
  f_descr.write(line)

f_descr.close()
