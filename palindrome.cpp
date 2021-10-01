// A palindrome is a word or phrase that reads the same backward as forward.
// Ex : M-A-D-A-M , POP, NAMAN ,ABA, ABCBA, ABCBAB, ABCBABABCBAB
// Logic : 
//  Take input from user
//   check if the number is palindrome or not
//  if yes the print "palindrome"
//  if not print"not palindrome"
 
#include<bits/stdc++.h>
using namespace std;
void palindrome(string s) {
    int n = s.length();
    // string 1st word s[0] compare with last word s[n-1] 
    int i=0,j=n-1,flag=0;
    while(i<j) {
        if(s[i]==s[j]) {
            i++;
            j--;
            flag=1;
        }
        else {
            flag=0;
        }
    }
    if(flag==1) {
        cout<<"Yes palindrome"<<endl;
    }
    else {
        cout<<"No palindrome"<<endl;
    }

}
int main() {
    string s;
    cin>>s;
    palindrome(s);
    return 0;
}
