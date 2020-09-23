This kernel is InceptionV3 that written by Tensorflow. Web: https://keras.io/api/applications/inceptionv3/

Task: Binary classification of images of women and men

1. Preparing images for training
For loading images and taking them to model I used ImageDataGenerator from keras.preprocessing.image: the generator was created so that we do not load RAM with images, we transform them right before uploading them to the network
Unusual parameters for training data generator: shear_range - counterclockwise shift angle in degrees, set to 0.2; zoom_range - the range for the random zoom, set to 0.2; horizontal_flip - randomly flip inputs horizontally. I used it to make flaxible model

2. Model
I haven't chosen all of Inception V3 for this task
Parameters:
*include_top=False : we don't need fully connected layer with 1000 outputs
*weights='imagenet' : we need weights from ImageNet
*new_output = keras.layers.GlobalAveragePooling2D()(model.output) : global pooling like in InceptionV3
*new_output = keras.layers.Dense(1, activation='sigmoid')(new_output) : fully connected layer with 1 output

Summary of model you can check in file named "Model_summary.txt"

3. Results


https://drive.google.com/file/d/1cVNz9MQpnw2X6ecds5L0SYSLMt923YU3/view?usp=sharing
