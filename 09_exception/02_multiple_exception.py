def process_order(item,quantity):
    try:
        price = {"masala":20}[item]
        cost = price * int(quantity)
        print(f"Total cost is {cost}")
    except KeyError as k:
        print(f"Sorry the {item} chai is not on menu")
    except ValueError as t:
        print("Quantity must be integer")

process_order("ginger",2)
process_order("masala","two")