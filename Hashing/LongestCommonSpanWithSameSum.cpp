#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

int Solve(vector<int> c){
   unordered_map<int,int> n;
   int presum(0),res{0};
   for(int i{0};i<c.size();i++){
       presum+=c[i];
       if(presum==0){res=i+1;}
       if(n.find(presum)==n.end()){n.insert({presum,i});}
       if(n.find(presum)!=n.end()){res=max(res,i-n[presum]);}
   }
   return res;
}


int main(){
    cout<<"Enter the list1 of size n:";
    vector<int> a,b,c;
    int x,sum,y;
    while(true){
        cin>>x;
        a.push_back(x);
        if(cin.get()=='\n'){break;}
    }
    cout<<"Enter the List2 of size n:";
    while(true){
        cin>>y;
        b.push_back(y);
        if(cin.get()=='\n'){break;}
    }

    for(int i{0};i<a.size();i++){
        c.push_back(a[i]-b[i]);
    }

    cout<<Solve(c);
    return 0;
}
