"""

在Entry类中修改__str__函数

def __str__(self):
    if len(self.text) > 50:
        return self.text[:50] + "..."
    return self.text

"""