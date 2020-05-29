#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

int Solve(vector<int> a,int k){
   unordered_map<int,int> n;
   for(int i{0};i<k;i++){
       n[a[i]]++;
   }
   cout<<n.size()<<" ";
   for(int i{k};i<a.size();i++){
        if(n[a[i-k]]==1){n.erase(a[i-k]);}
        else{n[a[i-k]]--;}
        if(n.find(a[i])!=n.end()){n[a[i]]++;}
        else{n.insert({a[i],1});}
        cout<<n.size()<<" ";

   }
   
} 


int main(){
    cout<<"Enter the list of numbers:";
    vector<int> a;
    int x,k;
    while(true){
        cin>>x;
        a.push_back(x);
        if(cin.get()=='\n'){break;}
    }
    cout<<"Enter the size of Window:";
    cin>>k;
    Solve(a,k);
    return 0;
}
