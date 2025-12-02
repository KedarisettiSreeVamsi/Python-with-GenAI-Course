def pure_chai(cups):
    return cups * 10

total_chai = 0
def impure_chai(cups): #Not recommended
    global total_chai
    total_chai += cups * 10

# Recursive functions
def pour_chai(n):
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print((lambda x: x*2)(3))

chai_types = ["light","kadak","ginger","kadak"]
strong_chai = list(filter(lambda x: x != "kadak",chai_types))
print(strong_chai)
