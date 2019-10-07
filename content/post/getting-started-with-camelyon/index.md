+++
title = "Getting Started With Camelyon (Part 1)"
subtitle = ""

# Add a summary to display on homepage (optional).
summary = "This post is the first of a three post series on using deep learning to tackle the CAMELYON Challenge. This first post covers basic convolutional neural network training using the PatchCAMELYON dataset and TensorFlow 2.0."

date = 2019-04-24T13:41:43+02:00
draft = false

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["geert"]

# Is this a featured post? (true/false)
featured = false

# Tags and categories
# For example, use `tags = []` for no tags, or the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["CAMELYON", "machine learning", "tutorial"]
categories = []

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["deep-learning"]` references 
#   `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
# projects = ["internal-project"]

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
[image]
  # Caption (optional)
  caption = ""

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = ""
  preview_only = true
+++

This is the first part of a three part tutorial on how to get started with the [CAMELYON dataset](https://camelyon17.grand-challenge.org). This first part will focus on getting a basic convolutional neural network trained using [PatchCAMELYON](https://github.com/basveeling/pcam), TensorFlow 2.0, Keras and TensorFlow Datasets. Part 2 will cover applying your trained model to a whole-slide image and visualizing the results and Part 3 will cover how to use the full dataset to train a model at different resolution levels, sampling strategies, and data augmentation.

To get started you need to setup a Python environment with NumPy, Matplotlib and TensorFlow 2.0. To use the PatchCAMELYON dataset with TensorFlow Datasets you will need to use my fork of the project for now as the pull request to add PatchCAMELYON to the master branch is not yet approved. To this end you need to do clone the repository and add it to your Python environment:


```bash
git clone https://github.com/GeertLitjens/tensorflow_datasets
cd tensorflow_datasets
python setup.py develop
```

After this step you should be able to import the relevant packages with the following cell


```python
# Import NumPy to handle array's and Matplotlib for plotting loss curves
import numpy as np
import matplotlib.pyplot as plt

# Import TensorFlow and relevant Keras classes to setup the model
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPool2D, Flatten, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint
```

The next cell will automatically download PatchCAMELYON from Zenodo and prepare the TensorFlow Datasets


```python
import tensorflow_datasets as tfds
pcam, pcam_info = tfds.load("patch_camelyon", with_info=True)
print(pcam_info)
```
>```python
    tfds.core.DatasetInfo(
        name='patch_camelyon',
        version=1.0.0,
        description='The PatchCAMELYON dataset for identification of breast cancer metastases in lymph nodes. This dataset has been extracted from the larger CAMELYON dataset of 1399 whole-slide images, which created for the CAMELYON challenges at ISBI 2016 and 2017.It contains 96x96 RGB patches of normal lymph node and tumor tissue in a roughly 50/50 distributions. It packs the clinically-relevant task of metastasis detection into a straight-forward image classification task, akin to CIFAR-10 and MNIST. This increases the ease of use by removing the complexity of handling large whole-slide images.',
        urls=['https://github.com/basveeling/pcam', 'https://camelyon17.grand-challenge.org/'],
        features=FeaturesDict({
            'image': Image(shape=(96, 96, 3), dtype=tf.uint8),
            'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2)
        },
        total_num_examples=327680,
        splits={
            'test': <tfds.core.SplitInfo num_examples=32768>,
            'train': <tfds.core.SplitInfo num_examples=262144>,
            'validation': <tfds.core.SplitInfo num_examples=32768>
        },
        supervised_keys=('image', 'label'),
        citation='"""
            @ARTICLE{Veeling2018-qh,
              title         = "Rotation Equivariant {CNNs} for Digital Pathology",
              author        = "Veeling, Bastiaan S and Linmans, Jasper and Winkens, Jim and
                               Cohen, Taco and Welling, Max",
              month         =  jun,
              year          =  2018,
              archivePrefix = "arXiv",
              primaryClass  = "cs.CV",
              eprint        = "1806.03962"
            }
            @article{Litjens2018,
                author = {Litjens, G. and Bándi, P. and Ehteshami Bejnordi, B. and Geessink, O. and Balkenhol, M. and Bult, P. and Halilovic, A. and Hermsen, M. and van de Loo, R. and Vogels, R. and Manson, Q.F. and Stathonikos, N. and Baidoshvili, A. and van Diest, P. and Wauters, C. and van Dijk, M. and van der Laak, J.},
                title = {1399 H&E-stained sentinel lymph node sections of breast cancer patients: the CAMELYON dataset},
                journal = {GigaScience},
                volume = {7},
                number = {6},
                year = {2018},
                month = {05},
                issn = {2047-217X},
                doi = {10.1093/gigascience/giy065},
                url = {https://dx.doi.org/10.1093/gigascience/giy065},
                eprint = {http://oup.prod.sis.lan/gigascience/article-pdf/7/6/giy065/25045131/giy065.pdf},
            }
            
        """',
        redistribution_info=,
    )
```
    

Now we have our dataset ready, it is time to define our model. The cell below defines a very simple VGG-like convolutional neural network using Keras.


```python
#First setup the input to the network which has the dimensions of the patches contained within PatchCAMELYON
input_img = Input(shape=(96,96,3))

# Now we define the layers of the convolutional network: three blocks of two convolutional layers and a max-pool layer.
x = Conv2D(16, (3, 3), padding='valid', activation='relu')(input_img)
x = Conv2D(16, (3, 3), padding='valid', activation='relu')(x)
x = MaxPool2D(pool_size=(2,2), strides=(2,2))(x)
x = Conv2D(32, (3, 3), padding='valid', activation='relu')(x)
x = Conv2D(32, (3, 3), padding='valid', activation='relu')(x)
x = MaxPool2D(pool_size=(2,2), strides=(2,2))(x)
x = Conv2D(64, (3, 3), padding='valid', activation='relu')(x)
x = Conv2D(64, (3, 3), padding='valid', activation='relu')(x)
x = MaxPool2D(pool_size=(2,2), strides=(2,2))(x)

# Now we flatten the output from a 4D to a 2D tensor to be able to use fully-connected (dense) layers for the final
# classification part. Here we also use a bit of dropout for regularization. The last layer uses a softmax to obtain class
# likelihoods (i.e. metastasis vs. non-metastasis)
x = Flatten()(x)
x = Dense(256, activation='relu')(x)
x = Dropout(rate=0.2)(x)
x = Dense(128, activation='relu')(x)
x = Dropout(rate=0.2)(x)
predictions = Dense(2, activation='softmax')(x)

# Now we define the inputs/outputs of the model and setup the optimizer. In this case we use regular stochastic gradient
# descent with Nesterov momentum. The loss we use is cross-entropy and we would like to output accuracy as an additional metric.
model = Model(inputs=input_img, outputs=predictions)
sgd_opt = SGD(lr=0.01, momentum=0.9, decay=0.0, nesterov=True)
model.compile(optimizer=sgd_opt,
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.summary()
```
> ```text
 Model: "model"
 _________________________________________________________________
 Layer (type)                 Output Shape              Param #   
 =================================================================
 input_1 (InputLayer)         [(None, 96, 96, 3)]       0         
 _________________________________________________________________
 conv2d (Conv2D)              (None, 94, 94, 16)        448       
 _________________________________________________________________
 conv2d_1 (Conv2D)            (None, 92, 92, 16)        2320      
 _________________________________________________________________
 max_pooling2d (MaxPooling2D) (None, 46, 46, 16)        0         
 _________________________________________________________________
 conv2d_2 (Conv2D)            (None, 44, 44, 32)        4640      
 _________________________________________________________________
 conv2d_3 (Conv2D)            (None, 42, 42, 32)        9248      
 _________________________________________________________________
 max_pooling2d_1 (MaxPooling2 (None, 21, 21, 32)        0         
 _________________________________________________________________
 conv2d_4 (Conv2D)            (None, 19, 19, 64)        18496     
 _________________________________________________________________
 conv2d_5 (Conv2D)            (None, 17, 17, 64)        36928     
 _________________________________________________________________
 max_pooling2d_2 (MaxPooling2 (None, 8, 8, 64)          0         
 _________________________________________________________________
 flatten (Flatten)            (None, 4096)              0         
 _________________________________________________________________
 dense (Dense)                (None, 256)               1048832   
 _________________________________________________________________
 dropout (Dropout)            (None, 256)               0         
 _________________________________________________________________
 dense_1 (Dense)              (None, 128)               32896     
 _________________________________________________________________
 dropout_1 (Dropout)          (None, 128)               0         
 _________________________________________________________________
 dense_2 (Dense)              (None, 2)                 258       
 =================================================================
 Total params: 1,154,066
 Trainable params: 1,154,066
 Non-trainable params: 0
 _________________________________________________________________
```    

To keep the dataset size small PatchCAMELYON is stored as int8 patches. For network training we need float32 and we want to normalize between 0 and 1. The function below performs this task.


```python
def convert_sample(sample):
    image, label = sample['image'], sample['label']  
    image = tf.image.convert_image_dtype(image, tf.float32)
    label = tf.one_hot(label, 2, dtype=tf.float32)
    return image, label
```

Now we use the `tf.data` pipeline to apply this function to the dataset in a parallel fashion. We also shuffle the training data with a shuffle buffer (which is randomly filled with samples from the dataset) of 1024. Next we define batches of 64 patches for training and 128 for validation. Last, we prefetch 2 batches such that we can get batches during training on the GPU.


```python
train_pipeline = pcam['train'].map(convert_sample,
                                   num_parallel_calls=8).shuffle(1024).repeat().batch(64).prefetch(2)
valid_pipeline = pcam['validation'].map(convert_sample,
                                        num_parallel_calls=8).repeat().batch(128).prefetch(2)
```

Now we just apply train and evaluate the model using our dataset pipeline. We pick the steps per epoch such that the entire training and validation set are covered each epoch. We keep the History object that `fit` returns to plot the loss progression later on. We now just do 5 epochs for illustration purposes. Feel free to experiment with the number of epochs. If you want to keep the best model during training you can use the Keras `ModelCheckpoint` callback to write each improvement to disk.


```python
hist = model.fit(train_pipeline,
                 validation_data=valid_pipeline,
                 verbose=2, epochs=5, steps_per_epoch=4096, validation_steps=256)
```
>```text
 Epoch 1/5
 4096/4096 - 101s - loss: 0.6756 - accuracy: 0.5501 - val_loss: 0.5228 - val_accuracy:  0.7527
 Epoch 2/5
 4096/4096 - 98s - loss: 0.4292 - accuracy: 0.8071 - val_loss: 0.3946 - val_accuracy:  0.8249
 Epoch 3/5
 4096/4096 - 99s - loss: 0.3165 - accuracy: 0.8675 - val_loss: 0.3634 - val_accuracy:  0.8390
 Epoch 4/5
 4096/4096 - 100s - loss: 0.2586 - accuracy: 0.8958 - val_loss: 0.3707 - val_accuracy:  0.8340
 Epoch 5/5
 4096/4096 - 99s - loss: 0.2260 - accuracy: 0.9118 - val_loss: 0.3353 - val_accuracy:  0.8568
```    

If we are happy with our performance on the validation set we can check whether it generalized to the test set. Note that it is bad practice to look at your test set performance too often; you will start making modification to your network/training procedure to optimize test set performance which results in optimistically biased performance estimates.


```python
test_pipeline = pcam['test'].map(convert_sample, num_parallel_calls=8).batch(128).prefetch(2)
print("Test set accuracy is {0:.4f}".format(model.evaluate(test_pipeline, steps=128, verbose=0)[1]))
```
>```text
 Test set accuracy is 0.8563
```    

If we are happy with the performance we can write the model to disk.


```python
model.save("./patchcamelyon.hf5")
```

If you followed along with all the steps you should get a test set performance between 0.8 and 0.87. Differences occur due to different weight initialization of the network for example. To make network training more reproducible you can specify the random seed for the weight initializers manually. Note that the training process cannot be fully deterministic due to backpropogation step in the CUDNN library not being deterministic. I hope you enjoyed this brief tutorial, the next post will be about how to use our saved model to classify a whole-slide image.
