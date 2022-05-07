# # string concatenation (aka how to put  string together)

# name = "Aaron"

# # a few ways to create strings
# print ("hello there, " + name)
# print ("hello there, {}".format(name))
# print (f"hello there, {name}")
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person:")
madlib = f"Computer programing is so {adj}! It makes me soo excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

print(madlib)