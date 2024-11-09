#Create a set using curly brasksets

my_set = {1,2,3}

#print(my_set)

#create a set from a list using the set() function
#my_set = ([4,5,6])
#print(my_set)

#Create an empty set using the set() function
#my_set = set()
#print(my_set)

#my_set = {1,1,2,3,3,4,5,3,2,3}
#print(my_set) #set will automaticlly remove duplicates


##################


set1 = {1,2,3}
set2 = {1,2,3}

print(union_method)
#union betweem set 1 and set2 using thhe union method

union_method = set1.union(set2)

union_operator = set1 | set2

print("uniono of set and set2 using method: ", union_method)
print("uniono of set and set2 using operator: ", union_method)

#compute intersection between set1 and set2 using the intersection() method

intersection_method = set1.intersection(set2)

#compute intersection between set1 and set2 using & operatore

intersection_operator = set1 & set2
print("intersection of set1 and set2 using the intersection method",   intersection_method)
print("intersection of set1 and set2 using the intersection operator",   intersection_operator

difference_method = set1.difference(set2)

difference_operator = set1 - set2
print("difference of set1 and set2 using the difference method",   difference_method
print("difference of set1 and set2 using the - operator",   difference_operator

symetric_difference_method = set1,symetric_difference(set2)

symetric_difference_operator = set1 ^ set2

print("symetric difference set1 and set2 using symetric difference operator",      symetric_difference_operator)
print("symetric difference set1 and set2 using symetric difference method",      symetric_difference_method)
my_set = {1,2,3}

my_set.add(7)

my_set.remove(3)

my_set.discard(8)

print(my_set)

my_set.clear()

my_list = [1,2,2,3,4,4,5,6]

uniqe_set =set(my_list)

print(uniqe_set)

uniqe_list = list(uniqe_set)
print(uniqe_set)

yllis_intrests = {"music", "movies", "travel"}
drilonis_intrests = {"movies", "games",  "skiing"}

common_interests = yllis_intrests.intersection(drilonis_intrests)
print(common_interests)

colors = {"red", "purple", "yellow"}
