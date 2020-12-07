import numpy as np
import glob
import os
import cv2
import pandas as pd

def color_moments(pic):
    pic=np.double(pic)
    R=pic[:,:,0]
    G=pic[:,:,1]
    B=pic[:,:,2]
    colorFeature=[np.mean(R[:]),np.std(R[:]),np.mean(G[:]),np.std(G[:]),np.mean(B[:]),np.std(B[:])];
    colorFeature=colorFeature/np.mean(colorFeature)
    return colorFeature

def gatFeatures(pic,fsize):
    features=np.zeros((fsize,1))
    features=color_moments(pic)
    features = [features, hsvHistogramFeatures(pic)];
    #features = [features, textureFeatures(pic)];
    #features = [features, shapeFeatures(pic)];
    return features
def createFeatures(fold):
    etat=dict()
    features=dict()
    list=os.listdir(fold)
    id=1
    for i in range(len(list)):
        if os.path.abspath(list[i]):
            file=os.path.relpath(list[i])
            for pic in glob.glob('DB2C\\'+file+'\\*.jpg'):
                etat[file]=id
                picture=cv2.imread(pic)
                features[id]=gatFeatures(picture,50)
            id=id+1
                
if __name__ == '__main__':
    
    createFeatures('DB2C')
    