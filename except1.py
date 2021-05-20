from time import sleep
print("started")
a=input("Enter a value:")
b=input("Enter b value:")
print(f"before conversion: a={a},b={b}")
try:
    a,b=float(a),float(b)
    print(f"after conversion: a={a},b={b}")
    sleep(10)
    res=a/b #raise
    print(f"result={res}")
except ValueError as err:
    print("Expecting only digits.")
except ZeroDivisionError as err:
    print("expecting b not equal 0.")
except Exception as err:
    print("something went wrong")
    print("Error:",err)
except:
    print("something went wrong")
print("ended")