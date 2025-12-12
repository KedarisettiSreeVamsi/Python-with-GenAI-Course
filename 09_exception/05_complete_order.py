class InvalidChaiError(Exception): pass

def bill(flavor,cups):
    menu = {'masala':20,'ginger':15,'matcha':400}
    try:
        if flavor not in menu:
            raise InvalidChaiError(f"{flavor} chai is not available")
        if not isinstance(cups,int):
            raise TypeError("Number of cups must be integer")
    except InvalidChaiError as ice:
        print(ice)
    except TypeError as te:
        print(te)
    else:
        total = menu[flavor] * cups
        print(f"The total bill for {cups} cups of {flavor} chai is {total}.")
    finally:
        print("Thanks for visiting ChaiCode!")

bill("mint",2)
bill("masala",'three')
bill("matcha",5)
