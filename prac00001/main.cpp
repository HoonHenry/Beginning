#include <iostream>
#include <string>

using namespace std;

class Book{
    public:
        string title;
        string author;
        int pages;
        int numBooks;
        Book(){
            title = "no title";
            author = "no author";
            pages = 0;
        }
//        Book(string aTitle, string anAuthor, int aPage){
//            cout << "Possible authors: " << authorNames << endl;
//        }
        void Dispaly(string a, string b, int c){
            cout << "Title: " << endl;
            cout << "Author: " << endl;
            cout << "Total Pages: " << endl;
        }
        void getInfo(int c){
            for (int i = 0; i < c; i++){
                cout << "Title is?: "; cin >> title;
                cout << "Author is?: "; cin >> author;
                cout << "Pages are?: "; cin >> pages;
            }
        }
        int numOfBooks(){
            cout << "How many books do you want to store? (Enter a positive integer): ";
            cin >> numBooks;
            return numBooks;
        }
    private:
        //string authorNames = {"Charles", "Hoon", "Henry"};


};
int main()
{
//    Book book1("Hoon", "Who", 400);
//    cout << book1.author << endl;
    getInfo(numOfBooks());
    return 0;
}






