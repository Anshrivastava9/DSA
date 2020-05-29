t=int(input())
while(t!=0):
	k,d0,d1=(int(i) for i in input().split())
	res=d0+d1
	s=res
	for i in range(2,k):
	    res1=(res)%10
	    s+=res1
	    res+=res1
	if s%3==0:
        print("YES")
	else:
        print("NO")
    t-=1

