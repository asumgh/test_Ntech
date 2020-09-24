# -*- coding: utf-8 -*-
# """Training model InceptionV3"""
# import sys
# sys.path.append("..")

# #Load libraries which helps us with building model
# #
# import keras
# from keras.preprocessing.image import ImageDataGenerator

# import keras_utils
# from keras_utils import reset_tf_session

# #Size of images
# #
# IMG_SIZE = 250


# def inception(use_imagenet=True):
#     """The main frame of our model. Input: None; Output: model of NN"""
#     model = keras.applications.InceptionV3(include_top=False, input_shape=(IMG_SIZE, IMG_SIZE, 3),
#                                           weights='imagenet' if use_imagenet else None)
#     new_output = keras.layers.GlobalAveragePooling2D()(model.output)
#     new_output = keras.layers.Dense(1, activation='sigmoid')(new_output) # for binary classification
#     model = keras.engine.training.Model(model.inputs, new_output)
#     return model

# #Building model
# #
# model = inception()

# #Set all layers trainable by default
# #
# for layer in model.layers:
#     layer.trainable = True
#     if isinstance(layer, keras.layers.BatchNormalization):
#         # parameters to faster adjust to our new dataset
#         layer.momentum = 0.9

# #Fixing deep layers (fine-tuning only last 50)
# #
# for layer in model.layers[:-50]:
#     #Fixing all but batch norm layers, because we neeed to update moving averages for a new dataset
#     if not isinstance(layer, keras.layers.BatchNormalization):
#         layer.trainable = False

# #Compile our model
# #
# model.compile(
#     loss='binary_crossentropy',
#     optimizer=keras.optimizers.Adamax(lr=1e-4),
#     metrics=['accuracy'],
# )

# #Size of batches which we use for training
# #
# batch_size = 32

# #Frame of train generator
# #
# train_datagen = ImageDataGenerator(
#         rescale=1./255,
#         shear_range=0.2,
#         zoom_range=0.2,
#         horizontal_flip=True)

# #Frame of test generator
# #
# test_datagen = ImageDataGenerator(rescale=1./255)

# #Train generator
# #
# train_generator = train_datagen.flow_from_directory(
#         'internship_data/train/',
#         target_size=(IMG_SIZE, IMG_SIZE),
#         batch_size=batch_size,
#         class_mode='binary')

# #Test generator
# #
# validation_generator = test_datagen.flow_from_directory(
#         'internship_data/valid/',
#         target_size=(IMG_SIZE, IMG_SIZE),
#         batch_size=batch_size,
#         class_mode='binary')


# #We must do it to prevent memory overflow
# #
# s = reset_tf_session()

# #Train our model
# #
# model.fit(
#         train_generator,
#         steps_per_epoch=len(train_generator) // 8,
#         epochs=16,
#         validation_data=validation_generator, 
#         validation_steps=len(validation_generator) // 4,
#         callbacks=[keras_utils.TqdmProgressCallback()],
#         verbose=0
# )

# eval_score = model.evaluate_generator(
#     validation_generator, 
#     len(validation_generator) // 4
# )
# print("Evaluation score = {}".format(eval_score[1]))

# #Save the model to use it in the future
# #
# model.save('my_model.h5')
