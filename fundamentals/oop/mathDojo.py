class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self,*nums):
        # your code here
        for num in nums:
            self.result += num
        return self

    def subtract(self, *nums):
        for num in nums:
            self.result -= num
        return self
md = MathDojo()
# to test:
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # should print 5
# run each of the methods a few more times and check the result!
md.result = 0
y=md.add(3,5,1,2,7).subtract(4,3,6).add(1).subtract(4).result
print(y)

md.result = 0
z=md.subtract(5,8,6,4,3).add(4,8,1).subtract(1).subtract(4).result
print(z)

md.result = 0
add_test = md.add(4,3).result
print(add_test)

md.result = 0
add_test = md.add(103,5,2).result
print(add_test)

md.result = 0
add_test = md.add(-4,5).result
print(add_test)

md.result = 0
sub_test = md.subtract(4,3).result
print(sub_test)

md.result = 0
sub_test = md.subtract(103,5,2).result
print(sub_test)

md.result = 0
sub_test = md.subtract(-4,5).result
print(sub_test)
