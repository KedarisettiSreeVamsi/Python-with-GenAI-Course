def serve_chai():
    chai_type = "Masala" #local scope
    print(f"Inside function {chai_type}")

chai_type = "Ginger" #Global
serve_chai()
print(f"Outside function {chai_type}")


def chai_counter():
    chai_order = "Lemon" #Enclosing scope
    def print_order():
        chai_order = "Ginger"
        print(f"Inner: {chai_order}")
    print("Outer scope:",chai_order)
    print_order()

chai_counter()