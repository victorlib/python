# example.py
#
# Example of calculating with dictionaries

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM' : 205.55,
    'HPQ' : 37.20,
    'FB'  : 10.75
}

print('-'*20)
for i in zip(prices.values(), prices.keys()):
    print(i)
print('-'*20)
print(zip(prices.values()))

# Find min and max price
#min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
min_price = min(zip(prices.keys(), prices.values()))
min_ = min(prices)
print('min_:', min_)

print('min price:', min_price)
print('max price:', max_price)

print('sorted prices:')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
for price, name in prices_sorted:
    print('    ', name, price)


# learn zip()
x = [3, 2]
y = [1, 5]
z = [2, 8]
xyz = zip(x, y, z)
for i in xyz:
    print(i)
