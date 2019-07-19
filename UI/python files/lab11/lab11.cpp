// Lab 11
// heap sort a deque of Person pointers in descending order

#include <iostream>
#include <deque>
#include "Person.h"
using namespace std;


// Do1: write the heap sort in DESCENDING order. 
// Add additional functions if necessnodes
/*template <class T>
void HeapSortDescending( deque<T*> & nodes, int size )
{
	for (int i = 0; i < size; i++)
	{
		int maxChild = -1;
		if (*nodes[i * 2 + 1] < *nodes[i * 2 + 2])
			maxChild = i * 2 + 2;
		else
			maxChild = i * 2 + 1;

		if (*nodes[i] < *nodes[maxChild])
			swap(nodes, i, maxChild);
	}
}*/


template <class T>
void swap(T *& x, T *& y)
{
	T *temp = x;
	x = y;
	y = temp;
}

template <class T>
void ReheapDown(deque<T*> & nodes, int root, int num)
{
	if (2 * root + 1 <= (num - 1)) 
	{
		int maxKid = 2 * root + 1;
		if ((2 * root + 2) <= (num - 1) &&
			nodes[2 * root + 2] > nodes[maxKid])
			maxKid = 2 * root + 2;
		if (nodes[root] < nodes[maxKid])
		{
			swap(nodes[root], nodes[maxKid]);
			ReheapDown(nodes, maxKid, num);
		}
	}
}


template <class T>
void HeapSortDescending(deque<T*> & nodes, int num)
{
	int index;
	for (index = num / 2 - 1; index >= 0; index--)
		ReheapDown(nodes, index, num);
	for (index = num - 1; index >= 1; index--)
	{
		swap(nodes[0], nodes[index]);
		ReheapDown(nodes, 0, index);
	}
}






void main()
{
	deque<Person *> people;
	Person p;

	// Do2: write end of file loop to read in multiple persons and store in people.
	
	cin >> p;
	while (cin)
	{
		Person *pp = new Person();
		*pp = p;
		people.push_back(pp);
		cin >> p;
	}
	
	
	

	// print out the entire people
	for( int i = 0; i < people.size(); i++ )
		cout << *people[i];
	
	// Do3: Use HeapSortDescending to sort people in age descending order
	
	HeapSortDescending(people, people.size());
	
	
	// print out the sorted people
	cout << "The sorted array is: " << endl;
	for( int i = 0; i < people.size(); i++ )
		cout << *people[i];

	for( int i = 0; i < people.size(); i++ )
		delete people[i];
}