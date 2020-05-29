//Anagram meaning permutations of each other.
#include<bits/stdc++.h>
#include<string>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        string s1,s2;
        cin>>s1;
        cin>>s2;
        int arr[256]{0};
        if(s1.size()!=s2.size()){cout<<"NO"<<endl;}
        else{
            for(int i{0};i<s1.size();i++){
                arr[s1[i]]+=-1;
        }
        for(int i{0};i<s1.size();i++){
                arr[s2[i]]+=1;
        }
        int count=0;
        for(int i{0};i<256;i++){
                if(arr[i]!=0){count=1;cout<<"NO"<<endl;break;}
        }
        if(count==0){cout<<"YES"<<endl;}

        }
    }
    return 0;
}