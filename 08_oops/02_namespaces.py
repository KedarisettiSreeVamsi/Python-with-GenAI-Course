class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

# creating objects from class Chai

masala = Chai()
print(masala.origin)
print(masala.is_hot)

masala.is_hot = False
print(Chai.is_hot) #True
print(masala.is_hot) #False

