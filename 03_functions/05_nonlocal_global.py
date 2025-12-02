# Non Local
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        # nonlocal chai_type
        chai_type = "Kesar"
    print("Before Kitchen:",chai_type)
    kitchen()
    print("After Kitchen:",chai_type)

update_order()

#Global access
chai_order = "Plain"
def front_desk():
    def kitchen():
        global chai_order
        chai_order = "Ginger"
    print("Before kitchen:",chai_order)
    kitchen()
    print("After kitchen:",chai_order)

print("Global update:",chai_order)
front_desk()
print("Global update:",chai_order)