import cv2
import pylab as plt
import glob

# Get all items in folder
def getItems():
    mylist = [f for f in glob.glob("images/*")]
    for f in mylist:
        showInfo(f)

# Plot origianl image and it's histogram
def showInfo(f):
    img = cv2.cvtColor(cv2.imread(f), cv2.COLOR_BGR2RGB)
    f = plt.figure()
    f.add_subplot(1, 2, 1)
    plt.imshow(img)
    f.add_subplot(1, 2, 2)
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()


getItems()



