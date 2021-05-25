print("started")
a=10
b=20
c=a+b
def fun(x,y):
	print(f"x={x},y={y}")
	try:
		z=x/y
		print("result=",z)
	except Exception as err:
		print(err)
	
for i in [1,4,2,0,4,6,7,8]:
	if i!=0:
		res=10/i 
fun(10,20)
import pdb;pdb.set_trace()
fun(10,0)
print("ended")