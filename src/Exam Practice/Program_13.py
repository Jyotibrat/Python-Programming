class Grand_Parent: # Hybrid Inheritance
    def grand_parent(self):
        print("I am the Grand Parent")

class Parent(Grand_Parent): # Single Inheritance
    def parent(self):
        obj = Grand_Parent()
        obj.grand_parent()
        print("I am the Parent")

class Child1(Parent, Grand_Parent): # Multiple Inheritance
    def child1(self):
        obj = Parent()
        obj.parent()
        print("I am Child 1")

class Child2(Child1): # Multilevel Inheritance
    def child2(self):
        obj = Child1()
        obj.child1()
        print("I am Child 2")

class Mother(Grand_Parent): # Hierarchical Inheritance
    def mother(self):
        obj = Grand_Parent()
        obj.grand_parent()
        print("I am the Mother")

obj1 = Child2()
obj1.child2()

obj2 = Mother()
obj2.mother()