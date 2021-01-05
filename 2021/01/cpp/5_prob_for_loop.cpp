// HackerRank for loop problem C++
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int a,b;
    
    string result[9] = {"one", "two", "three", "four", "five", "six", "seven",  "eight", "nine"};
    
    cin >>a >>b;
    
    for (int i = a; i <= b; i++)
    {
        if (i >= 1 && i <= 9)
        {
            cout << result[i-1] << endl;
        }
        else
            cout << ((i % 2 == 0) ? "even" : "odd") << endl;
    }
    return 0;
}