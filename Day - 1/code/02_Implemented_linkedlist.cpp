#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int data): data(data), next(nullptr) {}
};

class LinkedList {
private:
    Node* head;

public:
    LinkedList(): head(nullptr) {}

    void insertAtEnd(int data) {
        Node* newNode = new Node(data);
        if (!head) {
            head = newNode;
            return;
        }
        Node* curr = head;
        while (curr->next) curr = curr->next;
        curr->next = newNode;
    }

    void insertAtStart(int data) {
        Node* newNode = new Node(data);
        newNode->next = head;
        head = newNode;
    }

    void insertAtIndex(int index, int data) {
        if (index < 0) {
            cout << "Index cannot be negative." << endl;
            return;
        }

        if (index == 0) {
            insertAtStart(data);
            return;
        }

        Node* curr = head;
        int count = 0;

        while (curr && count < index - 1) {
            curr = curr->next;
            count++;
        }

        if (!curr) {
            cout << "Index out of bounds." << endl;
            return;
        }

        Node* newNode = new Node(data);
        newNode->next = curr->next;
        curr->next = newNode;
    }

    void removeAtIndex(int index) {
        if (index < 0) {
            cout << "Index cannot be negative." << endl;
            return;
        }

        if (!head) {
            cout << "List is empty." << endl;
            return;
        }

        if (index == 0) {
            Node* temp = head;
            head = head->next;
            delete temp;
            return;
        }

        Node* curr = head;
        int count = 0;

        while (curr->next && count < index - 1) {
            curr = curr->next;
            count++;
        }

        if (!curr->next) {
            cout << "Index out of bounds." << endl;
            return;
        }

        Node* temp = curr->next;
        curr->next = curr->next->next;
        delete temp;
    }

    int get(int index) {
        if (index < 0) {
            cout << "Index cannot be negative." << endl;
            return -1;
        }

        Node* curr = head;
        int count = 0;

        while (curr) {
            if (count == index) return curr->data;
            curr = curr->next;
            count++;
        }

        cout << "Index out of bounds." << endl;
        return -1;
    }

    void printList() {
        Node* curr = head;
        while (curr) {
            cout << curr->data;
            if (curr->next) cout << " -> ";
            curr = curr->next;
        }
        cout << endl;
    }
};

int main() {
    LinkedList ll;
    ll.insertAtEnd(10);
    ll.insertAtEnd(20);
    ll.insertAtStart(5);
    ll.insertAtIndex(1, 7);
    ll.printList(); // 5 -> 7 -> 10 -> 20

    ll.removeAtIndex(2);
    ll.printList(); // 5 -> 7 -> 20

    cout << ll.get(1) << endl;  // 7
    cout << ll.get(10) << endl; // Index out of bounds.

    return 0;
}
