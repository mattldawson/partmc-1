#!/usr/bin/env python

import sys, os
sys.path.append("../../../tool")
import mpl_helper
import matplotlib
import partmc
import scipy.io, numpy as np

(figure, axes_array) \
    = mpl_helper.make_fig_array(1,1,figure_width=4,
                                top_margin=0.1, bottom_margin=0.45,
                                left_margin=0.5, right_margin=1,
                                vert_sep=0.2,
                                share_y_axes=False)

######## first row ###############
filename = 'out/urban_plume2_process.nc'
ncf = scipy.io.netcdf_file(filename)

time = ncf.variables["time"].data / 3600
avg_part_entropy = np.exp(ncf.variables["avg_part_entropy"].data)
entropy_of_avg_part = np.exp(ncf.variables["entropy_of_avg_part"].data)
#tot_entropy_ratio = ncf.variables["tot_entropy_ratio"].data
tot_entropy_ratio = (avg_part_entropy-1) / (entropy_of_avg_part-1)
ncf.close()

axes = axes_array[0][0]
axes.plot(time, avg_part_entropy, "b-")
axes.plot(time, entropy_of_avg_part, "k--")

axes.set_ylabel(r"$D_{\alpha}, D{\gamma}$")
axes.set_ylim([0,10])

axes2 =  axes.twinx()
axes2.plot(time, tot_entropy_ratio, "r-", markersize = 2)
axes2.set_ylabel(r"$\chi$")
axes2.set_ylim([0,1])
#axes2.set_yticks([0,0.2,0.4,0.6,0.8, 1])

axes2.set_xscale("linear")
axes2.set_xlabel(r"time / h")
axes2.set_xlim([0,48])
axes2.set_xticks([0, 12, 24, 36, 48])

print "coordinates "
print time[78], avg_part_entropy[78]
print time[66], entropy_of_avg_part[66]
print time[102], tot_entropy_ratio[102]

axes.annotate(r"$D_{\alpha}$", (20,1.5),
              verticalalignment="bottom", horizontalalignment="right",
              bbox = dict(facecolor='white', edgecolor='white'),
              xytext=(0, 5), textcoords='offset points')
axes.annotate(r"$D_{\gamma}$", (3,1.8),
              verticalalignment="bottom", horizontalalignment="right",
              bbox = dict(facecolor='white', edgecolor='white'),
              xytext=(0, 5), textcoords='offset points')
axes.annotate(r"$\chi$", (10,1.7),
              verticalalignment="bottom", horizontalalignment="right",
              bbox = dict(facecolor='white', edgecolor='white'),
              xytext=(0, 5), textcoords='offset points')

#axes.annotate(r"All Particles", (25,8),
#              verticalalignment="bottom", horizontalalignment="left",
#              bbox = dict(facecolor='white', edgecolor='white'),
#              xytext=(0, 5), textcoords='offset points')

axes.grid(True)

######## second row ###############
#filename = 'out/urban_plume2_process_bc.nc'
#ncf = scipy.io.netcdf_file(filename)

#time = ncf.variables["time"].data / 3600
#avg_part_entropy = np.exp(ncf.variables["avg_part_entropy"].data)
#entropy_of_avg_part = np.exp(ncf.variables["entropy_of_avg_part"].data)
##tot_entropy_ratio = ncf.variables["tot_entropy_ratio"].data
#tot_entropy_ratio = (avg_part_entropy-1) / (entropy_of_avg_part-1)
#ncf.close()

#axes = axes_array[1][0]
#axes.plot(time, avg_part_entropy, "b-")
#axes.plot(time, entropy_of_avg_part, "k--")
#axes.set_ylabel(r"$D_{\alpha}, D{\gamma}$")
#axes.set_ylim([0,10.0])

#axes2 =  axes.twinx()
#axes2.plot(time, tot_entropy_ratio, "r-", markersize = 2)
#axes2.set_ylabel(r"$\chi$")
#axes2.set_ylim([0,1])
#axes2.set_xscale("linear")
#axes2.set_xlim([0,48])
#axes2.set_xticks([0, 12, 24, 36, 48])


#axes.annotate(r"$D_{\alpha}$", (time[78], avg_part_entropy[78]),
#              verticalalignment="bottom", horizontalalignment="right",
#              bbox = dict(facecolor='white', edgecolor='white'),
#              xytext=(0, 5), textcoords='offset points')
#axes.annotate(r"$D_{\gamma}$", (time[66], entropy_of_avg_part[66]),
#              verticalalignment="bottom", horizontalalignment="right",
#              bbox = dict(facecolor='white', edgecolor='white'),
#              xytext=(0, 5), textcoords='offset points')
#axes.annotate(r"$\chi$", (20,1.15),
#              verticalalignment="bottom", horizontalalignment="right",
#              bbox = dict(facecolor='white', edgecolor='white'),
#              xytext=(0, 5), textcoords='offset points')

#axes.annotate(r"BC-particles only", (25,8),
#              verticalalignment="bottom", horizontalalignment="left",
#              bbox = dict(facecolor='white', edgecolor='white'),
#              xytext=(0, 5), textcoords='offset points')
#axes.grid(True)

#mpl_helper.remove_fig_array_axes(axes_array)

out_filename = "urban_plume_poster2.pdf"
figure.savefig(out_filename)
print out_filename