import os
os.system('clear')

nation = {'Korea':'+82', "US":"+1", "Japan":"+81"}
print(nation["US"])
var = input()

if(var in nation):
  print("contury code =", nation["US"])
else:
  print("something wrong")