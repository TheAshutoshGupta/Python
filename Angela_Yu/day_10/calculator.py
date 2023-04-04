from art import logo

#add
def add(a,b):
  return a+b

#subs
def sub(a,b):
  return a-b
#mul
def mul(a,b):
  return a*b
#div
def div(a,b):
  return a/b

def calculator():
  print(logo)
  n1=float(input("first number?:"))
  
  operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
  }
  for i in operations:
    print(i)
  sym=input("pic an operation mentioned above")
  
  n2=float(input("second number?:"))
  
  
  
  calculation=operations[sym]
  answer=calculation(n1,n2)
  
  print(f"{n1} {sym} {n2} = {answer}")
  flag = "y"
  while flag=="y":
    sym=input("another operation")
    n2=float(input("next number?:"))
    
    calculation=operations[sym]
    answer2=calculation(answer,n2)
    
    print(f"{answer} {sym} {n2} = {answer2}")
    
    print(f"type 'y' to continue with {answer}, or type 'n' to start :")
    flag=input()

    if flag=="y":
      answer=answer2
      answer2=0

    else:
      clear()
      calculator()

calculator()
