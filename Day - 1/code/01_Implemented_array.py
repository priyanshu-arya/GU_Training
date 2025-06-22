class MyArray:
    def __init__(self):
        self.data = []
        self.length = 0

    def insert(self, value):
        self.data += [value]  
        self.length += 1

    def insert_at(self, index, value):
        if index < 0 or index > self.length:
            print("Index out of bounds.")
            return
        self.data = self.data[:index] + [value] + self.data[index:]
        self.length += 1

    def remove(self):
        if self.length == 0:
            print("Array is empty.")
            return
        self.data = self.data[:-1]
        self.length -= 1

    def remove_at(self, index):
        if index < 0 or index >= self.length:
            print("Index out of bounds.")
            return
        self.data = self.data[:index] + self.data[index+1:]
        self.length -= 1

    def get(self, index):
        if index < 0 or index >= self.length:
            print("Index out of bounds.")
            return None
        return self.data[index]

    def size(self):
        return self.length

    def print_array(self):
        print(self.data)


if __name__ == "__main__":
    arr = MyArray()
    arr.insert(10)
    arr.insert(20)
    arr.insert_at(1, 15)
    arr.print_array()        # Output: [10, 15, 20]
    arr.remove()
    arr.print_array()        # Output: [10, 15]
    arr.remove_at(0)
    arr.print_array()        # Output: [15]
    print(arr.get(0))        # Output: 15
    print(arr.size())        # Output: 1
