#project oop
class parcel:#parcel là kiện hàng cũ trong kho
    def __init__(self,name,weight,_base_price):
        self.name=name
        self.weight=weight
        self._base_price=_base_price
    @property
    def shipping_fee(self):
        return self._base_price*1.1
    def __str__(self):
        return f'{self.name} {self.weight}'
class fragile(parcel):
    def __init__(self,name,weight,_base_price,padding_thickness):
        super().__init__(name,weight,_base_price)
        self.padding_thickness=padding_thickness
    @property#dùng property 2 lần để đổi riêng thuộc tính của cái mình muốn
    def shipping_fee(self):
        return self._base_price+(self.padding_thickness)*20
    def __str__(self):
        return('hàng dễ vỡ: ',self.name)
class cargoship:
    def __init__(self,ship_name,max_load,parcel):
        self.ship_name=ship_name
        self.max_load=max_load
        self.parcel=parcel
    def add_parcel(self,item):#kien 1,2 sẽ ngồi ở đây đợi cộng vào
        tong_hien_tai=0
        for p in self.parcel:#p là parcel là đồ cũ trong kho
            tong_hien_tai=tong_hien_tai+p.weight
        if tong_hien_tai+item.weight>self.max_load:
            print('tàu quá tải,bỏ lại kiện tên: ',self.ship_name)
        else:
            self.parcel.append(item)
            print('tàu có thể lưu thông')
    @staticmethod
    def check_weather(status):
        if status=='storm':
            return 'tàu không được xuất bến'
        else:
            return'thuận buồm xuôi gió'
    def __call__(self):#nó sẽ in ra bảng kê khai tổng tiền phí vận chuyển mà tàu sẽ thu được.
        doanh_thu=0
        for kienhang in self.parcel:#có tổng khả năng cao dùng for,vì phải lặp đi lặp lại 1 bước để ra được tổng
            doanh_thu=doanh_thu+kienhang.shipping_fee
        print('tổng tiền: ',doanh_thu)
tau_tmu = cargoship("TMU Logistics", 100, [])
kien_1 = parcel("Laptop Dell", 10, 1000)      # Hàng thường
kien_2 = fragile("Bình cổ", 5, 2000, 5)       # Hàng dễ vỡ
kien_3 = parcel("Tủ lạnh mini", 95, 5000)     # Hàng này siêu nặng
tau_tmu.add_parcel(kien_1)#đóng vai trò item
tau_tmu.add_parcel(kien_2)#item mới
tau_tmu.add_parcel(kien_3)


        
        
