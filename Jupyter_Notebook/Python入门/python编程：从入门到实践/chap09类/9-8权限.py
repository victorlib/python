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


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
        print()


class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)


a = Admin('chen', 'jiasheng', ['can add post', 'can delete post', 'can ban user'])
a.privileges.show_privileges()



