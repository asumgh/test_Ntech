# -*- coding: utf-8 -*-
"""Code for making prediction by model InceptionV3"""
#System libraries
#
import sys
import os
sys.path.append("..")
#Load libraries which helps us with building model
#

#Neural network framework
#
import keras

#For images
#
import cv2

#Algebra
#
import numpy as np

#For Data Frame
#
import pandas as pd

#Size of images
#
IMG_SIZE = 250

#Read name of directory
#
directory = sys.argv[1]

#Get all file names
#
all_files = os.listdir(directory)

#Prepared model
#
my_model = keras.models.load_model('my_model.h5')

#Size of each batch
#
batch_size = 32


def batch_generator(items, batch_size):
    '''Generating batches'''
    k = batch_size
    for item in items:
        if k == batch_size:
            list_items = []
        if k>0:
            list_items.append(item)
            k-=1
            if k==0:
                k=batch_size
                yield list_items
    if k>0:
        yield list_items


def predict_generator(files, batch_size, directory):
    '''Making row of numbers for each batch of images'''
    for batch in batch_generator(files, batch_size):
        batch_imgs = []
        for name in batch:
            img = cv2.imread(directory+name)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            img = img.astype("float32")
            img = keras.applications.inception_v3.preprocess_input(img)
            batch_imgs.append(img)
        batch_imgs = np.stack(batch_imgs, axis=0)
        yield batch, batch_imgs


#Making prediction of each batch
#
names = []
predicts = []
for item in predict_generator(all_files, batch_size, directory):
    names+=item[0]
    predicts+=[n[0] for n in my_model.predict(item[1])]


#Making DataFrame and json with predictions
#
df_predicts = pd.DataFrame(columns = ['Pred_num'], data = np.asarray([np.round(i) for i in predicts]))
df_predicts.loc[df_predicts.Pred_num == 1, 'Pred'] = 'male'
df_predicts.loc[df_predicts.Pred_num == 0, 'Pred'] = 'female'
df_predicts.drop(columns = ['Pred_num'], inplace = True)
df_predicts.index = np.array(names).reshape(-1)

df_predicts['Pred'].to_json('process_results.json')

