#include<iostream>
#include<string>
using namespace std;
int main(){
    string str1;
    cout<<"Enter the String:";
    cin>>str1;

    for(int i{0};i<str1.length();i++){
        int j{0};
        while(j<str1.length()-i-1){
            cout<<" ";
            j++;
        }
        int k{0};
        while(true){
        if(k<=i)
        {
            cout<<str1[k];
            k++;/* code */
        }
        else
        {
            break;
        }
        
        }
                k-=2;
                while(k>=0){
                    cout<<str1[k];
                    k-=1;
                }
                cout<<endl;
            }
        
    return 0;    
        }