#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

bool Solve(vector<int> a,int sum){
    unordered_set<int> n;
    int presum{0};
    for(auto i:a){
        presum+=i;
        if(n.find(presum-sum)!=n.end()){
            return true;
        }
        if(presum==sum){return true;}

        n.insert(presum);
    }
    return false;
}

int main(){
    vector<int> a;
    int sum,x;
    cout<<"Enter Given List:";
    while(true){
        cin>>x;
        a.push_back(x);
        if(cin.get()=='\n'){break;}
    }
    cout<<"ENter the value of Sum:";
    cin>>sum;
    cout<<boolalpha<<Solve(a,sum);

}