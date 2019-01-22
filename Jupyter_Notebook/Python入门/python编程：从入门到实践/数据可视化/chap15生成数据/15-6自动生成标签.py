import pygal
from random import randint


class Die:
    """表示一个骰子的类"""
    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """"返回一个位于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)


# 创建一个D6骰子，一个D10骰子
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子， 并将结果存储在一个列表中
results = [die_1.roll()+die_2.roll() for i in range(50000)]


# 分析结果
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(i) for i in range(2, max_result + 1)]

# 对结果可视化
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = list(range(2, max_result + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')

