
def fib(n):  # return Fi
    bonacci series up to n
    """Return a list containing the Finonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result


f100 = fib(100)
print(f100)

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return


print(f(1))
print(f(2))
print(f(3))


def cheeseshop(kind, *argument, **keywords):
    print("-- Do you have any", kind, "?")

    for arg in argument:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop('liwenxing', 'It\'s very sunny, sir.',
        "It\'s really ver, sunny, sir.",
        shopkeeper = "Vincent",
        client = "John",
        sketch = "Cheese Shop Sketch"

print( list(range(3, 6)))


