import hashlib

class HashTable:
    def __init__(self, size=8):
        self.table = [[None] for _ in range(size)]

    '''calculate key hash and where index '''
    def hash(self, key):
        hash_hex = hashlib.sha256(key.encode()).hexdigest() # get hexdecimal
        index = int(hash_hex, 16) # convert to integer
        return index


        '''if key dosen't exist create it if exist and value are diffrent update value'''
    def create_update(self, key, value):
        pass


    def delete(self, key):
        pass


    def search(self, key):
        pass