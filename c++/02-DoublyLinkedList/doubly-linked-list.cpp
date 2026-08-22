#include <iostream>
#include <string>

using namespace std;

class Node {
    public:
        int val;
        Node* next;
        Node* prev;

        Node(int value) {
            val = value;
            next = nullptr;
            prev = nullptr;
        }
};

class DoublyLinkedList {
    private:
        Node* head;
        Node* tail;
        int length;

    public:
        DoublyLinkedList(int value) {
            Node* newNode = new Node(value);
            head = newNode;
            tail = newNode;
            length = 1;
        }

        ~DoublyLinkedList() {
            Node* curr = head;
            while (head) {
                head = head->next;
                delete curr;
                curr = head;
            }
        }

        void prepend(int value) {
            Node* newNode = new Node(value);
            if (length == 0) {
                head = newNode;
                tail = newNode;
            } else {
                newNode->next = head;
                head->prev = newNode;
                head = newNode;
            }
            length++;
        }

        void append(int value) {
            Node* newNode = new Node(value);
            if (length == 0) {
                head = newNode;
                tail = newNode;
            } else {
                tail->next = newNode;
                newNode->prev = tail;
                tail = newNode;
            }
            length++;
        }

        void deleteFirst() {
            if (length == 0) return;
            Node* temp = head;
            if (length == 1) {
                head = nullptr;
                tail = nullptr;
            } else {
                head = head->next;
                head->prev = nullptr;
            }
            delete temp;
            length--;
        }

        void deleteLast() {
            if (length == 0) return;
            Node* temp = tail;
            if (length == 1) {
                head = nullptr;
                tail = nullptr;
            } else {
                Node* prev = tail->prev;
                prev->next = nullptr;
                tail = prev;
            }
            delete temp;
            length--;
        }

        Node* get(int index) {
            if (index < 0 or index >= length) return nullptr;
            Node* temp = head;
            for (int i = 0; i < index; i++) {
                temp = temp->next;
            }
            return temp;
        }

        bool set(int index, int value) {
            Node* node = get(index);
            if (!node) return false;
            node->val = value;
            return true;
        }

        bool insert(int index, int value) {
            if (index < 0 or index > length) return false;
            if (index == 0) {
                prepend(value);
                return true;
            } 
            if (index == length) {
                append(value);
                return true;
            } 
            
            Node* newNode = new Node(value);
            Node* prev = get(index-1);
            Node* curr = prev->next;
            prev->next = newNode;
            newNode->prev = prev;
            newNode->next = curr;
            curr->prev = newNode;
            length++;
            return true;
        }

        void deleteNode(int index) {
            if (index < 0 or index >= length or length == 0) return;
            if (index == 0) return deleteFirst();
            if (index == length - 1) return deleteLast();

            Node* prev = get(index-1);
            Node* curr = prev->next;
            Node* next = curr->next;
            prev->next = next;
            next->prev = prev;
            delete curr;
            length--;
        }   
};

int main() {
    return 0;
}