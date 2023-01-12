sweets=int(input("How meny sweet do u have"))
people=int(input("How many people do the sweet need to be split between"))
how_many_each=sweets // people
left_over=sweets % people
print("Each person will get ", how_many_each, "sweet with", left_over, "sweets left over,")
print("")
print("Enter your player code that you want youritem to be stored in ")
playercode = int(input())
if playercode <= 1000:
    print("Well done u have succesluly")
else:
   print("sorry try agin latter")
   print("")

