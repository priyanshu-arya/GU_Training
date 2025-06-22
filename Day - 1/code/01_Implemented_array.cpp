#include <iostream>
#include <vector>

class MyArray {
private:
    std::vector<int> data;
    int length;

public:
    MyArray() : length(0) {}

    void insert(int value) {
        data.push_back(value);
        length++;
    }

    void insertAt(int index, int value) {
        if (index < 0 || index > length) {
            std::cout << "Index out of bounds." << std::endl;
            return;
        }
        data.insert(data.begin() + index, value);
        length++;
    }

    void remove() {
        if (length == 0) {
            std::cout << "Array is empty." << std::endl;
            return;
        }
        data.pop_back();
        length--;
    }

    void removeAt(int index) {
        if (index < 0 || index >= length) {
            std::cout << "Index out of bounds." << std::endl;
            return;
        }
        data.erase(data.begin() + index);
        length--;
    }

    int get(int index) {
        if (index < 0 || index >= length) {
            std::cout << "Index out of bounds." << std::endl;
            return -1;  // or throw exception
        }
        return data[index];
    }

    int size() const {
        return length;
    }

    void printArray() const {
        std::cout << "[";
        for (int i = 0; i < length; ++i) {
            std::cout << data[i];
            if (i < length - 1) std::cout << ", ";
        }
        std::cout << "]" << std::endl;
    }
};

int main() {
    MyArray arr;
    arr.insert(10);
    arr.insert(20);
    arr.insertAt(1, 15);
    arr.printArray();        // Output: [10, 15, 20]
    arr.remove();
    arr.printArray();        // Output: [10, 15]
    arr.removeAt(0);
    arr.printArray();        // Output: [15]
    std::cout << arr.get(0) << std::endl; // Output: 15
    std::cout << arr.size() << std::endl; // Output: 1
}
