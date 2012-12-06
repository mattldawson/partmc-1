
# run from inside gnuplot with:
# load "<filename>.gnuplot"
# or from the commandline with:
# gnuplot -persist <filename>.gnuplot

set logscale x
set xlabel "dimensionless volume"
set ylabel "dimensionless number concentration"

set xrange [1e-3:10]
set yrange [0:1.5]

plot "out/part_naumann_cont_df_1_8_0001_self_preserve.txt" using 1:2 title "Df = 1.8, PartMC", \
     "ref_cont_df_1_8_self_preserve_regrid.txt" using 1:2 with lines title "Df = 1.8, Ref"