#include<iostream>
#include<vector>
#include<unordered_set>


using namespace std;



bool Solve(int sum,vector<int> n){
    unordered_set<int> s;
    for(auto i:n){
        if(s.find(sum-i)!=s.end())
        { return true;
        }
        s.insert(i);
    }
    return false;

}

int main(){
    vector<int> n;
    int sum,a;
    cout<<"Enter the List:";
    while(true){
        cin>>a;
        n.push_back(a);
        if(cin.get()=='\n'){break;}
    }
    cout<<"Enter the Value of Sum:";
    cin>>sum;
    cout<<boolalpha;
    cout<<Solve(sum,n);


    





}