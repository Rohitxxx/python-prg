class myStringFun:
    def __init__(self,str):
        self.str=str
    def countStr(self,ch):
        count=0
        for index in range(0,len(self.str)):
            if(self.str[index] == ch):
                count+=1
        return count
    def xcapitalize(self,source):
        desti=" "
        for index in range(0,len(source)):
            if(source[index]>='a' and source[index]<='z'):
                desti=desti+chr(ord(source[index])-32)
            elif source[index]>='A' and source[index]<='Z':
                desti=desti+source[index]
            

        return desti

#print(ord('a')-ord('A'))
#print('s'>'a')
obj=myStringFun("rsohissssst")
#print(obj.countStr("s"))
print(obj.xcapitalize("rohIt"))
