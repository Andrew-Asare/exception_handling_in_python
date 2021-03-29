# # Dealing with files and error/exception handling
#
# # There is a built in method in python called open("")
# # file = open("orders.text") # looks for the file called orders.text
# # keyword try
# try:
#     file = open("orders.text")
#     print("file was found")
# except FileNotFoundError as errmsg:
#     print(f"the above block of code was not executed {errmsg}")
#     # raise
# # finally executes regardless of above conditions
# finally:
#     print("This is found, your task is to read the data and display it as a list")
#
# second iteration:
# Your task is to read the data and display it as a list
# file = open("orders.text", "r")
# content = file.read()
# print(content)
# third iteration:
filename = "orders.text"
# def read_and_print(filename):
#     try:
#         items = []
#         file = open(filename, 'r')
#         print('File found')
#         for line in file:
#             items.append(line.rstrip('\n'))
#         print(items)
#     except IOError:
#         print('The above block was not executed')
#     finally:
#         print("Thank you")
#

#
# def open_using_with_and_print(file):
#     try:
#         with open(file, "r") as file:
#             for line in file.readlines():
#                 print(line.rstrip('\n'))
#     except FileNotFoundError:
#         print("file cannot be found or directory is incorrect, please check the details provided")
#         raise
#     finally:
#         print("\nPlease chose the items from the list  and enjoy your HAPPY MEAL")
# open_using_with_and_print("orders.text")
#
# open_and_read_file(filename)


#
# def write_to_file(file, order_item):
#     try:
#         with open(file, "w") as file:
#             file.write(order_item + '\n')
#     except FileNotFoundError:
#         print("file cannot be found or directory is incorrect, please check the details provided")
#         raise