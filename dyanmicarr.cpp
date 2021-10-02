#include<bits/stdc++.h>
using namespace std;
int main()
{
    // making of dynamic array 
    int s;
    cout<<"give size : ";
    cin>>s;
    int a[s];
    cout<<"give me values : ";
    for(int i=0;i<s;i++)
    {
        cin>>a[i];
    }
    cout<<"your given values are : ";
    for(int j=0;j<s;j++)
    {
        cout<<a[j]<<" ";
    }
    cout<<endl;
    cout<<"your odd values are : ";
    for(int k=0;k<s;k++)
    {
      
      if(a[k]%2==0)
      {
      }
      else
      {
        cout<<a[k]<<" ";
      }
    }
    return 0;
}
