#Dealing with files and Exception in Python
## We have `try`, `except`, `raise` and `finally` as our code blocks to handle the error of an exception

### To understand the concept easily - 
- Each block of code works as an if, elif, else block

```
# There is a built in method in python called open("")
# file = open("orders.text") # looks for the file called orders.text
# keyword try
try:
    file = open("orders.text")
    print("file was found")
except FileNotFoundError as errmsg:
    print(f"the above block of code was not executed {errmsg}")
    # raise
# finally executes regardless of above conditions
finally:
    print("This is found, your task is to read the data and display it as a list")

```

- Please ensure to create an orders.text if does not exist

| Mode |Description|
| :----: |:---- |
|'r' |This is the default mode. It Opens file for reading. |
|'w' |This Mode Opens file for writing. If file does not exist, it creates a new file. If file exists it truncates the file.|
|'x' |Creates a new file. If file already exists, the operation fails.|
|'a' |Open file in append mode. If file does not exist, it creates a new file.|
|'t' |This is the default mode. It opens in text mode.|
|'b' |This opens in binary mode.
|'+' |This will open a file for reading and writing (updating)|




It is worth noting that the `+` operator can be used with


### CRUD
`create` `read` `update` `delete`