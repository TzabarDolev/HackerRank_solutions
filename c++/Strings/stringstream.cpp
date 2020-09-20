#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    vector<int> out;
    stringstream ss(str);
    char ch;
    int temp;
    while(ss){
        if(ss.peek() != ','){
            if(ss >> temp){
                out.push_back(temp);
            }
        }
        else{
            ss >> ch;
        }

        ss >> ch;
    }
    return out;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }

    return 0;
}
