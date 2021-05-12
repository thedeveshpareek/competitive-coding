#include <bits/stdc++.h>
using namespace std;
#define ll long long
//#define mod 10000000007
int  power (long long x, unsigned int y, int p)
{
    int  result=1;
    x= x%p;
    if(x==0)
    {
        return 0;
    }
    while (y>0)
    {
        if (y&1)
        {
            result = (result*x)%p;
        }
        y = y>>1;
        x = (x*x)%p;
    }
    return result;
}
int main() {
    int t;
     cin>>t;
     for(int j=0;j<t;j++)
     {
          int n ;
         cin>>n;
         int i, ans =1;
          ans = power (2,n-1,10000000007);
         cout<<ans<<endl;
     }
	return 0;
}
