#How does data enable machine learning

#ex: images of animals
input = [1,2,3,4,5]

#ex: animal name
output = [2,4,6,8,10]

#what is rule based programming
def smart_function(x):
    li = []
    for item in x:
        li.append(item * 2)
    return li
print(smart_function(input))

#Three ingredients of machine learning: data, model, feedback loop

#data:
input, output

#model
#tell the machine what it is allowed to do in order to create the output from the input
#linear model = input * constant

#feedback loop
#error = machine_learned_output - output
input:output = 1:2
model prediction[1] = 3
error = 3 - 2 = 1

#what is a machine learning model? (real life simplification)
