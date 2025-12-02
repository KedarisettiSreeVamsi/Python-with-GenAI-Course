snack = input("Provide either samosa/cookies or something else:")
if str(snack).lower() in ['samosa','cookies']:
    print("Order confirmed")
else:
    print("Stock unavailable")