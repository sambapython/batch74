# import purchase
# import sales
# purchase.create_supplier()
# print(purchase.name)
# print(purchase.age)
# sales.create_customer()

#import purchase
#purchase.create_supplier()
#from purchase import create_supplier
#create_supplier()

#import purchase
"""
it look for the __pycache__.purchase.pyc
1. if this file not available then it will compile purchase.py file and create purchase.pyc file and run it.
2. if the purchase.pyc file availabe, then it will take a decission to create pyc file again or not 
base on the below scenarios.

	a. It will check the modified date and time of purchase.py and purchase.pyc files
	   if .py date> .pyc date then it will recompile the file.

	   some scenarios it will recompile the code eventhough .py date < .pyc date
	    I. when you are running the file using differet copiler. i.e first you created pyc using cpython ccompiler, now you are running your file using jpython compiler
	    Some scenarios it will recopile the code eventhough compiler is same and .py date < .pyc date.
	       i.e created pyc file using cpython -3.8 version. now running the file using cpython 3.9 version.

instaled: 3.8 cpython compiler: running  main.py: it will compile all the imported files according the cpython copiler and 3.8 version
instaled: 3.9 cpython compiler: running  main.py: it will compile all the imported files according the cpython copiler and 3.9 version
instaled: 3.8 jpython compiler: running  main.py: it will compile all the imported files according the jpython copiler and 3.8 version

"""
"""

I modified a pur.py python file in local and imported in to main, I am not run the main.py file in local. I uploaded .py file and .pyc
file in to server. Now if i run main.py in server will i get the changes?

what is the modified date and time of files if you upload in to server. will it gets the original modifed time 
or uploaded date and time?
uploaded date and time. 
"""
# import sales
# purchase.create_supplier()
# sales.create_customer()
# print(purchase.name)
# print(purchase.age)

#from ERP import stock, pur, product
#product.create_product()
#from ERP.product import create_product
#create_product()
#from ERP import stock as stock_module , pur as pur_module, product as product_module
#product_module.create_product()
#import delivery
#import os
'''
import sys
sys.path.append("C:\\Users\\Lenovo\\Desktop\\")
print(sys.path)
import delivery
'''
import sys
#print(sys.argv)
for arg in sys.argv[1:]:
	print(arg, type(arg))
