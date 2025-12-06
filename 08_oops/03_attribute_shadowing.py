class Chai:
    temperature = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild" #Updating existing attribute
cutting.cup = "small" #New attribute
print("After changing",cutting.temperature)
print("Cup Size is ",cutting.cup)
print("Direct look into the class",Chai.temperature)

del cutting.temperature
print("After deleting",cutting.temperature) #Fallbacks to class value

del cutting.cup
print("Cup Size:"+cutting.cup) #AttributeError as there is no fallback