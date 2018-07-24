import numpy as np
from PIL import Image as Im
import util

class Image(object):
    
    def __init__(self, filename):
        self.filename = filename
        self.img_data = self.__load_img_data()
    
    def __load_img_data(self):
        image = Im.open(self.filename)
        return np.asarray(image, "L")
    
    def __to_img(self):
        return Im.fromarray(self.img_data.astype(dtype=np.uint8), "L")
    
    def reload_img(self):
        self.img_data = self.__load_img_data()
    
    def histogram(self, norm='True'):
        L = 256
        hist = util.histogram(self.img_data, L, norm=norm)
    
        return hist
    
    def histogram2D(self, norm='True'):
        L = 256
        hist2D = util.histogram2D(self.img_data, L, norm=norm)
    
        return hist2D
    
    def show(self):
        self.__to_img().show()
        
if __name__ == '__main__':
    i = Image('Fig1.tif')
    
    w, h = i.img_data.shape
    i.show()
    print(w,h)
    
    hist = i.histogram()
    util.plot_hist(hist, 'a')
    i.show()