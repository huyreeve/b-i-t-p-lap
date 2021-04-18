s=(input().strip())
s=s.lower()
for i in s:
    if (i<'a' or i>'z') and i!=' ':
        s = s.replace(i, "")
res=s.split(" ")

for i in range( len(res)-1):
    temp=res[i]
    if(len(temp)>0):
        print(temp[0].upper(),end='')
print(".",end='')

temp=res[len(res)-1]
print(temp.capitalize())
# ví dụ test:  Hoang   Mau  Trung
#b1 : chuyển sang chữ thường và xóa dấu cách đầu cuối chuỗi => hoang   mau  trung
#b2: xoá các ký tự gây nhiễu như : . , ; ? ! ...
#b2: s.split(" ") để tách chuỗi :
# với n-1 tiếng đầu thì in hoa chữ cái đầu của 1 tiếng
#còn với tiếng cuối cùng thì dùng capitalize để in hoa chữ cái đầu tiên
"""
temp=res[len(res)-1]
for i in range( len(temp)):
    if i==0:print(temp[i].upper(),end='')
    else: print(temp[i],end='')
"""