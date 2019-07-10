for l in '2016'
do
  for k in {'002_010','010_025','025_050'}
  do
        OUTF="../Map_hitmap_"$l'_'$k'.npy'
        if [ ! -f ${OUTF} ]; then
          echo  $k $l
          echo $OUTF
          python average_maps.py   $k $l
        fi
  done
done
