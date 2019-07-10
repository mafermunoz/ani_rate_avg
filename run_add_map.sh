for l in '2016'
do
  for k in {'002_010','010_025','025_050'}
  do
    for i in {1..100}
    do
        OUTF="../Map_full_hitmap_"$l'_'$k'_'$i'.npy'
        if [ ! -f ${OUTF} ]; then
          echo  $i $k $l
          echo $OUTF
          sbatch submit_add_maps.sh  $i $k $l
        fi
    done
  done
done
