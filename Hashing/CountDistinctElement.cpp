//Count number of distinct in elements in list
#include<iostream>
#include<unordered_set>
#include<vector>
using namespace std;

int main(){
    vector <int> n;
    int i;
    cout<<"Enter the Elements:";
    while(true)
    {
        cin>>i;
        n.push_back(i);
        if(cin.get()=='\n'){break;}
    }

    unordered_set <int> s;
    for(int i=0;i<n.size();i++){
        s.insert(n[i]);
    }
    cout<<s.size()<<endl;    

}