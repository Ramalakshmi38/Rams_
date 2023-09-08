num=int(input("Enter a num"))
fact=1
if num<0:
  print("Negative num")
elif num==0:
  print("The factorial of a given num 0 is 1")
else:
  for i in range(1,num+1):
   fact=fact*i
print(fact)