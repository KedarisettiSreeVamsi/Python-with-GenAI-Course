raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA",b"CARD")
print(f"Bytes:{raw_spice_data}")
print(bytes("CINNABON",'utf-8'))

essential_spices = {'cardamom','cinnamon','ginger'}
optional_spices = {'cloves','ginger','black pepper'}

# all the spices (union)
all_spices = essential_spices | optional_spices
print(all_spices)

# common set (intersection)
common_spices = essential_spices & optional_spices
print(common_spices)

# only first set & no common elements from second set(difference)
only_essential_spices = essential_spices - optional_spices
print(only_essential_spices)