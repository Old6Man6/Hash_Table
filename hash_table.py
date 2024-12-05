import hashlib

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class HashTable:
    def __init__(self, size=8):
        self.table = [[None] for _ in range(size)]

    '''Hash the key and find the index'''
    def hash(self, key):
        hash_hex = hashlib.sha256(key.encode()).hexdigest() # get hexdecimal
        index = int(hash_hex, 16) # convert to integer
        return index


        '''if key dosen't exist create it if exist and value are diffrent update value'''
    def create_update(self, key, value):
        index = self.hash(key)
        if self.table[index] is None:



    def delete(self, key):
        pass


    def search(self, key):
        pass