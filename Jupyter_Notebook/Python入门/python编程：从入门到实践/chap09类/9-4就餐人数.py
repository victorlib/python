from chap09类.common import Restaurant

r = Restaurant('火锅店', '麻辣')
print(r.number_served)
r.number_served = 50
print(r.number_served)
r.set_number_served(70)
print(r.number_served)
r.increment_number_served(30)
print(r.number_served)