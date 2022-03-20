#type data distionari
dic={"alim":23,"adri":34,"arif":35}
itms=dic.items()
for i,j in itms:
    print(i,":",j)
#mengubdate
dic={"alim":23,"adri":34,"arif":35}
dic["alim"]=100
print(dic)
#menghapus
dic={"alim":23,"adri":34,"arif":35}
del dic["alim"]
print(dic)
#menambah
dic={"alim":23,"adri":34,"arif":35}
dic["awal"]=78
print(dic)