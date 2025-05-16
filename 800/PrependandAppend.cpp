#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{   ll a; 
    cin>>a;
for(int i=0;i<a;i++)
{
    int b;
    cin>>b; 
    string s;
    cin>>s;
    int st=0;
    int en=b-1;
    int x=b;
    while(st<en && s[st]!=s[en] ) {
        x=x-2;
        st++;
        en--;
    }
    cout<<x<<endl;
    }
}
