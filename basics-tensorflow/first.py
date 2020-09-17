import tensorflow as tf

import sys
from numpy import *


#load mnist data
# x_train is image data and y_train its label
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


#Convert the samples from integers to floating-point numbers:
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)), # converting 28*28 matrix into array of 276
  tf.keras.layers.Dense(128, activation='relu'), # decreasing array size from 276 to 126 using fxn=relu
  #tf.keras.layers.Dense(50, activation='sigmoid'), # decreasing array size from 276 to 126 using fxn=relu,
  tf.keras.layers.Dropout(0.2), #remove 20% data randomaly to remove overfitting
  tf.keras.layers.Dense(10) # decreasing array size from (20% of 126 = 100) to 10 outputs
])
predictions = model(x_train[:1]).numpy()
predictions
print (predictions)

tf.nn.softmax(predictions).numpy()

# design your own loss function
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
# tell the model giving your loss fxn and the expected output
loss_fn(y_train[:1], predictions).numpy()

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

# 
model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)

probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])

probability_model(x_test[:5])

