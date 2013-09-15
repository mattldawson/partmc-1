#!/usr/bin/env python

import sys, os
sys.path.append("../../../tool")
import mpl_helper
import matplotlib
import partmc
import scipy.io, numpy

(figure, axes_array, cbar_axes_array) \
    = mpl_helper.make_fig_array(1,1,figure_width=4,
                                top_margin=0.1, bottom_margin=0.45,
                                left_margin=0.5, right_margin=1,
                                vert_sep=0.2,
                                colorbar="individual",colorbar_location="right",
                                share_y_axes=False)

######## first row ###############
filename = 'out/urban_plume2_process.nc'
ncf = scipy.io.netcdf_file(filename)
time_grid_edges = ncf.variables["time_grid_edges"].data
diversity_edges = ncf.variables["diversity_edges"].data
time_diversity_dist = ncf.variables["time_diversity_dist"].data

time = ncf.variables["time"].data / 3600
avg_part_entropy = numpy.exp(ncf.variables["avg_part_entropy"].data)
entropy_of_avg_part = numpy.exp(ncf.variables["entropy_of_avg_part"].data)
#tot_entropy_ratio = ncf.variables["tot_entropy_ratio"].data
tot_entropy_ratio = (avg_part_entropy-1) / (entropy_of_avg_part-1)
ncf.close()

axes = axes_array[0][0]
cbar_axes = cbar_axes_array[0][0]
p = axes.pcolor(time_grid_edges, diversity_edges, time_diversity_dist.transpose(),
                norm = matplotlib.colors.LogNorm(), linewidths = 0.1)

axes.set_xscale("linear")
axes.set_xlabel(r"time / h")
axes.set_xlim([0,48])
axes.set_xticks([0, 12, 24, 36, 48])

axes.set_yscale("linear")
axes.set_ylabel(r"particle diversity $D_i$")
axes.set_ylim(0, 10.05)

axes.grid(True)

#axes.annotate(r"All Particles", (25,8),
#              verticalalignment="bottom", horizontalalignment="left",
#              bbox = dict(facecolor='white', edgecolor='white'),
#              xytext=(0, 5), textcoords='offset points')

cbar = figure.colorbar(p, cax=cbar_axes, format=matplotlib.ticker.LogFormatterMathtext(),
                       orientation='vertical')
cbar_axes.xaxis.set_label_position('top')
cbar.set_label(r"$n(t, D_i)$ / $\rm m^{-3}$")

######## second row ###############
#filename = 'out/urban_plume2_process_bc.nc'
#ncf = scipy.io.netcdf_file(filename)
#time_grid_edges = ncf.variables["time_grid_edges"].data
#diversity_edges = ncf.variables["diversity_edges"].data
#time_diversity_dist = ncf.variables["time_diversity_dist"].data

#time = ncf.variables["time"].data / 3600
#avg_part_entropy = numpy.exp(ncf.variables["avg_part_entropy"].data)
#entropy_of_avg_part = numpy.exp(ncf.variables["entropy_of_avg_part"].data)
##tot_entropy_ratio = ncf.variables["tot_entropy_ratio"].data
#tot_entropy_ratio = (avg_part_entropy-1) / (entropy_of_avg_part-1)
#ncf.close()

#axes = axes_array[1][0]
#cbar_axes = cbar_axes_array[1][0]
#p = axes.pcolor(time_grid_edges, diversity_edges, time_diversity_dist.transpose(),
#                norm = matplotlib.colors.LogNorm(), linewidths = 0.1)

#axes.set_xscale("linear")
#axes.set_xlim([0,48])
#axes.set_xticks([0, 12, 24, 36, 48])

#axes.set_yscale("linear")
#axes.set_ylabel(r"particle diversity $D_i$")
#axes.set_ylim(0, 10)

#axes.annotate(r"BC-particles only", (25,8),
#              verticalalignment="bottom", horizontalalignment="left",
#              bbox = dict(facecolor='white', edgecolor='white'),
#              xytext=(0, 5), textcoords='offset points')

#axes.grid(True)
#cbar = figure.colorbar(p, cax=cbar_axes, format=matplotlib.ticker.LogFormatterMathtext(),
#                       orientation='vertical')
#cbar_axes.xaxis.set_label_position('top')
#cbar.set_label(r"$n(t, D_i)$ / $\rm m^{-3}$")

mpl_helper.remove_fig_array_axes(axes_array)

out_filename = "urban_plume_poster1.pdf"
figure.savefig(out_filename)
print out_filename