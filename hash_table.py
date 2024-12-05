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


        '''Create key-value pair or Update the value if the key exist'''
    def create_update(self, key, value):
        index = self.hash(key)

        if self.table[index] is None: # If is empty
            self.table[index] = Node(key, value) # Create new node
            print(f"Key ---> '{key}' added with value ---> '{value}' at index ---> {index}.")

        else:
            current = self.table[index]
            while current:

                if current.key == key:  # If key is the same just update value
                    current.value = value
                    print(f"Key ---> {key} updated with new value ---> {value}")

                if current.next is None:
                    break # Find last node

                '''Create new node in end of the list'''
                current = current.next
                new_Node = Node(key, value)
                current.next = new_Node # chained new node as next node of current
                new_Node.prev = current # chained current node as previous node
                print(f"Collision handled: Key '{key}' added with value '{value}'.")

    def delete(self, key):
        pass


    def search(self, key):
        pass