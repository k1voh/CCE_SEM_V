#make a class and derived class to input some values and print them


class vehicle:
    
    def __init__(self):
        pass
    
    def __init__(self,v_id,own,manu):
        self.id = v_id
        self.own = own
        self.manu = manu
        
class passenger(vehicle):
    
    def __init__(self):
        pass
    
    def __init__(self,v_id,own,manu,npas):
        super().__init__(v_id,own,manu)
        self.npas = npas
        
    def set_val(self):
        self.v_id = int(input("Enter Vehicle ID: \n"))
        self.own = input("Enter name of owner: \n")
        self.manu = input("Enter name of manufacturer: \n")
        self.npas = int(input("Enter number of passengers: \n"))
        
    def get_val(self):
        print(self.v_id, self.own, self.manu, self.npas)
        
P = passenger(12,"Joseph","Hyundai",3)
P.set_val()
P.get_val()
