#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

int Solve(vector<int> a){
    int res{0};
    unordered_set<int> n;
    for(auto x:a){
        n.insert(x);
    }

    for(int i{0};i<a.size();i++){
        if(n.find(a[i]-1)==n.end()){
            int curr=1;
            while(n.find(a[i]+curr)!=n.end())
            {
                curr++;
            }
            res=max(res,curr);
            
        }
    }
    return res; 
}


int main(){
    cout<<"Enter the list of numbers:";
    vector<int> a;
    int x,sum;
    while(true){
        cin>>x;
        a.push_back(x);
        if(cin.get()=='\n'){break;}
    }
    cout<<Solve(a);
    return 0;
}
