# run from inside gnuplot with:
# load "<filename>.gnuplot"
# or from the commandline with:
# gnuplot -persist <filename>.gnuplot

set logscale x
set xlabel "diameter / m"
set ylabel "number concentration / (1/m^3)"

set xrange [1e-9:1e-6]

set key top left

plot "out/parallel_dist_aero_size_num.txt" using 1:2 with lines title "parallel t = 0 h", \
     "out/serial_aero_size_num.txt" using 1:2 with lines title "serial t = 0 h", \
     "out/sect_aero_size_num.txt" using 1:2 with lines title "sect t = 0 h", \
     "out/parallel_dist_aero_size_num.txt" using 1:14 with lines title "parallel t = 12 h", \
     "out/serial_aero_size_num.txt" using 1:14 with lines title "serial t = 12 h", \
     "out/sect_aero_size_num.txt" using 1:14 with lines title "sect t = 12 h", \
     "out/parallel_dist_aero_size_num.txt" using 1:26 with lines title "parallel t = 24 h", \
     "out/serial_aero_size_num.txt" using 1:26 with lines title "serial t = 24 h", \
     "out/sect_aero_size_num.txt" using 1:26 with lines title "sect t = 24 h"
