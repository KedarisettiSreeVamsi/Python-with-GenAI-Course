def chai_flavor(flavor="masala"):
    "Returns the flavor of chai (default: masala)"
    return flavor

def generate_bill(chai=0,samosa=0):
    """
    Calculate the total bill for chai and samosa
    :param chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    :return (total_amount,thank you message)
    """
    total = chai*10 + samosa*15
    return total,"Thank you for purchasing chai and samosa"

print(chai_flavor.__doc__)
print(chai_flavor.__name__)