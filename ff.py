a,b = map(int,input().split())
if b-a==1 or a==b:
	if b-a==1:
		print("{} {}".format(a,b))
	else:
		a*=10
		b*=10
		b+=1
		print("{} {}".format(a,b))
    
elif a==9 and b==1:
	b*=10
	print("{} {}".format(a,b))
	
else:
    print(-1)
    
