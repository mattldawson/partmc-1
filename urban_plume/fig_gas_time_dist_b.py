#!/usr/bin/env python
# Copyright (C) 2007, 2008 Matthew West
# Licensed under the GNU General Public License version 2 or (at your
# option) any later version. See the file COPYING for details.

import os, sys
import copy as module_copy
from Scientific.IO.NetCDF import *
from pyx import *
sys.path.append("../tool")
from pmc_data_nc import *
from pmc_pyx import *

#gas_species = ["C2H6", "HCHO", "ANOL", "TOL", "ETH", "ISOP"]
gas_species = ["HNO3", "SO2", "NH3"]
#line_style_order = [4, 5, 0, 1, 2, 3]

data = pmc_var(NetCDFFile("out/urban_plume_with_coag_0001.nc"),
	       "gas",
	       [])

#data.write_summary(sys.stdout)

data.scale_dim("time", 1.0/60)
g = graph.graphxy(
    width = 6.5,
    x = graph.axis.linear(min = 0.,
                          max = 1440,
#                          parter = graph.axis.parter.linear(tickdists = [6, 3]),
#                          max = max(data.dim_by_name("time").grid_centers),
                          parter = graph.axis.parter.linear(tickdists
                                                            = [6 * 60, 3 * 60]),
                          texter = time_of_day(base_time = 6 * 60),
                          title = "local standard time",
			  painter = grid_painter),
    y = graph.axis.linear(min = 0.,
                          max = 20,
                          title = "gas concentration (ppb)",
			  painter = grid_painter))
#    key = graph.key.key(pos = "tr"))
#    key = graph.key.key(pos = None, hpos = 0.7, vpos = 0.8))

for i in range(len(gas_species)):
    data_slice = module_copy.deepcopy(data)
    data_slice.reduce([select("gas_species", gas_species[i])])
#    data_slice.scale_dim("time", 1.0/3600)
    g.plot(graph.data.points(data_slice.data_center_list(),
			   x = 1, y = 2,
			   title = tex_species(gas_species[i])),
	   styles = [graph.style.line(lineattrs = [line_style_list[i], style.linewidth.Thick])])
g.text(1.5,3.1,r"$\rm HNO_3$",[text.halign.boxleft,text.valign.bottom,color.rgb(0,0,0)])
g.text(2.2,2,r"$\rm SO_2$",[text.halign.boxleft,text.valign.bottom,color.rgb(0,0,0)])
g.text(2.4,0.7,r"$\rm NH_3$",[text.halign.boxleft,text.valign.bottom,color.rgb(0,0,0)])

g.writePDFfile("figs/gas_time_dist_b.pdf")
print "figure height = %.1f cm" % unit.tocm(g.bbox().height())
print "figure width = %.1f cm" % unit.tocm(g.bbox().width())
