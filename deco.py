def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print(f"ismail {func.__name__} ")
        print("{}{}".format("abc","cd"))
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
#
# k={}
# abc = "abccc1"
# for f in abc:
#     if f.isdigit():
#         print("digit is:",f)
#     if f in k:
#         k[f]=k[f]+1
#     else:
#         k[f]=1
#
# print(k)
#
#
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # import time
# #
# # # Optional: specify the path to your ChromeDriver
# # # service = Service('/path/to/chromedriver')
# # # driver = webdriver.Chrome(service=service)
# #
# # # If chromedriver is in PATH
# # driver = webdriver.Chrome()
# #
# # # Open Google
# # driver.get("https://www.google.com")
# #
# # time.sleep(3)
#
#
# ######custom exception
# # Define a custom exception
#
# class customException(Exception):
#     def __init__(self, msg):
#         self.msg = msg + "--->add some extra information"
#         super().__init__(self, self.msg)
#
# def try_ce():
#     try:
#         print("Print Normal line")
#         raise customException("Normal line failed")
#     except customException as e:
#         print("This is the cs error", e)
#
# try_ce()

# for ind,f in enumerate(range(5),start=1):
#     print(str(ind)+","+str(f))
#
# import pandas as pd
#
# data = [
#     {"name": "Alice", "age": 25, "city": "Hyderabad"},
#     {"name": "Bob", "age": 30, "city": "Delhi"}
# ]
#
# df = pd.DataFrame(data)
# print(df)
#
#
# nested_data = {
#     "students": [
#         {"name": "Alice", "info": {"age": 25, "city": "Hyderabad"}},
#         {"name": "Bob", "info": {"age": 30, "city": "Delhi"}}
#     ]
# }
#
# df = pd.json_normalize(nested_data['students'], sep='_')
# print(df)
#
#
# data = [
#     {'name': 'Alice', 'age': 25},
#     {'name': 'Bob', 'age': 30}
# ]
#
# df = pd.DataFrame(data)
# print(df)
#
# ############singleton
#
# class SingletonClass:
#     _instance = None
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(SingletonClass, cls).__new__(cls)
#         return cls._instance
#
# class normalClass:
#     msg =None
#     def __init__(self):
#         self.msg = "Ismail"
#
#
# o1 = normalClass()
# o2 = normalClass()
# print(o1 is o2)
#
# s1 = SingletonClass()
# s2 = SingletonClass()
# print(s1 is s2)
import time


class CE(Exception):
    msg = None
    def __init__(self, msg):
        self.msg = msg
        return super().__init__(msg)

def checkce():
    try:
        print("ce")
        raise CE("ismail rased")
    except CE as e:
        print(" Ce is",e)

checkce()




from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/test')
def home():
    return jsonify({"message": "Hello, Flask API is running 1!"})

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80, debug=False)
    app.run(host='0.0.0.0', port=80, threaded=True, use_reloader=False, debug=False)
