from numpy import *

randMat = mat(random.rand(4,4))
print randMat
invRandMat = randMat.I
print invRandMat
myEye = randMat*invRandMat
print myEye
eyeDiff = myEye - eye(4)
print eyeDiff