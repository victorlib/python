# -*- coding:utf-8 -*-


print('a,b,c'.split(','))
print('this is my string'.split())

s = ' this  is my string '
print(s.split())
print(s.split(' '))

s = 'this is my string'
print(s.split(maxsplit=2))


input_string = """Name,Phone,Address
Mike Smith,15554218841,123 Nice St, Roy, NM, USA
Anita Hernandez,15557789941,425 Sunny St, New York, NY, USA
Guido van Rossum,315558730,Science Park 123, 1098 XG Amsterdam, NL"""

def string_split_ex(unsplit):
    results = []

    # Bonus points for using splitlines() here instead, 
    # which will be more readable
    for line in unsplit.split('\n')[1:]:
        results.append(line.split(',', maxsplit=2))

    return results

print(string_split_ex(input_string))


print(ord('李'))
print(chr(26446))

n = 20
m = 25
prod = n * m
print(f'The product of {n} and {m} is {prod}')

# modifying strings
s = 'foobar'
s = s[:3] + 'x' + s[4:]
print(s)










































