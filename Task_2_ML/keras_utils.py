# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# from collections import defaultdict
# import numpy as np
# from keras.models import save_model
# import tensorflow as tf
# import keras
# from keras import backend as K
# import tqdm_utils


# class TqdmProgressCallback(keras.callbacks.Callback):

#     def on_train_begin(self, logs=None):
#         self.epochs = self.params['epochs']

#     def on_epoch_begin(self, epoch, logs=None):
#         print('\nEpoch %d/%d' % (epoch + 1, self.epochs))
#         if "steps" in self.params:
#             self.use_steps = True
#             self.target = self.params['steps']
#         else:
#             self.use_steps = False
#             self.target = self.params['samples']
#         self.prog_bar = tqdm_utils.tqdm_notebook_failsafe(total=self.target)
#         self.log_values_by_metric = defaultdict(list)

#     def _set_prog_bar_desc(self, logs):
#         self.log_values_by_metric['accuracy'].append(logs['accuracy'])
#         desc = "; ".join("{0}: {1:.4f}".format(k, np.mean(values)) for k, values in self.log_values_by_metric.items())
#         if hasattr(self.prog_bar, "set_description_str"):
#             self.prog_bar.set_description_str(desc)
#         else:
#             self.prog_bar.set_description(desc)

#     def on_batch_end(self, batch, logs=None):
#         logs = logs or {}
#         if self.use_steps:
#             self.prog_bar.update(1)
#         else:
#             batch_size = logs.get('size', 0)
#             self.prog_bar.update(batch_size)
#         self._set_prog_bar_desc(logs)

#     def on_epoch_end(self, epoch, logs=None):
#         logs = logs or {}
#         self._set_prog_bar_desc(logs)
#         self.prog_bar.update(1)
#         self.prog_bar.close()


# class ModelSaveCallback(keras.callbacks.Callback):

#     def __init__(self, file_name):
#         super(ModelSaveCallback, self).__init__()
#         self.file_name = file_name

#     def on_epoch_end(self, epoch, logs=None):
#         model_filename = self.file_name.format(epoch)
#         save_model(self.model, model_filename)
#         print("Model saved in {}".format(model_filename))


# def reset_tf_session():
#     curr_session = tf.compat.v1.get_default_session()
#     # close current session
#     if curr_session is not None:
#         curr_session.close()
#     # reset graph
#     K.clear_session()
#     # create new session
#     config = tf.compat.v1.ConfigProto(allow_soft_placement=True)
#     config.gpu_options.allow_growth = True
#     s = tf.compat.v1.InteractiveSession(config=config)
#     tf.compat.v1.keras.backend.set_session(s)
#     return s
