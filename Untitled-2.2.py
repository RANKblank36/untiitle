class U:
    def __init__(self, u):
        self.u = u
    def __lt__(self,other):
        if(self.u<other.u):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
    def __eq__(self, other):
        if(self.u == other.u):
            return "Both are equal"
        else: return "Not equal"

ob1 = U(5)
ob2 = U(3)
print("Passed Values :", ob1.u, ob2.u)
print(ob1 < ob2)

ob3 = U(8)
ob4 = U(8)
print("Passed Values :", ob3.u, ob4.u)
print(ob3 == ob4)