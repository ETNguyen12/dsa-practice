#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

class Node {
    public:
        int val;
        Node* next; 

        Node (int value) {
            this->val = value;
            this->next = nullptr;
        }
};

class LinkedList {
    private:
        Node* head;
        Node* tail;
        int length;
    
    public:
        LinkedList (int value) {
            Node* newNode = new Node(value);
            this->head = newNode;
            this->tail = newNode;
            this->length = 1;
        }

        ~LinkedList() {
            Node* curr = head;
            while (head) {
                head = head->next;
                delete curr;
                curr = head;
            }
        }

        void printList() {
            Node* curr = head;
            cout << "[" << curr->val << "]";
            curr = curr->next;
            
            while (curr) {
                cout << "-> [" << curr->val << "]";
                curr = curr->next;
            }
            cout << endl;
        }

        void append(int value) {
            Node* newNode = new Node(value);
            if (length == 0) {
                head = newNode;
                tail = newNode;
            } else {
                tail->next = newNode;
                tail = newNode;
            }
            length++;
        }

        void prepend(int value) {
            Node* newNode = new Node(value);
            if (length == 0) {
                head = newNode;
                tail = newNode;
            } else {
                newNode->next = head;
                head = newNode;
            }
            length++;
        }

        void deleteFirst() {
            if (length == 0) {
                return;
            } else if (length == 1) {
                delete head;
                head = nullptr;
                tail = nullptr;
            } else {
                Node* temp = head;
                head = head->next;
                delete temp;
            }
            length--;
        }

        void deleteLast() {
            if (length == 0) {
                return;
            } else if (length == 1) {
                delete head;
                head = nullptr;
                tail = nullptr;
            } else {
                Node* temp = head;
                while (temp->next != tail) {
                    temp = temp->next;
                }
                delete tail;
                tail = temp;
                tail->next = nullptr;
            }
            length--;
        }

        Node* get(int index) {
            if (index < 0 or index >= length) {
                return nullptr;
            }

            Node* curr = head;
            int i = 0;
            while (i != index) {
                curr = curr->next;
                i++;
            }
            return curr;
        }

        bool set(int index, int value) {
            Node* node = get(index);
            if (!node) {
                return false;
            }
            node->val = value;
            return true;
        }

        bool insert(int index, int value) {
            if (index < 0 or index > length) {
                return false;
            }
            
            if (index == 0) {
                prepend(value);
            } else if (index == length) {
                append(value);
            } else {
                Node* newNode = new Node(value);
                Node* temp = get(index-1);
                newNode->next = temp->next;
                temp->next = newNode;
            }
            length++;
            return true;
        }

        void deleteNode(int index) {
            if (index < 0 or index >= length) {
                return;
            }

            if (index == 0) {
                deleteFirst();
            } else if (index == length-1) {
                deleteLast();
            } else {
                Node* prev = get(index-1);
                Node* node = prev->next;
                prev->next = node->next;
                delete node;
                length--;
            }
        }

        void reverse() {
            Node* temp = head;
            head = tail;
            tail = temp;

            Node* prev = nullptr;
            while (temp) {
                Node* nxt = temp->next;
                temp->next = prev;
                prev = temp;
                temp = nxt;
            }
        }

        Node* findMiddleNode() {
            Node* slow = head;
            Node* fast = head;
            while (fast and fast->next) {
                slow = slow->next;
                fast = fast->next->next;
            }   
            return slow;
        }

        bool hasLoop() {
            Node* slow = head;
            Node* fast = head;
            while (fast and fast->next) {
                slow = slow->next;
                fast = fast->next->next;
                if (slow == fast) {
                    return true;
                }
            }
            return false;
        }

        Node* findKthFromEnd(int k) {
            Node* slow = head;
            Node* fast = head;
            
            for (int i = 0; i < k; i++) {
                if (!fast) return nullptr;
                fast = fast->next;
            }

            while (fast) {
                slow = slow->next;
                fast = fast->next;
            }
            return slow;
        }

        void removeDuplicates() {
            unordered_set<int> seen;
            Node* prev = nullptr;
            Node* curr = head;
            while (curr) {
                if (seen.count(curr->val)) {
                    prev->next = curr->next;
                    delete curr;
                    curr = prev->next;
                    length--;
                } else {
                    seen.insert(curr->val);
                    prev = curr;
                    curr = curr->next;
                }
            }
        }

        int binaryToDecimal() {
            int total = 0;
            Node* curr = head;
            while (curr) {
                total = total * 2 + curr->val;
                curr = curr->next;
            }
            return total;
        }

        Node* partition(int x) {
            Node lessHead(-1);
            Node greaterHead(-1);
            Node* less = &lessHead;
            Node* greater = &greaterHead;

            Node* temp = head;
            while (temp) {
                if (temp->val < x) { 
                    less->next = temp;
                    less = less->next;
                } else {
                    greater->next = temp;
                    greater = greater->next;
                }
                temp = temp->next;
            }
            greater->next = nullptr;
            less->next = greaterHead.next;
            return lessHead.next;
        }
};

int main() {
    LinkedList* myLinkedList = new LinkedList(2);
    myLinkedList->append(4);
    myLinkedList->prepend(1);
    myLinkedList->printList();
    myLinkedList->getLength();
    return 0;
}