#include<bits/stdc++.h>
#include<string>
using namespace std;

int main(){
    string s;
    cout<<"Enter the String:";
    cin>>s;

    int a=count(s.begin(),s.end(),'g');
    cout<<a;

}
