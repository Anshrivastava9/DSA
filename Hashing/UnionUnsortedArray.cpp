#include<iostream>
#include<vector>
#include<unordered_set>

using namespace std;

int main(){
    vector<int> a;
    vector<int> b;
    int x,y;
    cout<<"Enter 1st Array:";
    while(true)
    {
        cin>>x;
        a.push_back(x);
        if(cin.get()=='\n'){break;}
    }
    cout<<"Enter 2st Array:";
    while(true)
    {
        cin>>y;
        a.push_back(y);
        if(cin.get()=='\n'){break;}
    }
    unordered_set <int> n;
    for(auto i:a){
        n.insert(i);
    }
    for(auto j:b){
        n.insert(j);
    }

    for(auto k:n){
        cout<<k<<" ";
    }

    return 0;
}