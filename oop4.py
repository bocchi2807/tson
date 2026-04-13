#project cuối
class xetai:   
    def __init__(self,license_plate,max_weight):
        self.license_plate=license_plate
        self.max_weight=max_weight
        self.hang=0#nếu muốn tính cân nặng hãy để n là số 0 hoặc số bất kì, vật thì là list
    def kiem_tra_xe(self):
        if  self.hang>self.max_weight:
            return 'xe tải nhỏ không chở nổi'
        else:
            return 'đủ để chở'
class xecontainer(xetai):
    def __init__(self,license_plate,max_weight,container_code):
        super().__init__(license_plate,max_weight)
        self.container_code=container_code
    def kiem_tra_xe(self):
        if self.hang>20:
            return 'cần xe dẫn đoàn'
        else:
            return 'xe này thì cân hết'
class dieuphoixe:
    def __init__(self,company_name,list_xe=None):
        self.company_name=company_name
        self.list_xe=[]#ban đầu chưa cso gì cả thì để là list,vì đây là xe
    def them_xe_moi(self,xe):
        self.list_xe.append(xe)
    def  goi(self,weight_hang):#weight_hang là cái mà sẽ được ghi ở dưới ,có nghãi đây là 1 hàm giả định,con số giả định này sẽ so sánh vs x.max_weight ở lis_xe
        found=False
        for x in self.list_xe:
            if x.max_weight >= weight_hang:# x là xe trong list,vậy x.max_weight là cân nặng và p so sánh 2 cân nặng vs nhau
                print('điều xe: ',x.license_plate,'đi giao hàng')
                self.list_xe.remove(x)# đuổi xe1 ra khỏi Gara.
                found=True
                break#tìm đc xe r thì dừng
        if not found:
                print('không xe nào chở được: ',weight_hang)
#đầu tiên p có chủ xe để quản lí           
tmu_fleet = dieuphoixe("TMU Logistics")
xe1 = xetai("29A-123", 2000)
xe2 = xecontainer("15C-456", 30000, "CONT_A")
#chủ cty tmu sẽ nhập xe vào bãi thông qua hàm append
tmu_fleet.them_xe_moi(xe1)#chủ thêm 2 xe mình quản lí vào hàm append
tmu_fleet.them_xe_moi(xe2)
tmu_fleet.goi(500)#thực chất 500 này là hàm gdinh,là weight_hang,Có đơn 500kg, xe nào đi được không?",sẽ tìm 2 xe ở trong list
tmu_fleet.goi(60000)#goi hàm này là 60000=weight_hang,sau đó ngta sẽ lấy x.max_weight(thực chất là cân nặng cảu xe có trong list để so sánh)
print(xe1.kiem_tra_xe())





