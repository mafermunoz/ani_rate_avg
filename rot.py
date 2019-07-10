from root_numpy import root2array
from ROOT import TVector3, TMatrixD
import numpy as np


def Orb2Equ_RM(r_sat, v_sat, r_Track):

    #The Direction of Incident Particle is the Inverse Direction of the Track Reconstructed
    r_Particle = -r_Track

    #Calculate the Matrix for Coordinate Transformation Using Satellite Position and Velocity
    T= np.zeros([3,3])

    Z_sat = -r_sat.Unit() #Z_sat is in the Inverse Direction of Satellite Position
    Y_sat =  v_sat.Cross(r_sat).Unit()#; //Y_sat is in the Inverse Direction of Orbit Normal
    X_sat =  Y_sat.Cross(Z_sat).Unit()#; //X = Y Cross Z
    #print (X_sat)
    #//The Row Vectors of the Rotation Matrix are X_sat, Y_sat, and Z_sat
    T[0][0] = X_sat.X()
    T[1][0] = X_sat.Y()
    T[2][0] = X_sat.Z()

    T[0][1] = Y_sat.X()
    T[1][1] = Y_sat.Y()
    T[2][1] = Y_sat.Z()

    T[0][2] = Z_sat.X()
    T[1][2] = Z_sat.Y()
    T[2][2] = Z_sat.Z()

    #//Transform from Orbit Coord to Equatorial Coord by Applying the Rotation Matrix
    #pp=np.array(3)
    #print(r_Particle)
    #pp=np.array([0,0,1])
    aa=np.dot(T, r_Particle)
    bb=TVector3(aa[0],aa[1],aa[2])

    return bb.Theta(),bb.Phi()
#b=np.loadtxt('try_rot')
#print(b.shape)
#for i in range (len(b)):
    # a=b[i]
    # r_sat=TVector3(a[2],a[3],a[4])
    # v_sat=TVector3(a[5],a[6],a[7])
    # r_Track=TVector3(0,0,1)
    #
    # dd=Orb2Equ_RM(r_sat,v_sat,r_Track)
    # print (dd.Theta(),dd.Phi())
