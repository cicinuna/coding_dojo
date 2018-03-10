import datetime

class Call(object):
    def __init__(self, id, name, number, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = datetime.datetime.now()
        self.reason = reason
    
    def display(self):
        print "Call ID is: {}.".format(self.id)
        print "Call name is: {}.".format(self.name)
        print "Call number is: {}.".format(self.number)
        print "Call time is: {}.".format(self.time)
        print "Call reason is: {}.".format(self.reason)

class Call_Center(object):
    def __init__(self):
        self.calls = []
        self.queue = len(self.calls)
    
    def add(self, new_call):
        self.calls.append(new_call)
        self.queue = len(self.calls)
        return self
    
    def remove(self):
        self.calls.pop(0)
        self.queue = len(self.calls)
        return self

    def remove_number(self, num):
        for i in range(0, self.queue-1):
            if self.calls[i].number == num:
                temp = self.calls[i]
                self.calls[i] = self.calls[i+1]
                self.calls[i+1] = temp
        self.calls.pop()
        self.queue = len(self.calls)
        return self

    def sort(self):
        for i in range(0, self.queue-1):
            if self.calls[i].time < self.calls[i+1].time:
                temp = self.calls[i]
                self.calls[i] = self.calls[i+1]
                self.calls[i+1] = temp
        return self

    def info(self):
        for i in range(0, self.queue):
            print "The Caller name is: {} and the phone number is: {}.".format(self.calls[i].name, self.calls[i].number)
        return self

call1 = Call("1", "Jason", "555-555-5555", "test")
call2 = Call("2", "Bosco", "123-555-5555", "test")
call3 = Call("3", "Nick", "456-555-5555", "test")
call4 = Call("4", "Steph", "789-555-5555", "test")

# call1.display()

center = Call_Center()

center.add(call1)
center.add(call2)
center.add(call3)
center.add(call4)

# center.info().remove().info()
# center.remove_number("123-555-5555").info()

center.info()