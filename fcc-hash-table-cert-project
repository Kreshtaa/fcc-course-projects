class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        return sum(ord(c) for c in string)

    def add(self, key, value):
        h = self.hash(key)
        if h in self.collection:
            self.collection[h][key] = value
        else:
            self.collection[h] = {key: value}

    def remove(self, key):
        h = self.hash(key)
        if h in self.collection:
            self.collection[h].pop(key, None)
        self.collection.pop(key, None)
    
    def lookup(self, key):
        lookup_key_hash = self.hash(key)
        if not lookup_key_hash in self.collection:
            return None
        if not key in self.collection[self.hash(key)]:
            return None
        else:
            return self.collection[lookup_key_hash].get(key)
