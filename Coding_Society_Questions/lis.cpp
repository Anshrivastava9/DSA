#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector <int> arr;
    int a;
    cout<<"Enter the array:";
    int b;
    cin>>b;
    arr.push_back(b);
    char q{'\n'};
    while(true){
        if(cin.get()==q){break;}
        cin>>a;
        arr.push_back(a);

    }
    vector <int> arr2;
    arr2.push_back(1);
    for(int j=1;j<arr.size();j++){
        arr2.push_back(1);
        for(int k{0};k<j;k++){
            if(arr[k]<arr[j]){
                arr2[j]=max(1+arr2[k],arr2[j]);
            }
        }
    }

    /*for(int x{0};x<arr.size();x++){
        cout<<arr2[x]<<" ";
    }
*/

    int res=arr2[0];
    for(int i{1};i<arr.size();i++){
        res=max(res,arr2[i]);
    }


    cout<<"THe longest increasing subsequence:"<<res;


    return 0;
}