#include<bits/stdc++.h>
#include<string>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        string s;
        cin>>s;
        int arr[256];
        for(int i{0};i<256;i++){
            arr[i]=-1;
        }
        int res=INT_MAX;
        for(int i{0};i<s.size();i++){
            if(arr[s[i]]==-1){arr[s[i]]=i;}
            else
            {
                res=min(res,arr[s[i]]);
            }
            
        }
        if(res==INT_MAX){cout<<-1;}
        else{cout<<res;}
        cout<<endl;

        
    }
    return 0;
}