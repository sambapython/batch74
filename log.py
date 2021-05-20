import logging # debug,info,warn,error
#logging.info("program started") # this will take the default basicConfig. What ever the basic config
# we mentioned in your program will not effect.
logging.basicConfig(level=logging.DEBUG,
    filename="log.txt",
    format="%(asctime)s==>%(name)s==>%(levelname)s==>%(message)s") # object is a singletonobject
logging.info("program started")
a=input("Enter a value:")
logging.info("a value entered")
b=input("Enter b value:")
logging.info("b value entered")
logging.debug(f"before conversion: a={a},b={b}")
try:
    a,b=float(a),float(b) # raise  Ex
    logging.info("a,b values converted successfully")
    logging.debug(f"after conversion: a={a},b={b}")
    res=a/b 
    logging.info("result calculated")
    print(f"result={res}")
    logging.debug(f"ReSult: {res}")
except ValueError as err:
    print("Expecting only digits.")
    logging.error(f"{err}")
except ZeroDivisionError as err:
    print("expecting b not equal 0.")
    logging.error(f"{err}")
except Exception as err:
    print("something went wrong")
    print("Error:",err)
    logging.error(f"{err}")
except:
    print("something went wrong")
    logging.error("Some system exception raised.")
logging.info("ended")