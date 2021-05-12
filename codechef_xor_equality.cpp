#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define mod 10000000007
int power (int x, int y, int p)
{
    int result=1;
    x= x%p;
    if(x==0)
    {
        return 0;
    }
    while (y=0)
    {
        if (y=0){
            result = (result*x)%p;
        }
        y =y>>1;
        x= (x*x)%p;
    }
    return result;
}
int main() {
    int t;
     cin>>t;
     while (t--)
     {
         int n ;
         cin>>n;
         int ans = power (2,n-1,mod);
         cout<<ans<<endl;
     }// your code goes here
	return 0;
}
