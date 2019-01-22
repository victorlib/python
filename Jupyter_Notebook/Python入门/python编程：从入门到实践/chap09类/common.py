class Restaurant:
    def __init__(self, r_name, r_type):
        self.r_name = r_name
        self.r_type = r_type
        self.number_served = 0

    def describe(self):
        print('餐馆名字为：'+self.r_name)
        print('餐馆类型是：'+self.r_type)

    def open(self):
        print(self.r_name+'餐馆开业啦！！！')

    def set_number_served(self, n):
        self.number_served = n

    def increment_number_served(self, i):
        self.number_served += i


class IceCreamStand(Restaurant):
    def __init__(self):
        super().__init__('冰激凌小店', '冰激凌')
        self.flavors = ['香芋', '巧克力', '牛奶']

    def display_flavours(self):
        print('冰激凌口味如下：')
        for v in self.flavors:
            print(v)
        print('------------------------')


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe(self):
        print('name:'+self.first_name.title()+' '+self.last_name.title())

    def greet(self):
        print('hello, '+self.first_name.title()+' '+self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges

    def show_privileges(self):
        self.describe()
        for privilege in self.privileges:
            print(privilege)
        print()







