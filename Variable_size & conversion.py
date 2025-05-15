import sys 
hexadecimal = "0xff" #255
string = "24"
conversion_1 = int(hexadecimal,0)
conversion_2 = int(string,0)
print("hex into int:",conversion_1)
print("string into int:",conversion_2)
print("size before conversion=", sys.getsizeof(hexadecimal))
print("size before conversion=", sys.getsizeof(string))
print("size after conversion=", sys.getsizeof(conversion_1))
print("size after conversion=", sys.getsizeof(conversion_2))
