class good(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def add(self):
        return self.v1 + self.v2

    def subtract(self):
        return self.v1 - self.v2

def sum(a, b):
    return a+b

c1 = good(10,10)
print(c1.add())