tea_prices_inr = {
    "Masala Chai":40,
    "Green Tea":80,
    "Assamese Tea":200
}

tea_prices_usd = {tea: price/80 for tea,price in tea_prices_inr.items()}
print(tea_prices_usd)