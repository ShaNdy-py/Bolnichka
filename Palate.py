class Palate():

    def __init__(self, palate_name, free = True, place_list = []):
        self.palate_name = palate_name
        self.place_list = place_list
        self.free = free

    def set_place_list(self, place_list):
        self.place_list = self.place_list + place_list

    def find_free_space(self):
        for i in self.place_list:
            if i.get_free() == True:
                return True
    
    def free_palate(self):
        a = False
        for i in self.place_list:
            if i.get_free() == True:
                a = a or True
            else:
                a = a or False
        self.free = a

    def get_place_list(self):
        return self.place_list

    def get_free(self):
        return self.free
                
    

class Place():
    
    def __init__(self, free = True, person = 1):
        self.free = free
        self.person = person

    
    def set_free(self, name):
        self.free = name

    def set_person(self, person):
        self.person = person

    def get_free(self):
        return self.free

    def get_person(self):
        return self.person
