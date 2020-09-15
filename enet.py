import keras
from keras.models import Model
from keras.layers import Input, merge
from keras.layers import Dense, Activation, Flatten, BatchNormalization
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D


def initial(input):
    main = Conv2D(filters=13, kernel_size=3, strides=(2, 2), padding='same')(input)
    maxPool = MaxPooling2D(pool_size=(2, 2), strides=None)(input)
    concat = concatenate([main, maxPool])
    return concat

def dilated_bottleneck(input, output_filters, downsample, dilation, dropout):
    #need to add downsampling of filters
    if (downsample):
        stride = 2
    else:
        stride = 1
       
    
    return

def asymmetric_bottleneck():
    x = Conv2D(filters=reduce, kernel_size=(1,5), padding='same', use_bias=False)
    x = Conv2D(filters=reduce, kernel_size=(5,1), padding='same', use_bias=False)
    return

def upsampling_bottleneck():
    return 

def full_conv():
    return


#combining to bottleneck layers
#add together
