for f in $( ls ./in );
do
python $1 < in/${f} > out/${f}
./vis.exe in/${f} out/${f}
done