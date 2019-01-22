import pygal
from random import randint


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


# 创建两个D6骰子
die_1 = Die()
die_2 = Die()

# 掷几次骰子， 并将结果存储在一个列表中
results = [die_1.roll()*die_2.roll() for i in range(50000)]

# 所有结果的可能
x_label = sorted(set([i*j for i in range(1, die_1.num_sides+1) for j in range(1, die_2.num_sides+1)]))

# 分析结果
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(i) for i in x_label]

# 对结果可视化
hist = pygal.Bar()
hist.title = "Results of rolling two D6 50,000 times."
hist.x_labels = x_label
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 * D6', frequencies)
hist.render_to_file('两个D6骰子点数相乘.svg')

