import os, random, shutil

def renew(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        os.makedirs(path)
    else:
        os.makedirs(path)
    
    return


def makesample(fileDir,picknumber):
    folderDir = os.listdir(fileDir)    #取每一类的文件夹的原始路径
    sample = []
    for folder in folderDir:
        pathDir = os.listdir(fileDir+folder)
        #picknumber=1100 #从每个文件夹中取一定数量图片
        sample.append(random.sample(pathDir, picknumber))  #随机选取picknumber数量的样本图片
    return(sample)

def maketrain(fileDir,liDir,sample):
    folderlist = os.listdir(fileDir)
    for i in range(12):
        #renew(liDir+folderlist[i])
        a = sample[i]
        for name in a[0:1000]:
            shutil.copy(fileDir+folderlist[i]+'/'+name, liDir+'/'+name)
           
    return

def makelinear(fileDir,liDir,sample):
    folderlist = os.listdir(fileDir)
    for i in range(12):
        os.makedirs(liDir+'train/'+folderlist[i])
        os.makedirs(liDir+'val/'+folderlist[i])
        a = sample[i]
        for name in a[1000:1100]:
            shutil.copy(fileDir+folderlist[i]+'/'+name, liDir+'train/'+folderlist[i]+'/'+name)
        for name in a[1000:1200]:
            shutil.copy(fileDir+folderlist[i]+'/'+name, liDir+'val/'+folderlist[i]+'/'+name)
           
    return

 
if __name__ == '__main__':
    fileDir = "/home/jinjin/taskcv-2017-public/reshape/validation/"  #源图片文件夹路径
    tarDir = './train/'
    tarDir1 = './linear/'
    renew(tarDir)
    renew(tarDir1)

    sam= makesample(fileDir,1200)
    maketrain(fileDir,tarDir,sam)
    makelinear(fileDir,tarDir1,sam)
    print(len(sam[0]))

    '''
    fileDir = "/home/jinjin/taskcv-2017-public/reshape/validation/"  #源图片文件夹路径
    tarDir = './linear/'
    renew(tarDir)
    sam= makesample(fileDir,200)
    makelinear(fileDir,tarDir,sam)
    '''



  