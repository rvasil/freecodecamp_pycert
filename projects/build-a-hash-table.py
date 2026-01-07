class HashTable:
    def __init__(self):
        self.collection = {}

    def __str__(self):
        return str(self.collection)

    def hash(self, key: str) -> int:
        if not isinstance(key, str):
            raise ValueError("Key must be a string")
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value

    def add(self, key: str, value):
        h = self.hash(key)
        if h not in self.collection:
            self.collection[h] = {}
        self.collection[h][key] = value

    def remove(self, key: str):
        h = self.hash(key)
        if h in self.collection:
            found = self.collection[h]
            if key in found:
                del self.collection[h][key]
                if len(found) == 0:
                    del self.collection[h]

    def lookup(self, key: str):
        h = self.hash(key)
        if h in self.collection:
            return self.collection[h].get(key, None)
        return None


# ht = HashTable()
# ht.add("golf", "sport")
# print(ht)
# ht.add("gofl", "other")
# print(ht)
# print("lookup golf:", ht.lookup("golf"))
# print("lookup gofl:", ht.lookup("gofl"))
# # ht.add('abb', 'bbb')
# ht.remove("golf")
# print("lookup golf after remove:", ht.lookup("golf"))
# print(ht)
# print("final:", ht)
