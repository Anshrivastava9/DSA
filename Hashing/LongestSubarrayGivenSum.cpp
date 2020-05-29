#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

int Solve(vector<int> a,int sum){
   unordered_map<int,int> n;
   int presum{0},res{0};
   for(int i{0};i<a.size();i++){
       presum+=a[i];
       if(presum==sum){res=i+1;}
       if(n.find(presum)==n.end()){n.insert({presum,i});}
       if(n.find(presum-sum)!=n.end()){res=max(res,i-n[presum-sum]);}
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
    cout<<"Enter the Value of Sum:";
    cin>>sum;
    cout<<Solve(a,sum);
    return 0;
}
