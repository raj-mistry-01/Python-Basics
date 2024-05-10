# havung same methods with same name with different args  in same class.
class c1 :
    def add(self,a,b):
        return a+b
    def add(self,a,b,c) :
        return a+b+c
    
obj1=c1()
# print(obj1.add(2,3)) will lead to an  error. 

# because same method name will be overloaded.

# solution of the above 
class sol :
    def add(self,*args) :
        total = 0
        for i in args :
            total = total + i
        return total
c1 = sol()
print(c1.add(1,2,3))
print(c1.add(190,209,1083,19736,18386,27275))

# method Overriding
# atleast have class in that two class having method overloading.

class c1 :
    def sleep (self) :
        print("from 11pm to 7am.")

class c2 (c1) :
    def sleep(self) :
        print("from 2am to 7am.")
        c1.sleep(self)
        

obj = c2()
print(obj.sleep()) # executing to both.ss