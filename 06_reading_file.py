from sys import argv

filename = argv[1]

f_hand = open(filename)

#for l in f_hand:
#  print l

end_of_file = False;
while not end_of_file:
  line = f_hand.readline()
  if line:  
    print(line)
  else:
    end_of_file = True
