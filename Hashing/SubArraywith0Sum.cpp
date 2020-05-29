#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

bool Solve(vector<int> a){
    unordered_set<int> n;
    int addpre{0};
    for(auto i:a){
        addpre+=i;
        if(n.find(i)!=n.end()){return true;}
        if(addpre==0){return true;}

        n.insert(addpre);    
    }
    return false; 

}

int main(){
    vector<int> a;
    int x;
    cout<<"Enter the array:";
    while (true)
    {
        cin>>x;
        a.push_back(x);
        if(cin.get()=='\n'){break;}
    }
    cout<<boolalpha<<Solve(a);
    
    

}