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

        if self.table[index] is None: # If the slot is empty
            self.table[index] = Node(key, value) # Create new node
            print(f"Key ---> '{key}' added with value ---> '{value}' at index ---> {index}.")

        else:
            current = self.table[index]
            while current:

                if current.key == key:  # If the key already exists, update the value
                    current.value = value
                    print(f"Key ---> {key} updated with new value ---> {value}")
                    return
                if current.next is None:
                    break # Find the last node in the chain

                '''Create new node in end of the list'''
                current = current.next
                new_Node = Node(key, value)
                current.next = new_Node # chain new node as next node of current
                new_Node.prev = current # chain current node as previous node
                print(f"Collision handled: Key '{key}' added with value '{value}'.")

    def delete(self, key):
        pass

    '''Find the value by key or return (not found!!) or None'''
    def search(self, key):
        index = self.hash(key)
        current = self.table[index]

        while current: # iterate on all nodes in that index
            if current.key == key:
                print(f"Key ---> '{current.key}' value ---> {current.value} found at index ---> {current  .index}.")
                return current.value
            current = current.next

        print(f"Key not Found!!!")
        return None