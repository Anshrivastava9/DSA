//Recursive solution
#include<bits/stdc++.h>
#include<string>
using namespace std;
/*
int solve(string a,string b,int n,int m){
    if(n==0){return m;}
    if(m==0){return n;}

    if(a[n-1]==b[m-1]){
        return solve(a,b,n-1,m-1);
    }
    else{
        return 1+min({solve(a,b,n-1,m-1),solve(a,b,n,m-1),solve(a,b,n-1,m)});
    }

}
*/
//Dynamic Programming Solution
int solve(string a,string b,int n,int m){
    int matrix[n+1][m+1];
    int i{0};
    while(i<=n){
        matrix[i][0]=i;
        i++;
    }
    int j=0;
    while(j<=m){
        matrix[0][j]=j;
        j++;
    }

    for(int j=1;j<=n;j++){
        for(int k=1;k<=m;k++){
            if(a[j-1]==b[k-1]){matrix[j][k]=matrix[j-1][k-1];}
            else{
                matrix[j][k]=1+min({matrix[j-1][k-1],matrix[j-1][k],matrix[j][k-1]});
            }

            
        }
    }

    return matrix[n][m];

}




int main(){
    string a;
    cout<<"Enter the String to be converted:";
    cin>>a;
    string b;
    cout<<"Enter the target String:";
    cin>>b;
    int n{a.size()};
    int m{b.size()};
    cout<<solve(a,b,n,m);
    return 0;

}

