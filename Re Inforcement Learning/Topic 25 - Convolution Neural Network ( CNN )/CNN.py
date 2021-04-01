from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

#Data Generation
from keras.preprocessing.image import ImageDataGenerator

#Image Augmentation
train_datagen = ImageDataGenerator(
        rescale=1./255,                 #Divide the Image by 255 to make all the pixel value from 0 to 1 as RGBrange
                                                                                                    #is from 0 to 255.
        shear_range=0.2,                #Shering Intensiry
        zoom_range=0.2,                 #Zooming Intensity
        horizontal_flip=True,           #Flipping the Image Horizintaly.
        vertical_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

train_set = train_datagen.flow_from_directory(r'C:\Users\gauta\PycharmProjects\MachineLearning\Re Inforcement Learning\Topic 25 - Convolution Neural Network ( CNN )\DataSet\train_data',               #path for the training set
                                                    target_size=(64, 64),           #Expected Size/dimension of Image.
                                                                                           #same as input_shape of Convolution2D()
                                                    batch_size=32,                    #Every time 32 Images will be taken in batch.
                                                    class_mode='binary')                #No of Categories :- binary for 2 categories/ categorical for more than 2 categories

test_set = test_datagen.flow_from_directory(r'C:\Users\gauta\PycharmProjects\MachineLearning\Re Inforcement Learning\Topic 25 - Convolution Neural Network ( CNN )\DataSet\test_data',
                                            target_size=(64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary' )       #colour of Image -> rbf, grayscale, binary

#Neural Network Block
ann = Sequential()
ann.add( Convolution2D( 32, 3, 3, border_mode = 'same', input_shape = ( 64, 64, 3  ), activation = 'relu' ) )

#Applying Pooling the CNN
ann.add( MaxPooling2D( pool_size = ( 2, 2 ) ) )

#Flattening - Input Layer for ANN.
ann.add( Flatten() )

#Full Connection/ Applyin ANN.
ann.add( Dense( output_dim = 128, activation = 'relu') )

ann.add( Dense( output_dim = 1, activation = 'sigmoid' ) )

#Compiling the model.
ann.compile( optimizer = 'adam', loss = 'binary_crossentropy', metrics = [ 'accuracy' ] )

ann.fit_generator(  train_set ,
                    samples_per_epoch = 25000,               #No of Images in training data folder
                    nb_epoch = 1,                           #no. of epoch/ no/ of iteration of CNN.
                    validation_data = test_set,
                    nb_val_samples = 430)               #No of Images in testing data folder


#Prediction Block
import numpy as np
from keras.preprocessing import image

cat_test_image = image.load_img( r'C:\Users\gauta\PycharmProjects\MachineLearning\Re Inforcement Learning\Topic 25 - Convolution Neural Network ( CNN )\DataSet\Single_prediction/Cat_image.jpg'
                              , target_size = ( 64, 64 ) )

dog_test_image = image.load_img( r'C:\Users\gauta\PycharmProjects\MachineLearning\Re Inforcement Learning\Topic 25 - Convolution Neural Network ( CNN )\DataSet\Single_prediction/Dog_image.jpg'
                              , target_size = ( 64, 64 ) )

cat_test_image_arr = image.img_to_array( cat_test_image )
dog_test_image_arr = image.img_to_array( dog_test_image )

print( f"cat_test_image_arr = \n{cat_test_image_arr}\ncat_test_image_arr.shape = { cat_test_image_arr.shape }\n type( cat_test_image_arr ) = { type( cat_test_image_arr ) }\n" )
print( f"dog_test_image_arr = \n{dog_test_image_arr}\ndog_test_image_arr.shape = { dog_test_image_arr.shape }\n type( dog_test_image_arr ) = { type( dog_test_image_arr ) }\n" )

cat_test_image_arr = np.expand_dims( cat_test_image_arr, axis = 0 )
dog_test_image_arr = np.expand_dims( dog_test_image_arr, axis = 0 )

cat_result = ann.predict( cat_test_image_arr )
dog_result = ann.predict( dog_test_image_arr )

print( f"cat_result = { cat_result }" )
print( f"dog_result = { dog_result }\n" )

print( f"cat_result[0] = { cat_result[0] }" )
print( f"dog_result[0] = { dog_result[0] }\n" )

print( f"cat_result[0][0] = { cat_result[0][0] }" )
print( f"dog_result[0][0] = { dog_result[0][0] }\n" )

print( f"train_set.class_indices = { train_set.class_indices }" )