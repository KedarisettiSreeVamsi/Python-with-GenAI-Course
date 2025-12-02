names = input("Give names in a comma seperated fashion").split(',')
for i in range(len(names)):
    print(f"Serving chai for {names[i]}")

for i,name in enumerate(names,start=1):
    print(f"{i}. {name}")