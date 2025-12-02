names = ['Hitesh','Vamsi','Chakri']
bills = [240,50,30]

sumVal = 0
for i,values in enumerate(zip(names,bills),start=1):
    print(f"{i}. {values[0]} - {values[1]}")
    sumVal += values[1]

print(f"Total Bill: {sumVal}")
