#1.1

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
#input:output = 1:2
model prediction[1] = 3
error = 3 - 2 = 1

#1.2 - Tasks
#Machine learning is all about making predictions
#Regression is the task of predicting numbers

input = [0,1,2,3,4]
output = [0,2,4,6,8]

# Classification is the task of predicting labels
input = [0,1,2,3,4]
labels = ["mouse", "cat", "dog", "car"]

# other predictive tasks
# recommendations, clusters

#  1.4 - Learning methods

# Supervised Learning
# regression task example
input = [1,2,3,4,5]
output = [2,4,6,8,10]

# Unsupervised Learning
 input = [1,2,3,4,5,6,7,8]

# Reinforcement Learning
state = (internal_state, environment)
action = prediction


