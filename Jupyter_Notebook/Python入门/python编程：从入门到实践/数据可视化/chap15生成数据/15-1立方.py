import matplotlib.pyplot as plt

x_value = list(range(1, 5001))
y_value = [x**3 for x in x_value]
plt.plot(x_value, y_value, linewidth=3)
plt.title("cube")
plt.xlabel("x")
plt.ylabel("y")
plt.axis([0, 5100, 0, 130000000000])
plt.show()
