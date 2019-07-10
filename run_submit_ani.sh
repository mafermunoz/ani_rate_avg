for l in '2016'
do
  for k in '025_050'
  do
    for i in {1..100}
    do
      for j in {1..10}
      do
        OUTF="../Map_data_cc_try4_"$l'_'$k'_'$i'_'$j'.npz'
        if [ ! -f ${OUTF} ]; then
          echo  $i $j $k $l
          echo $OUTF
          sbatch submit_ani.sh  $i $j $k $l
        fi
      done
    done
  done
done
