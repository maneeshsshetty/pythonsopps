price=int(input("enter the price of the item: \n"))
quantity=int(input("enter the quantity of the item: \n"))
total=price*quantity
if (total>1000):
    discount=total*0.1
    final_price=total-discount
    print("the original price is:",total)
    print("the discounted price is: ",final_price)
else:
    print("total price:",total)