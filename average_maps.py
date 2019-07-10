import healpy
import numpy as np
import sys
import glob



def main(energy_range,year):
    file_path="../Map_full_hitmap_"+year+"_"+energy_range+"_*"
    txt=glob.glob(file_path)
    print(len(txt))
    for i,file  in enumerate (txt):
        if i==0:
            f=np.load(file)
        else:
            dummy=np.load(file)
            f=f+dummy

    f=f/(len(txt))


    np.save("../Map_hitmap_"+year+"_"+energy_range,f)

if __name__ == '__main__':
        main(sys.argv[1],sys.argv[2])
