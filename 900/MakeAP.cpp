#include<bits/stdc++.h>
using namespace std;
#define ll long long 
#define yes cout<<"YES"<<endl
#define no cout<<"NO"<<endl
signed main(){
    int t; cin>>t;
    while(t--){
       	ll a,b,c;
       	cin>>a>>b>>c;
       	ll r=a+c;
       	ll l=2*b;
       	if (r==l)yes;
       	else if (r>l)
       	{
       		ll k=r/l;
       		if(k*l==r) yes;
       		else no;
       	}
       	else
       	{
       		ll k1=(2*b-c)/a;
       		ll k2=(2*b-a)/c;
       		if (k1*a==2*b-c||k2*c==2*b-a)yes;
       		else no;
       	}
	}
}
