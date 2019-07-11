import healpy
import numpy as np
import sys
import glob



def main(nmap,energy_range,year):
    file_path="../Map_data_new_"+year+"_"+energy_range+"_"+str(nmap)+"_*"
    txt=glob.glob(file_path)
    print(txt)
    for i,file  in enumerate (txt):
        if i==0:
            f=np.load(file)
            ra=f['ra']
            dec=f['dec']
        else:
            dummy=np.load(file)
            ra=np.hstack([ra,dummy['ra']])
            dec=np.hstack([dec,dummy['dec']])

    #if(year=='2016'):
    #    nyear=1
    #elif (year=='2017'):
    #    nyear=2
    #elif (year=='2018'):
    #    nyear=3
    #nyear=int(nyear)## from 1 to 3


    #if(energy_range=='002_010'):
    #    energy_bin=1
    #elif (energy_range=='010_025'):
    #    energy_bin=2
    #elif (energy_range=='025_050'):
    #    energy_bin=3
    #events_per_year=np.load('rate_ps_year_energybin.npy')
    #x=events_per_year[nyear-1,energy_bin-1]
    #data=np.stack((ra,dec),axis=1)

    data = {"L":ra, "B":dec}

    NSIDE = 32
    pixels= healpy.ang2pix(NSIDE,data['L'], data['B'])
    hitmap= np.zeros(healpy.nside2npix(NSIDE)) * healpy.UNSEEN
    pixels_binned=0
    pixels_binned =np.bincount(pixels)
    hitmap[:len(pixels_binned)] =  pixels_binned

    # data = {"L":ra[:], "B":dec[:]}
    # print(len(ra))
    # NSIDE = 32
    # pixels= healpy.ang2pix(NSIDE, np.deg2rad(90)-data['B'],data['L'])
    # hitmap= np.zeros(healpy.nside2npix(NSIDE)) * healpy.UNSEEN
    # pixels_binned=0
    # pixels_binned =np.bincount(pixels)
    # hitmap[:len(pixels_binned)] =  pixels_binned

    np.save("../Map_full_hitmap_"+year+"_"+energy_range+"_"+str(nmap),hitmap)

if __name__ == '__main__':
        main(sys.argv[1],sys.argv[2],sys.argv[3])
