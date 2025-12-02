list1 = [1,1,1,4,5,6,3,2,1,3,1,3,2,1]
unique_vals = {val for val in list1}
print(unique_vals)

recipes = {
    "Masala Chai":["ginger","cardamom","clove"],
    "Elaichi Chai":["elaichi"],
    "Spicy Chai":["ginger","black pepper","clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)