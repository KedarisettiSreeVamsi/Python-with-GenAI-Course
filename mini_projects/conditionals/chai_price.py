size = input('How big cup of chai do you need?')

sizePrice = {
    'small':'10',
    'medium':'15',
    'large':'20'
}
if size.lower() in sizePrice.keys():
    print(f'Amount to be paid: {sizePrice[size.lower()]}')
else:
    print(f"The cup which you mentioned {size} is not available in the list of {sizePrice.keys()}")