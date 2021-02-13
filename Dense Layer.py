# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 17:16:12 2021

@author: Divyanshu
"""
# Dense Layer from Scratch

from tensorflow import tf

class MyDenseLayer(tf.keras.layers.Layer):
    def __init__(self, input_dim, output_dim):
        super(MyDenseLayer, self).__init__()
        
        #Initialize weights and bias
        self.W = self.add_weight([input_dim,output_dim])
        self.b = self.add_weight([1, output_dim])
    
    def call(self, inputs):
        #Forward propagate the inputs
        z = tf.matmul(inputs, self.W) + self.b
        
        #Feed through a non-linear activation
        output = tf.math.sigmoid(z)
        
        return output3