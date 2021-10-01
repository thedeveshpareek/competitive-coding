 // A aramstrong number is a number that is sum of its own digits each raised to the power of the number of digits.
//  example 153 = 1^3 + 5^3 + 3^3 = 3+125+27 = 153
#include<iostream>
#include<math.h>
using namespace std;
void armstrong(int x) 
{
    // find number of digits
    int n=0;
    int temp=x;
    while(temp!=0) {
        temp=temp/10;
        n++;
    }
    cout<<"Number of digits in "<<x<<" is "<<n<<endl;
    int sum=0;
    temp=x;
    // find sum of power of number of digits
    while(temp!=0) {
        int r=temp%10;
        cout<<"r is "<<r<<endl;
        sum=sum+pow(r,n);
        cout<<"sum is "<<sum<<endl;
        temp=temp/10;
    }
    cout<<"Sum of power of "<<n<<" is "<<sum<<endl;
    if(sum==x) {
        cout<<x<<" is a armstrong no"<<endl;
    }
    else {
        cout<<x<<" isn't a armstrong no."<<endl;
    }                                                              
}
int main() {
    int x;
    cout<<"Enter a number: ";
    cin>>x;
    armstrong(x);
    return 0;
}
