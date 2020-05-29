#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector <int> arr;
    int a;
    while(true){
        cin>>a;
        arr.push_back(a);
        if(cin.get()=='\n'){break;}
    }

    vector <int> l1{' '};
    vector <int> l2;
    int n{arr.size()};
    int i{0};
    while(i<n){
        l2.push_back(arr[i]);
        l1.insert(l1.end(),l2.begin(),l2.end());

    }

}