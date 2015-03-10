class Ph():
    '''
    Person do something woud be relative money
    '''
    #the same
    
    def __init__(self,name,money):
        self.name=name
        self.money=money
    def eat(self,food):
        if(food == "breakfirst"):
            self.money -=50
        elif(food == "lunch"):
            self.money -=100
        elif(food == "dinner"):
            self.money -= 100
    def take(self,work):
        if(work == "teacher"):
            self.money +=50000
        elif(work =="student"):
            self.money -=20000
        elif(work =="iOS"):
            self.money+=60000
Yenlung=Ph("Yenlung",50000)
Yenwun=Ph("Yenwun",30000)
Mingyi=Ph("Mingyi",10000)


print Yenlung.name +" "+str(Yenlung.money)
for i in range(3):
    Yenlung.eat("breakfirst")
    Yenlung.eat("lunch")
    Yenlung.eat("dinner")
    print "Today is 2015.03.0"+str(i)+" and release $"+ str(Yenlung.money)+"."

