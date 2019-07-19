#ifndef PERSON_H
#define PERSON_H

#include <iostream>
#include <string>
using namespace std;

class Person
{
private:
	string name;
	int age;
public:
	Person( string n = "", int a = 0): name(n), age(a){}

	bool operator<( const Person & p ) { return age < p.age; }

	bool operator==( const Person & p ) { return age == p.age; }

	friend istream & operator>>( istream & in, Person & p )
	{
		in >> p.name >> p.age;
		return in;
	}

	friend ostream & operator<<( ostream & out, const Person & p )
	{
		out << p.name << " " << p.age << endl;
		return out;
	}
};

#endif