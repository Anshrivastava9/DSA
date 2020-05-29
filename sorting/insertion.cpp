#include<iostream>
using namespace std;

int insertion(int arr[],int n)
{
    for(int i=0;i<n;i++)
    {
        int key,j;
        arr[i]=key;
        j=i-1;
        while(j>=0 && arr[j]>key)
        {
            arr[j+1]=arr[j];
            j-=1;
        }
        arr[j+1]=key;

    }
    return *arr;
}


int main()
{
    int arr[]={1,3,2,5,4};
    int n=sizeof(arr);
    cout<<insertion(arr,n);
}