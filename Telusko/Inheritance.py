
class A:
    def feature1(self):
        print("Hello from feature1")


class B(A):# single lebel inheritance
    def feature2(self):
        print("Hello from feature2")


class C(B, A):# multi lebel inheritance, make sure we giving B first then A for inherite order
    def feature3(self):
        print("Hello from feature3")


f1 = A()
f2 = B()
f3 = C()

f1.feature1()
f2.feature2()

f2.feature1()
f3.feature1()

# Multiple inheritance
class X: #parent class
    def show1(self):
        print("Hello from feature1")


class Y(): #parent class
    def show2(self):
        print("Hello from feature2")


class Z(X, Y):  #multiple inheritance
    def show3(self):
        print("Hello from feature3")


p1 = X()
p2 = Y()
p3 = Z()


p1.show1()
p2.show2()
#multiple inheritance
p3.show1()
p3.show2()
