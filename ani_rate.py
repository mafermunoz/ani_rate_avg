import numpy as np
import healpy as hp
import sys
from root_numpy import root2array
from ROOT import TVector3, TMatrixD
from rot import *

def main(nmap,njob,energy_range,year,JOBS=10):
    nmap=int(nmap)##From 1 to 100
    njob=int(njob)##From 1 toJOBS
    JOBS=int(JOBS)## 10
    if(year=='2016'):
        nyear=1
    elif (year=='2017'):
        nyear=2
    elif (year=='2018'):
        nyear=3
    nyear=int(nyear)## from 1 to 3


    if(energy_range=='002_010'):
        energy_bin=1
    elif (energy_range=='010_025'):
        energy_bin=2
    elif (energy_range=='025_050'):
        energy_bin=3

    energy_bin=int(energy_bin)

    ##Load the distribution from where to pull

    poisson_dist=np.load('/beegfs/dampe/users/mmunozsa/pois_dist/pois_dist_year_'+str(nyear)+"_energy_bin"+str(energy_bin)+'_nmap_'+str(nmap)+'.npy')#From  file with the random tracks according to the poisson distribution
    print(len(poisson_dist))
    poisson_dist=np.array_split(poisson_dist,JOBS)

    #sat_pointing=np.load('pointing_history_'+str(year)+'.npy')
    sat_pointing=np.load('/beegfs/dampe/users/mmunozsa/sat_info_2016.npy')

    print(len(sat_pointing))
    sat_pointing=np.array_split(sat_pointing,JOBS)#shuffle the sat pointing
    start=0
    start_track=0
    for i in range(njob-1):
        start=start+len(sat_pointing[i])
        start_track=start_track+poisson_dist[i].sum()
    #end=start+len(poisson_dist[nmap-1][njob-1])
    print(start)
    sat_pointing=sat_pointing[njob-1]
    poisson_dist=poisson_dist[njob-1]
    print(poisson_dist.sum())
    #np.random.shuffle(sat_pointing)
    track=np.load('/beegfs/dampe/users/mmunozsa/ani_tracks_xyz/2016_002_010track_xyz_shuffled_'+str(nmap)+'.npy')
    #track=np.load('/beegfs/dampe/users/mmunozsa/ani_tracks_xyz/2016_data_025_050track_xyz_shuffled_'+str(nmap)+'.npy')
    #track=np.load('/beegfs/dampe/users/mmunozsa/random_maps/tracks_data_'+year+"_"+energy_range+'_shuffled_'+str(nmap-1)+'.npy')

    nTracks=len(track)
    ctrack=start_track
    #ra=np.empty(poisson_dist[start:start+len(sat_pointing)].sum())
    #dec=np.empty(poisson_dist[start:start+len(sat_pointing)].sum())
    cc=0
    ra=np.ones(poisson_dist.sum())
    dec=np.ones(poisson_dist.sum())
    if(nTracks<(len(ra)+start_track)):

        ra=np.ones(nTracks-start_track)
        dec=np.ones(nTracks-start_track)

    ra=ra*-5000
    dec=dec*-5000
    #dec=np.empty(nTracks)
    #ra=np.empty(nTracks)
    #dec=np.empty(nTracks)
    esat=len(sat_pointing)

    for i,x in enumerate (poisson_dist): ##Loop over the elements of the poison distribution
        if(i%100000==0):
            print(i)
        if x==0:
            continue
        for j in range (x):## For each of the tracks that the possion distribution says to us

            if(ctrack<nTracks and i<esat): ## Counter to check we dont repeat tracks
                a=sat_pointing[i]
                #ra[cc],dec[cc],r=thetaphi2radec(np.rad2deg(track[ctrack,0]),np.rad2deg(track[ctrack,1])+180,np.rad2deg(a[0]),np.rad2deg(a[1]))
                r_sat=TVector3(a[2],a[3],a[4])
                v_sat=TVector3(a[5],a[6],a[7])
                r_Track=TVector3(track[ctrack,0],track[ctrack,1],track[ctrack,2])
                ra[cc],dec[cc]=Orb2Equ_RM(r_sat,v_sat,r_Track)
                ctrack=ctrack+1
                cc=cc+1
                a=0

    #ra=np.array(ra)
    #dec=np.array(dec)

    np.savez("../Map_data_"+year+"_"+energy_range+"_"+str(nmap)+"_"+str(njob),ra=ra,dec=dec)




if __name__ == '__main__':
        main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
