import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math

def histogram(imgData, L, norm='True'):
    hist = [0]*L
    rows, cols = imgData.shape
    
    for row in range(rows):
        for col in range(cols):
            r = imgData[row][col]
            hist[r]+=1
    
    if norm:
        for i in range(len(hist)):
            hist[i] = hist[i]/(rows*cols)

    return hist

def histogram2D(imgData, L, norm='True'):
    #TODO add borders
    n = 3
    imgData = add_borders(imgData, n)
    hist2D = [[0]*L]*L
    rows, cols = imgData.shape
    
    for row in range(rows):
        for col in range(cols):
            #get r and get average r from neighbors 3x3
            r = imgData[row][col]
            
            #window = imgData[row:row+n,col:col+n]
            
            
            hist[r]+=1
    
    if norm:
        for i in range(len(hist)):
            hist[i] = hist[i]/(w*h)

    return hist2D

def add_borders(imgData, n):
    shape = imgData.shape
    
    rows = np.zeros((n, shape[1]), dtype=np.uint8)
    data = np.insert(imgData, 0, rows, 0)
    data = np.insert(data, data.shape[0], rows, 0)
    
    cols = np.zeros((n, data.shape[0]), dtype=np.uint8)
    data = np.insert(data, 0, cols, 1)
    data = np.insert(data, data.shape[1], cols, 1)

    return data

#########

def show(imgData):
    img = data_to_img(imgData)
    img.show()

def load_img(imgName):
    img = Image.open(imgName)
    
    return img

def load_img_data(img):
    imgData = np.asarray(img, "L")
    
    return imgData

def data_to_img(imgData, L=256):
    img = Image.fromarray(imgData.astype(dtype=np.uint8), "L")
    
    return img

def img_mean(imgData):
    w, h = imgData.shape
    
    s = 0
    for x in range(w):
        for y in range(h):
             r = imgData[x][y]
             s+=r
    
    return s/(w*h)

def img_std(imgData):
    w, h = imgData.shape
    mean = img_mean(imgData)
    
    s = 0
    for x in range(w):
        for y in range(h):
            r = imgData[x][y]
            s+=(r-mean)**2
        
    return math.sqrt(s/(w*h))

def fit(value, L=256):
    if value > L-1:
        return L-1
    elif value < 0:
        return 0
    else:
        return value
    
def plot_hist(hist, name):
    plt.bar(range(len(hist)), hist)
    fig = plt.gcf()
    plt.show()
    plt.draw()
    fig.savefig(name+".png")

def normalize(imgData, L=256):
    shape = imgData.shape
    w, h = shape
    new_imgData = np.zeros(shape, dtype=np.uint8)
    
    min_value, max_value = imgData.min(), imgData.max()
    
    for x in range(w):
        for y in range(h):
            fm = imgData[x][y] - min_value
            new_value = round((L-1)*fm/(max_value-min_value))
            
            new_imgData[x][y] = int(new_value)
            
    return new_imgData

def add_img_data(imgs, c):
    imgShape = imgs[0].shape
    
    if imgs[1].shape != imgShape:
        raise Exception("Images aren't the same size")
    
    imgData0 = imgs[0]
    imgData1 = imgs[1] 
    
    w, h = imgShape
    new_imgData = np.zeros(imgShape)
    fit_imgData = np.zeros(imgShape, dtype=np.uint8)
    
    for x in range(w):
        for y in range(h):
            new_value = imgData0[x][y] + c * imgData1[x][y]
            new_imgData[x][y] = new_value
            fit_imgData[x][y] = fit(new_value)
    
    return new_imgData, data_to_img(fit_imgData)

def add_borders(imgData, n):
    shape = imgData.shape
    
    rows = np.zeros((n, shape[1]), dtype=np.uint8)
    data = np.insert(imgData, 0, rows, 0)
    data = np.insert(data, data.shape[0], rows, 0)
    
    cols = np.zeros((n, data.shape[0]), dtype=np.uint8)
    data = np.insert(data, 0, cols, 1)
    data = np.insert(data, data.shape[1], cols, 1)

    return data
