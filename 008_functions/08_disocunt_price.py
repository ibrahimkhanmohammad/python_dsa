def discount_price(original_price, discount):
    final_price = original_price * (1 - discount / 100)
    print(f'The final discount price is {final_price}')

discount_price(649, 25)