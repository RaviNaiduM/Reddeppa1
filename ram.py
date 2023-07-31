# # list1=["apple","mango","orange","banana","grapes","kiwi"]
# #
# # #list1.append("naresh")
# #
# # list1.insert(0,"rajesh")
# #
# # print(list1)
#
# #
# # # example of tuple
# # tuple=["apple","mango","orange","banana","grapes","kiwi"]
# #
# # print(tuple)
#
# # access the items
# #
# # tuple=["apple","mango","orange","banana","grapes","kiwi"]
# #
# # print(tuple[1])
#
# # range of indexes
# #
# # tuple=["apple","mango","orange","banana","grapes","kiwi"]
# #
# # print(tuple[2:5])
#
# # # how can we change tuple item value it's not changable...
# # tuple=["apple","mango","orange","banana","grapes","kiwi"]
# #
# # print(tuple.insert(0,"ramesh"))
#
# # changing the tuple items
# #list1=["apple","mango","orange","banana","grapes","kiwi"]
# #
# # list1 = list(tuple1)
# #
# # print(list1)
# #
# # list1[0] = "RameshNaidu"
# # tuple1 = list(list1)
# #
# # print(tuple1)
#
# # tuples comparision in Python
#
# # tuple1 =("1","2","3")
# #
# # tuple2 =("4","5","6")
# #
# # if tuple1 == tuple2:
# #     print("both are eqval")
# # else:
# #     print("not eqval")
#
#
# # dictionary
#
# dic = {1:"ramesh",2:"mahesh",3:"arun",4:"tharun"}
#
# print(dic)
#
# # accessing items from dictionary
#
# dic1={"brand":"car",
#       "model":"i10",
#       "year":2021
#       }
#
#
# print(dic1["brand"])
#
# # using get()
#
# print(dic1.get("brand"))
#
# for i in dic1:
#     print(dic1[i])
#
# for x,y in dic1.items():
#     print(x,y)  # print keys along with the values

# check key exist or not

dic1={"brand":"car",
      "model":"i10",
      "year":2021
   }


if "model" in dic1:
    print("present")
else:
    print("not exist")








