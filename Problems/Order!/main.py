a = int(input().strip())
b = int(input().strip())
c = int(input().strip())
fs = a < b
# ®print(fs, "FS")
if fs is False:
    print("False")
elif b < c:
    print("True")
else:
    print("False")
# 1 3 2 True
