class HashTable:
    def __init__(self, size=7):
        self.size = size
        self.data_map = [None] * size

    def __hash(self, key):
        hash_code = 0
        for letter in key:
            hash_code = (hash_code + ord(letter) * 23) % len(self.data_map)
        return hash_code

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []  # Initialize the index to an empty list
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def remove_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    self.data_map[index].pop(i)
                    return True  # Successfully removed
        return False  # Key not found

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ':', val)




h1 = HashTable()
h1.set_item("name","Quincy")
h1.print_table()
print('******************************\n')
h1.set_item("Washer","Susmita")
h1.print_table()
print('******************************\n')
h1.set_item("Officer","Cameran")
h1.print_table()
print('******************************\n')
h1.set_item("Lady","Elizabeth")
h1.print_table()
print('******************************\n')
h1.set_item("Hunter","Jhon")
h1.print_table()
print('******************************\n')
h1.set_item("Doctor","Thomas")
h1.print_table()
print('******************************\n')
print("The keys are:",h1.keys())
print(h1.get_item('Doctor'))



