from _Ingrediant_Vector import Ingrediant_Vector
from _Menu_Matrix import Menu_Matrix
from _Profile import Profile
        #chicken,beef,cheese
ls_pref= [0,1,1]
ls_chicken_curry = [1,0,0]
ls_beef_curry = [0,1,0]
ls_cheese_pizza = [0,0,1]
ls_duck_salad = [0,0,0]


profile = Ingrediant_Vector(vector_ls= ls_pref)

recipe_1 = Ingrediant_Vector(vector_ls =ls_chicken_curry,name = "chicken_curry")
recipe_2 = Ingrediant_Vector(vector_ls =ls_beef_curry,name ="beef_curry ")
recipe_3 = Ingrediant_Vector(vector_ls =ls_cheese_pizza,name ="cheese_pizza ")
recipe_4 = Ingrediant_Vector(vector_ls =ls_duck_salad,name ="duck_salad ")

print(recipe_1)
menu_ls = [recipe_1,recipe_2,recipe_3,recipe_4]
restraunt_1 = Menu_Matrix(list_features = menu_ls)
print(profile.get_vector())
print(restraunt_1.get_menu())
print (restraunt_1.angle_similarity_vect(profile.get_vector()))

print ("closest(1st occurance)",restraunt_1.get_close_recomendation(profile))
print ("farthest(1st occurance)",restraunt_1.get_far_recomendation(profile))

jordan = Profile("ji@Bmail.com","password",profile,user_ID= None)

print (jordan.user_name,"with a profile",restraunt_1.get_close_recomendation(jordan.get_Profile_Features()))

#print("profile" , pf)






