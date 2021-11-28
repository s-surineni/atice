def chef_stock_price():
    tc = int(input().strip())

    for _ in range(tc):
        price, low, high, change = [int(i) for i in input().strip().split()]
        perc = 100 + change
        new_price = price * perc // 100
        if low <= new_price <= high:
            print("Yes")
        else:
            print("No")


(chef_stock_price())
