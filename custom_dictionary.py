class MyDict:
    def __init__(self):
        self._keys = []
        self._values = []

    def __getitem__(self, key):
        if key in self._keys:
            index = self._keys.index(key)
            return self._values[index]
        return None

    def __setitem__(self, key, value):
        if key in self._keys:
            index = self._keys.index(key)
            self._values[index] = value
        else:
            self._keys.append(key)
            self._values.append(value)

    def __delitem__(self, key):
        if key in self._keys:
            index = self._keys.index(key)
            self._keys.pop(index)
            self._values.pop(index)

    def keys(self):
        return self._keys.copy()

    def values(self):
        return self._values.copy()

    def items(self):
        result = []
        for i in range(len(self._keys)):
            result.append((self._keys[i], self._values[i]))
        return result

    def __str__(self):
        return str(dict(self.items()))


my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
