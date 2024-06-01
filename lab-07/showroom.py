class Node:

    def __init__(self, nextNode, prevNode, data):
        self.nextNode = nextNode
        self.prevNode = prevNode
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.nextNode

    def car_insert(self, car):
        # 
        if self.head ==None:
            self.head = Node(None, None, car)
            self.tail = self.head
            self.length +=1
        elif self.head.data == None:
            self.head.data = car
            self.tail = self.head
            self.length +=1
        else:
            for node in self:
                if node.data.price <= car.price:
                    if node.nextNode == None:
                        new_node = Node(None, node,car)
                        node.nextNode = new_node
                        self.length +=1
                        self.tail = new_node
                        break
                    continue
                else:
                    if(node.prevNode == None):
                        new_node = Node(None, self.head, self.head.data)
                        self.head.nextNode = new_node
                        self.head.data = car
                    else:
                        new_node = Node(node, node.prevNode,car)
                        node.prevNode.nextNode = new_node
                        node.prevNode = new_node
                    self.length +=1
                    break
    
    def find_by_id(self, id):
        for node in self:
            if node.data.identification == id:
                return node
    
    def update_name(self, id, name):
        if self.find_by_id(id) != None:
            self.find_by_id(id).data.name = name

    def update_brand(self, id, brand):
        if self.find_by_id(id) != None:
            self.find_by_id(id).data.brand = brand
            

    def activate_car(self, id):
        if self.find_by_id(id) != None:
            self.find_by_id(id).data.active = True

    def deactivate_car(self, id):
        if self.find_by_id(id) != None:
            self.find_by_id(id).data.active = False

    def culc_active_prices(self):
        active_prices = 0
        for node in self:
            if node is None:
                continue
            if node.data.active:
                active_prices += node.data.price
        return active_prices 

    def PopEnd(self):
        if(self.head == None):
            return
        tmp_nd = self.tail.prevNode
        # tmp_nd == None
        if tmp_nd == self.head or tmp_nd == None:
            self.tail = None
            self.head = None
            self.length-=1
        else:
            self.tail = tmp_nd
            tmp_nd.nextNode = None
        self.length -= 1

    def clean(self):
        while self.tail != None:
            self.PopEnd()

class Car:
    def check_properties(self, identification, name, brand, price, active):
        if(isinstance(identification,int) and isinstance(name,str) and isinstance(brand,str) and isinstance(price,int) and isinstance(active,bool)):
            return True
        return False

    def __init__(self, identification, name, brand, price, active):
        if self.check_properties(identification,name,brand,price,active):
            self.identification = identification
            self.name = name
            self.brand = brand
            self.price = price
            self.active = active
        else:
            return None



db = LinkedList()

car_au = Car(1, "Audi", "Audi", 1222, True)
car_bmw = Car(2, "BMW", "BMW", 45450, True)
car_tesla = Car(3, "Tesla", "Tesla", 5659, True)
Oct = Car(4 , "Octavia",  "Skoda" , 123000 , False)
Fel =  Car(23,"Felicia","Skoda", 5000 , True)
cars = [car_au, car_bmw, car_tesla, Oct, Fel]
def add(car):
    db.car_insert(car)

def init(cars):
    for car in cars:
        add(car)

init(cars)

def updateName(identification, name):  
    db.update_name(identification, name)

updateName(23, "DKSKS")
print("zdvfds")

def updateBrand(identification, brand):
    db.update_brand(identification, brand)

def activateCar(identification):
    db.activate_car(identification)

def deactivateCar(identification):
    db.deactivate_car(identification)

def getDatabaseHead():
    return db.head
def getDatabase():
    return db

def calculateCarPrice():
    return db.culc_active_prices()
def clean():
    db.clean()


getDatabase()
getDatabaseHead()

activateCar(23)
deactivateCar(1)
deactivateCar(4)
x= calculateCarPrice()
print(x)
clean()
print("=========")
