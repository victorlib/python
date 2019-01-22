import matplotlib.pyplot as plt
from random import choice


class RandomWalk:
    """一个生成随机漫步数据的类"""
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        # 所有随机漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        # 不断漫步， 直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice(list(range(9)))
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice(list(range(9)))
            y_step = y_direction * y_distance
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)


# 只要程序处于活动状态， 就不断地模拟随机漫步
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    # plt.figure(figsize=(10, 6))  # 单位为英寸,Python假定屏幕分辨率为80像素/英寸
    plt.figure(dpi=128, figsize=(10, 6))  # 如果你知道自己的系统的分辨率,可使用形参dpi向figure()传递该分辨率

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make anther walk? (y/n): ")
    if keep_running == 'n':
        break

