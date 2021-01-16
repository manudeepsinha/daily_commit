//small demonstration of a linked list

#include<iostream>

using namespace std;

struct node
{
	int data;
	node *link;
};

typedef node* nodePtr;

void insert(nodePtr& head, int data);

int main()
{
	nodePtr head;
	head = new node;
	head -> data = 20;
	head -> link = NULL;

	insert(head, 30)

	nodePtr tmp;
	tmp = head;

	while(tmp != NULL)
	{
		cout << tmp-> data << endl;
		tmp = tmp -> link;
	}

	return 0;
}

void insert(nodePtr& head, int data)
{
	nodePtr tmpPtr;
	tmpPtr = new node;
	tmpPtr -> data = data;
	tmpPtr -> link = head
	head = tmpPtr;
}