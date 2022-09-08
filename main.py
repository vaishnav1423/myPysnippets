x=int(input("Enter the number to test if Prime:"))

def checkprime(num):
  if ((num**2)-1)%24==0:
    return True
  else:
    return False

if (x<5 and x in (2,3)):
  print("prime")
elif checkprime(x):
  print("prime")
else:
  print("Not Prime")