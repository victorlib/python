import pygal
from random import randint


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


# 创建三个D6骰子
die_1 = Die()
die_2 = Die()
die_3 = Die()

# 掷几次骰子， 并将结果存储在一个列表中
results = [die_1.roll()+die_2.roll()+die_3.roll() for i in range(50000)]

# 分析结果
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(i) for i in range(3, max_result + 1)]

# 对结果可视化
hist = pygal.Bar()
hist.title = "Results of rolling three D6 50,000 times."
hist.x_labels = list(range(3, max_result + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('三个D6骰子.svg')

