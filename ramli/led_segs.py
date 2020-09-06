import numpy as np
# from keras.models import Sequential
from tensorflow.keras.models import Sequential
from keras.layers.core import Activation, Dense
from keras.optimizers import SGD

# Trains a neural net that recognizes the digit displayed by a 7-segment LED:
# "Lit segments" are indexed as:
#  -- 0 --
# |        |
# 1        2
# |        |
#  -- 3 --
# |        |
# 4        5
# |        |
#  -- 6 --
#
# For instance "2" = [1, 0, 1, 1, 1, 0, 1]

# The testing data is a 10 x 7 array. A single row are the segments on the LED (e.g., 1,1,1,0,1,1,1 => "0") and there are 10 rows
x = np.zeros((10, 7), dtype='uint8')
# The output is a array of length 10. A single row is the one-hot encoded value of the equivalent 7-segment source
y = np.zeros((10, 10), dtype='uint8')

# This is the 7-segment map. x = input, y = output

x[0] = [1, 1, 1, 0, 1, 1, 1]
x[1] = [0, 0, 1, 0, 0, 1, 0]
x[2] = [1, 0, 1, 1, 1, 0, 1]
x[3] = [1, 0, 1, 1, 0, 1, 1]
x[4] = [0, 1, 1, 1, 0, 1, 0]
x[5] = [1, 1, 0, 1, 0, 1, 1]
x[6] = [1, 1, 0, 1, 1, 1, 1]
x[7] = [1, 0, 1, 0, 0, 1, 0]
x[8] = [1, 1, 1, 1, 1, 1, 1]
x[9] = [1, 1, 1, 1, 0, 1, 1]
# Here's the desired output, in "1-hot encoding"
y[0] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y[1] = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
y[2] = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y[3] = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
y[4] = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
y[5] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
y[6] = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
y[7] = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
y[8] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
y[9] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

# A "sequential" neural net is one where the data flows straight from inputs through the layers towards the output
model = Sequential()
# Densely interconnect an input layer consisting of 7 nodes (input_dim = 7) with a middle layer consisting of 4 nodes
# (Experiment with fewer middle layer nodes, possibly with different activation / training times?
# N.B. This also adds bias nodes
model.add(Dense(4, input_dim=7))
# Use the sigmoid activation function between the input layer and the middle layer
model.add(Activation('sigmoid'))

# Densely interconnect the middle layer with the 10 nodes in the output layer
model.add(Dense(10))
# Use the sigmoid activation function between the middle layer and this output layer
model.add(Activation('sigmoid'))

'''
The model is now ready!
7 nodes in the input layer
4 nodes in the middle layer
10 node in the output layer
'''

# Train using "Stochastic Gradient Descent"
sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
# Compile this to the underlying NN library.
model.compile(loss='mean_squared_error', optimizer=sgd, class_mode="binary")

weight_formatter = lambda x: "%.1f" % x
np.set_printoptions(formatter={'float_kind':weight_formatter})

print ("Prior to training weights are:")
for layer in model.layers:
    g=layer.get_config()
    h=layer.get_weights()
    print (g)
    print (h)


# Train. Take 10,000 spins through the training data!
print ("Training...")
history = model.fit(x, y, nb_epoch=10000, batch_size=5, show_accuracy=True, verbose=0)

# Take the input data and predict the outcomes.
print ("Predictions:")
float_formatter = lambda x: "%.0f" % round(x)
np.set_printoptions(formatter={'float_kind':float_formatter})
print (np.matrix(model.predict(x)))
predictArray = model.predict(x)


print ("Subsequent to training weights are:")
np.set_printoptions(formatter={'float_kind':weight_formatter})

for layer in model.layers:
    g=layer.get_config()
    h=layer.get_weights()
    print (g)
    print (h)
