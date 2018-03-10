# Part 1

class MathDojo(object):

    def __init__(self):
        self.sum = 0

    # def add(self, a, b):
    #     return a+b
    def add(self, a, b=None):
        if b == None:
            self.sum += a
        else: 
            self.sum += a + b
        return self
    
    def subtract(self, a, b=None):
        if b == None:
            self.sum -= a  
        else: 
            self.sum = self.sum - (a+b)
        return self

    def result(self):
        print self.sum

md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()

# Part 2 and 3

class MathDojoTwo(object):
    def __init__(self):
        self.sum = 0

    def add(self, a, *b):
        if b == None:
            if type(a) == int or type(a) == float:
                self.sum += a
            elif type(a) == list:
                self.sum += sum(a)
            elif type(a) == tuple:
                self.sum += sum(a)
            return self
        else:
            if type(a) == int and type(b) == int or type(a) == float and type(b) == int or type(a) == int and type(b) == float:
                self.sum += (a + b)
            elif type(a) == int and type(b) == list or type(a) == float and type(b) == list:
                self.sum += (a + sum(b))
            elif type(a) == int and type(b) == tuple or type(a) == float and type(b) == tuple:
                if type(b[0]) == list and len(b) > 1:
                    for i in range(0,len(b)):
                        self.sum += sum(b[i])
                    self.sum += a
                elif type(b[0]) == list and len(b) == 1:
                    self.sum += (a + sum(b[0]))
                else: 
                    self.sum += (a + sum(b))
            elif type(a) == list and type(b) == int or type(a) == list and type(b) == float:
                self.sum += (sum(a) + b)
            elif type(a) == list and type(b) == list:
                # print "here"
                self.sum += (sum(a) + sum(b))
            elif type(a) == list and type(b) == tuple:
                if type(b[0]) == list and len(b) > 1:
                    # print "here"
                    for i in range(0,len(b)):
                        self.sum += sum(b[i])
                    self.sum += sum(a)
                elif type(b[0]) == list and len(b) == 1:
                    self.sum += (sum(a) + sum(b[0]))
                else: 
                    self.sum += (sum(a) + sum(b))
            elif type(a) == tuple and type(b) == int or type(a) == tuple and type(b) == float:
                if type(a[0]) == list and len(a) > 1:
                    for i in range(0,len(a)):
                        self.sum += sum(a[i])
                    self.sum += b
                elif type(a[0]) == list and len(a) == 1:
                    self.sum += (b + sum(a[0]))
                else: 
                    self.sum += (sum(a) + b)
            elif type(a) == tuple and type(b) == list:
                if type(a[0]) == list and len(a) > 1:
                    for i in range(0,len(a)):
                        self.sum += sum(a[i])
                    self.sum += sum(b)
                elif type(a[0]) == list and len(a) == 1:
                    self.sum += (sum(b) + sum(a[0]))
                else: 
                    self.sum += (sum(a) + sum(b))
            elif type(a) == tuple and type(b) == tuple:
                if type(a[0]) == list and len(a) > 1 and type(b[0]) == int or type(a[0]) == list and len(a) > 1 and type(b[0]) == float:
                    for i in range(0,len(a)):
                        self.sum += sum(a[i])
                    self.sum += sum(b)
                elif type(a[0]) == list and len(a) == 1 and type(b[0]) == int or type(a[0]) == list and len(a) == 1 and type(b[0]) == float:
                    self.sum += (sum(a[0]) + sum(b))
                elif type(a[0]) == list and len(a) > 1 and type(b[0]) == list and len(b) > 1:
                    for i in range(0,len(a)):
                        self.sum += sum(a[i])
                    for i in range(0,len(b)):
                        self.sum += sum(b[i])
                elif type(a[0]) == list and len(a) == 1 and type(b[0]) == list and len(b) > 1:
                    for i in range(0,len(b)):
                        self.sum += sum(b[i])
                    self.sum += sum(a[0])
                elif type(a[0]) == list and len(a) > 1 and type(b[0]) == list and len(b) == 1:
                    for i in (0,len(a)):
                        self.sum += sum(a[i])
                    self.sum += sum(b[0])
                elif type(a[0]) == int and type(b[0]) == list  and len(b) > 1 or type(a[0]) == float and type(b[0]) == list and len(b) > 1:
                    for i in range(0,len(b)):
                        self.sum += sum(b[i])
                    self.sum += sum(a)
                elif type(a[0]) == int and type(b[0]) == list  and len(b) == 1 or type(a[0]) == float and type(b[0]) == list and len(b) == 1:
                    self.sum += (sum(a) + sum(b[0]))
            return self
    
    def subtract(self, a, *b):
        if b == None:
            if type(a) == int or type(a) == float:
                self.sum -= a
            elif type(a) == list:
                self.sum -= sum(a)
            elif type(a) == tuple:
                self.sum -= sum(a)
            return self
        else:
            if type(a) == int and type(b) == int or type(a) == float and type(b) == int or type(a) == int and type(b) == float:
                self.sum -= (a + b)
            elif type(a) == int and type(b) == list or type(a) == float and type(b) == list:
                self.sum -= (a + sum(b))
            elif type(a) == int and type(b) == tuple or type(a) == float and type(b) == tuple:
                if type(b[0]) == list and len(b) > 1:
                    for i in range(0,len(b)):
                        self.sum -= sum(b[i])
                    self.sum -= a
                elif type(b[0]) == list and len(b) == 1:
                    self.sum -= (a + sum(b[0]))
                else: 
                    self.sum -= (a + sum(b))
            elif type(a) == list and type(b) == int or type(a) == list and type(b) == float:
                self.sum -= (sum(a) + b)
            elif type(a) == list and type(b) == list:
                # print "here"
                self.sum -= (sum(a) + sum(b))
            elif type(a) == list and type(b) == tuple:
                if type(b[0]) == list and len(b) > 1:
                    # print "here"
                    for i in range(0,len(b)):
                        self.sum -= sum(b[i])
                    self.sum -= sum(a)
                elif type(b[0]) == list and len(b) == 1:
                    self.sum -= (sum(a) + sum(b[0]))
                else: 
                    self.sum -= (sum(a) + sum(b))
            elif type(a) == tuple and type(b) == int or type(a) == tuple and type(b) == float:
                if type(a[0]) == list and len(a) > 1:
                    for i in range(0,len(a)):
                        self.sum -= sum(a[i])
                    self.sum -= b
                elif type(a[0]) == list and len(a) == 1:
                    self.sum -= (b + sum(a[0]))
                else: 
                    self.sum -= (sum(a) + b)
            elif type(a) == tuple and type(b) == list:
                if type(a[0]) == list and len(a) > 1:
                    for i in range(0,len(a)):
                        self.sum -= sum(a[i])
                    self.sum -= sum(b)
                elif type(a[0]) == list and len(a) == 1:
                    self.sum -= (sum(b) + sum(a[0]))
                else: 
                    self.sum -= (sum(a) + sum(b))
            elif type(a) == tuple and type(b) == tuple:
                if type(a[0]) == list and len(a) > 1 and type(b[0]) == int or type(a[0]) == list and len(a) > 1 and type(b[0]) == float:
                    for i in range(0,len(a)):
                        self.sum -= sum(a[i])
                    self.sum -= sum(b)
                elif type(a[0]) == list and len(a) == 1 and type(b[0]) == int or type(a[0]) == list and len(a) == 1 and type(b[0]) == float:
                    self.sum -= (sum(a[0]) + sum(b))
                elif type(a[0]) == list and len(a) > 1 and type(b[0]) == list and len(b) > 1:
                    for i in range(0,len(a)):
                        self.sum -= sum(a[i])
                    for i in range(0,len(b)):
                        self.sum -= sum(b[i])
                elif type(a[0]) == list and len(a) == 1 and type(b[0]) == list and len(b) > 1:
                    for i in range(0,len(b)):
                        self.sum -= sum(b[i])
                    self.sum -= sum(a[0])
                elif type(a[0]) == list and len(a) > 1 and type(b[0]) == list and len(b) == 1:
                    for i in (0,len(a)):
                        self.sum -= sum(a[i])
                    self.sum -= sum(b[0])
                elif type(a[0]) == int and type(b[0]) == list  and len(b) > 1 or type(a[0]) == float and type(b[0]) == list and len(b) > 1:
                    for i in range(0,len(b)):
                        self.sum -= sum(b[i])
                    self.sum -= sum(a)
                elif type(a[0]) == int and type(b[0]) == list  and len(b) == 1 or type(a[0]) == float and type(b[0]) == list and len(b) == 1:
                    self.sum -= (sum(a) + sum(b[0]))
            return self

    def result(self):
        print self.sum

newmd = MathDojoTwo()
newmd.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()

