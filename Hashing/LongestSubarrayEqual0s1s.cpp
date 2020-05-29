#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

int Solve(vector<int> a){
   unordered_map<int,int> n;
   int presum{0},res{0};
   for(int i{0};i<a.size();i++){
       presum+=a[i];
       if(presum==0){res=i+1;}
       if(n.find(presum)==n.end()){n.insert({presum,i});}
       if(n.find(presum)!=n.end()){res=max(res,i-n[presum]);}
       
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
    for(int x{0};x<a.size();x++){if(a[x]==0){a[x]=-1;}}
    cout<<Solve(a);
    return 0;
}
