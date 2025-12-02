def make_chai(milk,tea,sugar):
    print(milk,tea,sugar)

make_chai("Yes","darjelling","low") #positional
make_chai("Yes","Assamese","High")

# keyword
make_chai(tea="Green",sugar="Low",milk="No")

print("Args and kwargs:")
def special_chai(*ingredients,**extras):
    print(ingredients) #arguments (args)
    print(extras) #keyword arguments (kwargs)

special_chai("Cinnamon","Cardamom",sweetner="Honey",foam="Yes")

print("Default trap:")
def chai_order(order=[]): #list as default value goes to default traps as it is mutable entity
    order.append("Masala")
    print(order)

chai_order()
chai_order()

print("Default trap prevention:")
def chai_order(order=None): #this prevents the default traps
    if order is None:
        order = []
    order.append("Masala")
    print(order)

chai_order()
chai_order()