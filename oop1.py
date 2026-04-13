#test oop1
class vehicle:#lớp cha
    def __init__(self,brand,model,base_price):
        self.brand=brand
        self.model=model
        self._base_price=base_price#đã đóng gói price
    @property 
    def fullname(self): 
        return f'{self.brand} {self.model}' 
    @fullname.setter
    def fullname(self,fullname):
        brand,model=fullname.split(' ')
        self.brand=brand
        self.model=model
    def calculate_cost(self):
        return '{self.base_price}'#Mọi thứ nằm trong Class, hễ muốn dùng là phải có self.
class truck(vehicle):#kế thừa từ vehicle
    def __init__(self,brand,model,base_price,payload):
        super().__init__(brand,model,base_price)
        self.payload=payload
    def calculate_cost(self):
        return self._base_price+(self.payload)*100
class drivers:
    def __init__(self,name,experience):
        self.name=name 
        self.experience=int(experience)
    def __repr__(self):
        return  f'{self.name}{self.experience}'
    def __add__(self,other):
        return self.experience+ other.experience
class logisticmanager():
    company_name='TMU Logistic'
    def __init__(self,drivers=None):
        self.drivers=drivers
        if drivers is None:
            self.drivers=[]
        else:
            self.drivers=drivers
    @staticmethod 
    def check_payload(payload):
        if payload<=15:
            return 'xe này thiếu dinh dưỡng'
        else:
            return 'xe đủ tiêu chuẩn'
            
xe1=truck('hino','500 series',500,15)
drv1=drivers('nam',3)
drv2=drivers('son',5)
print(drv1+drv2)
print(xe1.fullname)
print(logisticmanager.check_payload(xe1.payload))
xe1.calculate_cost()
print(xe1.calculate_cost())
log1=logisticmanager([drv1,drv2])
print('ng đầu tiên là: ',log1.drivers[0].name,'số năm kinh nghiệm: ',log1.drivers[0].experience)
drv1.__repr__()
print(drv1.__repr__())
xe1.calculate_cost()
print(xe1.calculate_cost())
xe1.fullname
print(xe1.fullname)

























