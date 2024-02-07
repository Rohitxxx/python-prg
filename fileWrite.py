f=open("data.txt",'w')
data="hello rohit"
f.write(data)
f.close

f=open("data2.txt",'a')
f.write("\n have a good day"+" this is appended")

f.close