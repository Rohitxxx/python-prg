# try:
#     a=1/0
# except ArithmeticError as e:
#     print(e)

try:
    f1=open("11.txt")
    f2=open("2.txt")
    f3=open("3.txt")
    
    f1.close()
    f2.close()
    f3.close()
except Exception as e:
    print(e)
    print(" cannot open file")

