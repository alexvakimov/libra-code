import os
import sys
import math

# Fisrt, we add the location of the library to test to the PYTHON path
cwd = os.getcwd()
print "Current working directory", cwd
sys.path.insert(1,cwd+"/../../_build/src/mmath")
sys.path.insert(1,cwd+"/../../_build/src/qchem")


print "\nTest 1: Importing the library and its content"
from cygmmath import *
from cygqchem import *


t = Timer()
t.start()
print "\nTest 2: 3D overlaps: normalized"
f = open("3D_overlaps_norm.txt","w")
Ra = VECTOR(0.0, 0.0, 0.0)
Rb = VECTOR(0.0, 0.0, 0.0)
u = VECTOR(1.0, 2.0, -0.5)
u.normalize()
print "u (normalized) = ", u.x, u.y, u.z


for i in range(0,50):
    x = 0.1 * i
    Rb = Ra + x*u    

    ss  = gaussian_overlap(0,0,0, 1.3, Ra,  0,0,0, 1.3, Rb )  # s(H)-s(H)
    spx = gaussian_overlap(0,0,0, 1.3, Ra,  1,0,0, 1.3, Rb )  # s(H)-px(H)
    spy = gaussian_overlap(0,0,0, 1.3, Ra,  0,1,0, 1.3, Rb )  # s(H)-py(H)
    spz = gaussian_overlap(0,0,0, 1.3, Ra,  0,0,1, 1.3, Rb )  # s(H)-pz(H)
    pxpx = gaussian_overlap(1,0,0, 1.3, Ra,  1,0,0, 1.3, Rb )  # px(H)-px(H) 
    pxpy = gaussian_overlap(1,0,0, 1.3, Ra,  0,1,0, 1.3, Rb )  # px(H)-py(H) = 0
    pypz = gaussian_overlap(0,1,0, 1.3, Ra,  0,0,1, 1.3, Rb )  # py(H)-pz(H) = 0
    sdz2 = gaussian_overlap(0,0,0, 1.3, Ra,  0,0,2, 1.3, Rb )  # s(H)-dz2(H) 
    sdxy = gaussian_overlap(0,0,0, 1.3, Ra,  0,1,1, 1.3, Rb )  # s(H)-dxy(H) 
    pxdxy = gaussian_overlap(1,0,0, 1.3, Ra,  0,1,1, 1.3, Rb )  # s(H)-dxy(H) 

    f.write("%8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f \n" % (x, ss, spx, spy, spz, pxpx, pxpy, pypz, sdz2, sdxy, pxdxy) )


f.close()

t.stop()
print "Time to compute = ", t.show(), " sec"



