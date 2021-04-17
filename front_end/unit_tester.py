from _Saveable import Saveable
from _Feature import Feature
from _Feature_Data_Struct import Feature_Data_Struct


s = Saveable(file_location="bob")
print(s)
##Feature testt
f_1 = Feature(name = "chicken",value=5,weight=6)
f_2 = Feature(name = "chicken",value=5,weight=6)
f_3 = Feature(name = "Bird",value=5,weight=6)
f_4 = Feature(name = "chicken",value=5,weight=6)
print("f1",f_1)
print("f2",f_2)
print("f3",f_3)
print("f1 = f2",f_1==f_2)
print("f1 = f3",f_1==f_3)
print("f1 > f2",f_1>f_2)
print("f1 > f3",f_1>f_3)
print("f1 < f2",f_1<f_2)
print("f1 < f3",f_1<f_3)

##Feature_data_struct testt
ls_f = [f_1,f_2,f_3,f_4]
ls_f2 = [f_1,f_1,f_1,f_1]


fds = Feature_Data_Struct(ls_f)
print("ls_f",fds)
fds.sort()

fds_1 = Feature_Data_Struct(ls_f2)
print("sort ls_f",fds)
print("fds==fds",fds==fds)
print("fds==fds_1",fds==fds_1)

