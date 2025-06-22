class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class LinkedList {
    Node head;

    public LinkedList() {
        this.head = null;
    }

    public void insertAtEnd(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node curr = head;
        while (curr.next != null)
            curr = curr.next;
        curr.next = newNode;
    }

    public void insertAtStart(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }

    public void insertAtIndex(int index, int data) {
        if (index < 0) {
            System.out.println("Index cannot be negative.");
            return;
        }

        if (index == 0) {
            insertAtStart(data);
            return;
        }

        Node curr = head;
        int count = 0;

        while (curr != null && count < index - 1) {
            curr = curr.next;
            count++;
        }

        if (curr == null) {
            System.out.println("Index out of bounds.");
            return;
        }

        Node newNode = new Node(data);
        newNode.next = curr.next;
        curr.next = newNode;
    }

    public void removeAtIndex(int index) {
        if (index < 0) {
            System.out.println("Index cannot be negative.");
            return;
        }

        if (head == null) {
            System.out.println("List is empty.");
            return;
        }

        if (index == 0) {
            head = head.next;
            return;
        }

        Node curr = head;
        int count = 0;

        while (curr.next != null && count < index - 1) {
            curr = curr.next;
            count++;
        }

        if (curr.next == null) {
            System.out.println("Index out of bounds.");
            return;
        }

        curr.next = curr.next.next;
    }

    public Integer get(int index) {
        if (index < 0) {
            System.out.println("Index cannot be negative.");
            return null;
        }

        Node curr = head;
        int count = 0;

        while (curr != null) {
            if (count == index)
                return curr.data;
            curr = curr.next;
            count++;
        }

        System.out.println("Index out of bounds.");
        return null;
    }

    public void printList() {
        Node curr = head;
        while (curr != null) {
            System.out.print(curr.data);
            if (curr.next != null) System.out.print(" -> ");
            curr = curr.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        LinkedList ll = new LinkedList();
        ll.insertAtEnd(10);
        ll.insertAtEnd(20);
        ll.insertAtStart(5);
        ll.insertAtIndex(1, 7);
        ll.printList(); // 5 -> 7 -> 10 -> 20

        ll.removeAtIndex(2);
        ll.printList(); // 5 -> 7 -> 20

        System.out.println(ll.get(1));  // 7
        System.out.println(ll.get(10)); // Index out of bounds.
    }
}
