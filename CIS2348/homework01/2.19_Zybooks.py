#Mariam Vaid
#1477614

lem = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
serving = float(input("How many servings does this make?\n"))

print("\nLemonade ingredients - yields {:.2f} servings".format(serving))
print("{:.2f} cup(s) lemon juice".format(lem))
print("{:.2f} cup(s) water".format(water))
print("{:.2f} cup(s) agave nectar".format(agave))

desi = float(input("\n How many serving would you like to make?\n"))
print("\nLemonade Ingredients - yields {:.2f} serving".format(desi))
print("{:.2f} cup(s) lemon juice".format(lem * desi / serving))
print("{:.2f} cup(s) water".format(water * desi / serving))
print("{:.2f} cup(s) agave nectar".format(agave * desi / serving))

print("\nLemonade ingredients - yields {:.2f} servings".format(desi))
print("{:.2f} cup(s) lemon juice".format(lem * desi / serving/16))
print("{:.2f} cup(s) water".format(water * desi / serving/16))
print("{:.2f} cup(s) agave nectar".format(agave * desi / serving/16))
