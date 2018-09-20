from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import os


def get_data(input_path):
    all_imgs = []

    classes_count = {}

    class_mapping = {}

    # obtain annotation information
    dataType = 'train2014'
    annFile = '%s/annotations/trainval_ann/instances_%s.json' % (input_path, dataType)

    # init COCO api for annotations
    coco = COCO(annFile)

    cats = coco.loadCats(coco.getCatIds())
    nms = [cat['name'] for cat in cats]
    print('COCO categories: \n\n', ' '.join(nms))

    difficulty = 1

    imgIds = coco.getImgIds()
    for imgId in imgIds:
        img = coco.loadImgs(imgId)

        file_path = '~/coco/images/train2014/%s' %(img['file_name'])
        width =int(img['width'].text)
        height =int(img['height'].text)

        annotation_data = {'filepath': os.path.join(file_path), 'width': width, 'height': height, 'bboxes': []}
        annotation_data['imageset'] = 'trainval'

        annIds = coco.getAnnIds(imgIds=imgId['id'])

        for annId in annIds:
            ann = coco.loadAnns(annId)

            class_name = ann['category_id']

            if class_name not in classes_count:
                classes_count[class_name] = 1
            else:
                classes_count[class_name] += 1

            if class_name not in class_mapping:
                    class_mapping[class_name] = len(class_mapping)

            cent_x = ann['bbox'][0]; cent_y = ann['bbox'][1]; wid = ann['bbox'][2]; hei = ann['bbox'][3]
            x1 = int(round(float(cent_x-wid/2)))
            y1 = int(round(float(cent_y-hei/2)))
            x2 = int(round(float(cent_x+wid/2)))
            y2 = int(round(float(cent_y+hei/2)))

            annotation_data['bboxes'].append({'class': class_name, 'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2, 'difficult': difficulty})

        all_imgs.append(annotation_data)

    return all_imgs, classes_count, class_mapping