ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

world = "World!"
countryCampus = "Germany!"
cityCampus = "Wolfsburg!"
nameCampus = "42Wolfsburg"

ft_list[1] = world
# ft_tuple[1] = countryCampus  # TypeError: 'tuple'
# object does not support item assignment
ft_tuple = ft_tuple[0:1] + (countryCampus,)
# tuples and strings are immutable
# thats why we have to change the touple itself
# ft_set["tutu!"] = cityCampus   Sets are unordered,
# so this doesn't guarantee position
ft_set.remove("tutu!")
ft_set.add(cityCampus)
ft_dict["Hello"] = nameCampus

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
