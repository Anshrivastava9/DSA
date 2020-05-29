#include<bits/stdc++.h>
#include<vector>
using namespace std;

int main(){
    int target{1};
    cout<<"Enter the list of NUmbers:";
    vector <int> l1;
    int a;
    while(true){
        cin>>a;
        l1.push_back(a);
        if(cin.get()=='\n')
            break;

    }
    sort(l1.begin(),l1.end());
    int n{l1.size()};
    int i{0};
    int j{l1.size()-1};
    int closest{l1[0]+l1[1]+l1[-1]}; 
    while(i<j-1){
        int k{i+1};
        while(k<j && i<j-1){
            if((l1[i]+l1[j]+l1[k])==target){break;}
            else if((l1[i]+l1[j]+l1[k])<target){
                closest=min(closest,l1[i]+l1[j]+l1[k]-target);
                k++;
                if(k==j-1){i++;}
            }
            else
            {
                closest=min(closest,target-l1[i]+l1[j]+l1[k]);
                j--;
                k=i+1;

            }
                
        }
        if(closest==target){break;}
}
cout<<"Closest number is:"<<closest;
return 0;
}
