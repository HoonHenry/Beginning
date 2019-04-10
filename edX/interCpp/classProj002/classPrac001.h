#ifndef CLASSPRAC001_H_INCLUDED
#define CLASSPRAC001_H_INCLUDED
#include <string>

class Person(){
private:
    std::string firstName;
    std::string lastName;
    int age;

public:
    Person();

    Person(std::string firName, std::string lName);

    Person(std::string firName, std::string lName, int age);

    ~Person();

    void sayHello();
};


#endif // CLASSPRAC001_H_INCLUDED
