n = 7000000000;
x = 4000000;
y = n-x;
nsobre2 = n/2;

T0 = 1/2*100;
T1 = 1/2*100;
for i in range(1,x):
	T1 = (nsobre2 - i)*T0/(n-i)
	T0 = T1;
	#print(i);
print("N = " + str(n) + "   X = " + str(x) + "   Prob = " + str(T1) + " %");
