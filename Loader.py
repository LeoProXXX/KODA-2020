import os
import glob
import cv2
import numpy as np

from PIL import Image
from Utils import get_concat_h
from matplotlib import pyplot as plt
from scipy.stats import entropy as scipy_entropy

class Loader:
    def __init__(self, natural_images_dir, 
                 artificial_images_dir):

        self.natural_images = glob.glob(natural_images_dir + "/*.pgm", recursive=True)
        self.artificial_images = glob.glob(artificial_images_dir + "/*.pgm", recursive=True)
        
    def generateHistograms(self):
        for path in self.natural_images:
            self.generateHistogram(path)
        for path in self.artificial_images:
            self.generateHistogram(path)
            
    def generateHistogram(self, path):
        image = Image.open(path)
        histr = image.histogram()
        histr_file_name = path.replace(".pgm", "_hist.png")
        
        plt.figure()
        plt.plot(histr)
        plt.xlim([0,256])
        plt.savefig(histr_file_name)
        plt.close()
        
    def getNaturalImages(self):
        images = []
        for path in self.natural_images:
            images.append(Image.open(path))
        return images
    
    def getArtificialImages(self):
        images = []
        for path in self.artificial_images:
            images.append(Image.open(path))
        return images
    
    def entropy(self, img, base=2): # 2 stands for Shannon entropy
        image = np.asarray(img)
        _, counts = np.unique(image, return_counts=True)
        return scipy_entropy(counts, base=base)

if __name__ == "__main__":
    loader = Loader(natural_images_dir="data/obrazy", 
                    artificial_images_dir="data/rozklady")
    loader.generateHistograms()
    for img in loader.getArtificialImages():
        print(loader.entropy(img))