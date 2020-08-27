import re

string=" This is @aanandkassu, mohit, @lucky."
pattern='@([a-z]+)'

# res=re.findall(pattern,string)
res=re.search(pattern,string)
if res==None:
    print(" not found")
else:
    print("match :{}".format(res.group()) )