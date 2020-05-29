#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

int main(){
    vector <int> n;
    cout<<"Enter the list:";
    int i;
    while(true){
        cin>>i;
        n.push_back(i);
        if(cin.get()=='\n'){break;}
    }
    unordered_map <int,int> m;
    for(int j=0;j<n.size();j++){
        m[n[j]]++;
    }

    for(int f=0;f<n.size();f++){
        if(m.find(n[f])!=m.end()){
        auto it=m.find(n[f]);
        cout<<it->first<<" "<<it->second<<endl;
        m.erase(it);
        }
    }


}