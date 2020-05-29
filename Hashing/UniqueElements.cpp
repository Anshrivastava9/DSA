#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

int countNonRepeated(vector<int> a, int n)
{
   unordered_map<int,int> m;
   for(int i{0};i<n;i++){
       m[a[i]]++;
   }
   int res{0};
   for(int j{0};j<n;j++){
       if(m[a[j]]==1){res++;}
   }
   return res;
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
    int n{a.size()};
    cout<<countNonRepeated(a,n);
    return 0;
}



