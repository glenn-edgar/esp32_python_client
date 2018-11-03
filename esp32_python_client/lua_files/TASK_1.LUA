

print("this is a lua test \n")
print("executing do file \n")
dofile("/spiffs/common.lua")
print("back from do file \n")
x = {1,2,3,4,5,6}
y = cmsgpack.pack(x)
print(y)
w = {}
w ["name"]="test"
w["data"] = x
z = cmsgpack.pack(w)
print(z)
print("unpacking y",table_dump(cmsgpack.unpack(y)))
print("unpacking z",table_dump(cmsgpack.unpack(z)))
print("keys of w",table_dump(keys(w)))
print("bye \n")
