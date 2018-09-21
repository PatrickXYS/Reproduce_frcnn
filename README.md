#**FRCNN for Object Detection**
***
By Yao Xiao

Virginia Tech

##**Use Pre-trained Model To Predict**
***

Use pre-trained model to predict images. You can simply use command line under ./Reproduce_frcnn directory: 

    python test_frcnn.py -p ./img

If you want to use your own images, you can import your images into ./img directory. Then use the above command sentences.

##**Train Your Own Model**
***

You need to first download Pascal_VOC dataset or COCO dataset from:

* 1 Pascal_VOC 2012: 

    http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar   

* 2 COCO 2014: 
    http://images.cocodataset.org/zips/train2014.zip

You need to put dataset under ./Reprouduce_frcnn directory

To train your own model, you can use vgg16, resnet50 or resnet101.

* 1 Vgg16 pre-trained weights: 

    https://github.com/fchollet/deep-learning-models/releases/download/v0.1/vgg16_weights_tf_dim_ordering_tf_kernels.h5

* 2 Resnet50 pre-trained weights:
    
    https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_tf_dim_ordering_tf_kernels.h5

* 3  Resnet101 pre-trained weights:

    https://github.com/keras-team/keras-applications/releases/download/resnet/resnet101_weights_tf_dim_ordering_tf_kernels.h5

You need to put .h5 file under ./Reprouduce_frcnn directory
* 1 Pascal_VOC dataset training:

        python test_frcnn.py -p ./img

        python train_frcnn.py -p ./VOCdevkit/

* 2 COCO dataset training:

        python train_frcnn.py -p ./coco/
