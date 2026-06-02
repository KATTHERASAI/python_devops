import sys
type = sys.argv[1]
if type == "t2.micro":
    print("ok we create the instance")

elif type == "t2.medium":
      print ("create t2 medium")
elif type == "t2.large":
      print ("create t2 large")
elif type == "t2.xl":
      print ("create t2 xl")
else:
    print("invalid output")
    