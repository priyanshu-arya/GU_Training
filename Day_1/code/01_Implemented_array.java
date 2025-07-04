import java.util.ArrayList;

public class MyArray {
    private ArrayList<Integer> data;
    private int length;

    public MyArray() {
        data = new ArrayList<>();
        length = 0;
    }

    public void insert(int value) {
        data.add(value);
        length++;
    }

    public void insertAt(int index, int value) {
        if (index < 0 || index > length) {
            System.out.println("Index out of bounds.");
            return;
        }
        data.add(index, value);
        length++;
    }

    public void remove() {
        if (length == 0) {
            System.out.println("Array is empty.");
            return;
        }
        data.remove(length - 1);
        length--;
    }

    public void removeAt(int index) {
        if (index < 0 || index >= length) {
            System.out.println("Index out of bounds.");
            return;
        }
        data.remove(index);
        length--;
    }

    public Integer get(int index) {
        if (index < 0 || index >= length) {
            System.out.println("Index out of bounds.");
            return null;
        }
        return data.get(index);
    }

    public int size() {
        return length;
    }

    public void printArray() {
        System.out.println(data);
    }

    public static void main(String[] args) {
        MyArray arr = new MyArray();
        arr.insert(10);
        arr.insert(20);
        arr.insertAt(1, 15);
        arr.printArray();        // Output: [10, 15, 20]
        arr.remove();
        arr.printArray();        // Output: [10, 15]
        arr.removeAt(0);
        arr.printArray();        // Output: [15]
        System.out.println(arr.get(0)); // Output: 15
        System.out.println(arr.size()); // Output: 1
    }
}
