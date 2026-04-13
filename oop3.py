#project cuối oop
#hệ thống quản lí kho shopee
class hangthuong:
    def __init__(self,name,weight,area):
        self.name=name
        self.weight=weight
        self.area=area
    @property
    def philuukho(self):
        return self.area*5000
    def fullname(self):
        return f'{self.name} {self.weight} {self.area}'
class hangdientu(hangthuong):
    def __init__(self,name,weight,area,brand,warranty_fee):
        super().__init__(name,weight,area,)
        self.brand=brand 
        self.warranty_fee=warranty_fee
    @property 
    def philuukho(self):
        return (self.area*5000)+self.warranty_fee
    def fullname(self):
        return f'{self.name} {self.weight} {self.area}'
class khohang:
    def __init__(self,warehose_name,capacity_area,suchchuakho=None):
        self.warehose_name=warehose_name
        self.capacity_area=capacity_area
        self.suchchuakho=[]
    def nhap_hang(self,item):
        tong_area=0
        for monhang in self.suchchuakho:
            tong_area=tong_area+monhang.area
        if tong_area+item.area>self.capacity_area:
            return 'từ chối'
        else:
            self.suchchuakho.append(item)
    def __call__(self):
        doanh_thu=0
        for kienhang in self.suchchuakho:
            doanh_thu=doanh_thu+kienhang.philuukho
        print('tổng chi phí là: ',doanh_thu)
kho_shopee = khohang("Shopee HN", 50)
h1 = hangthuong("Quần jean", 1, 10)
h2 = hangdientu("Laptop Dell", 2, 5, "Dell", 100000)

kho_shopee.nhap_hang(h1)
kho_shopee.nhap_hang(h2)
kho_shopee()
print('phí lưu kho là: ',h1.philuukho)
h1.fullname
h2.fullname
print(h1.fullname)
print(h2.fullname)