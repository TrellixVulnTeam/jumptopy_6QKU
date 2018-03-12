class FourCal:
    def setdata(self,first,second):
        self.first = first #Step out Shift+F8
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def sub(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second
    def mul(self):
        return self.first * self.second

a = FourCal()
a.setdata(4,2) # Step into F7

print(a.first)
print(a.second)
a.first = 1
a.second = 2
print(a.first)
print(a.second)

print(a.sum())

