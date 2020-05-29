#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector <string> arr;
    string a;
    cout<<"Enter Your List of Strings:";
    while(true){
        cin>>a;
        arr.push_back(a);
        if(cin.get()=='\n'){break;}
    }
    int count;
    for(int i{0};i<arr.size();i++){
        count=1;
        for(int j{0};j<arr.size()-1;j++){
            if(arr[j][i]==arr[j+1][i]){count++;}
            else{break;}
        }
        if(count==arr.size()){cout<<arr[0][i];}
    }






    return 0;

}