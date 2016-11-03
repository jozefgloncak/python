def simple(myString):

 x = raw_input(myString)
 if(x == "1"):
  print("ok")
 else:
  print("wrong")

#simple("specify input")

def add(num1, num2):
 return num1 + num2

def substract(num1, num2):
 return num1 - num2

def multiply(num1,num2):
 return num1*num2

def divide(num1, num2):
 return num1/num2

def main():

 operand1 = input("Specify first number: ")
 operand2 = input("Specify second number: ")  

 operation = raw_input("Select operation, please (+,-,*,/) ")

 if (operation == '+'):
  print(add(operand1, operand2))
 elif (operation == '-'):
  print(substract(operand1, operand2))
 elif (operation == '*'):
  print(multiply(operand1, operand2))   
 elif (operation == '/'): 
  print(divide(operand1, operand2))   
 else:  
  print("You must specify correct operation")

main()


