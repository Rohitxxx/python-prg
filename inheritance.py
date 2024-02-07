#single
class base:
    def basef(self):
        print('single  base')
class child(base):
    def childf(self):
        print('single child')
single=child()
single.basef()
single.childf()

#multilevel
class A:
    def Af(self):
        print("A")
class B(A):
    def Bf(self):
        print("B")
class C(B):
    def Cf(self):
        print("C")

multilevel=C()
multilevel.Af()
multilevel.Bf()
multilevel.Cf()


#multiple

class Parent1:
    def p1(self):
        print("Parent1")
class Parent2:
    def p2(self):
        print("Parent2")
class Child(Parent1,Parent2):
    def c1(self):
        print("child")

multiple=Child()
multiple.p1()
multiple.p2()
multiple.c1()