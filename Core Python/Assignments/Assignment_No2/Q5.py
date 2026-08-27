# WAP to calculate selling price of book based on cost price and discount.

cost_price=int(input('Enter the cost price of book:'))
discount=int(input('Enter the discount:'))

total_discount=cost_price*discount/100
selling_price=cost_price-total_discount
print(f'Selling price of book based on cost price and discount is {selling_price}.')