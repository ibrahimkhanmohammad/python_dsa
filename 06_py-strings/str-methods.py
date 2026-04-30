movie_name = "The lion King"
print(movie_name.lower())
print(movie_name)   #original content doesn't change so str is immutable in py
print(movie_name.upper())
print(movie_name.capitalize())
print(movie_name.title())
print(movie_name.isdigit())
print(movie_name.find('King'))
print(movie_name.find('king'))  #returns -1 if 'king' isn't available in the <str>
print(movie_name.count('king')) #returns 0 if 'king' isn't available in the <str>
print(movie_name.count('King'))
print(movie_name.find('i'))     #returns the index of first occurence of 'i' in the <str>
print(movie_name.rfind('i'))    #returns the index of 'i' from reverse order in the <str>
print(movie_name.replace('King', 'Queen'))

print(help(str))    #to get help in <str>
print(help(str.count))  #to get help in count method of <str>

name = "Rahul"
age = 34
field = "cricketer"

print("{} is of {} years old and is an indian {}".format(name, age, field)) #we must have to pass the arguments i.e; variables inside the format as we're writing inside the print statement