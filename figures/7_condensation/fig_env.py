#!/usr/bin/env python2.5

import Scientific.IO.NetCDF
import sys
import numpy as np
import matplotlib
matplotlib.use("PDF")
import matplotlib.pyplot as plt
sys.path.append("../../tool")
import pmc_data_nc

maximum_ss = np.zeros([4,8])
 
def make_plot(in_dir, in_file_pattern, out_filename, title, max_ss_i, max_ss_j):
    print in_dir, in_file_pattern
    
    env_state_history = pmc_data_nc.read_history(pmc_data_nc.env_state_t, in_dir, in_file_pattern)
    time = [env_state_history[i][0] for i in range(len(env_state_history))]
    rh = [env_state_history[i][1].relative_humidity for i in range(len(env_state_history))]
    temp = [env_state_history[i][1].temperature for i in range(len(env_state_history))]
    
    print title, (max(rh) - 1)*100.
    
    maximum_ss[max_ss_i, max_ss_j] = (max(rh) - 1)*100.

    plt.clf()
    plt.plot(time,rh,'r')
    ax1 = plt.gca()
    ax1.set_ylim(1,1.003)
    ax2 = plt.twinx()
    ax2.plot(time,temp)
    plt.title(title)
    fig = plt.gcf()
    fig.savefig(out_filename)


make_plot("../../new_cond/out_up2","cond_1_0001_.*.nc","figs/env_01.pdf","1 hours", 0, 0)
make_plot("../../new_cond/out_up2","cond_2_0001_.*.nc","figs/env_07.pdf","7 hours", 0, 1)
make_plot("../../new_cond/out_up2","cond_3_0001_.*.nc","figs/env_15.pdf","15 hours", 0, 2)
make_plot("../../new_cond/out_up2","cond_4_0001_.*.nc","figs/env_24.pdf","24 hours", 0, 3)
make_plot("../../new_cond/out_up2","cond_5_0001_.*.nc","figs/env_30.pdf","30 hours", 0, 4)
make_plot("../../new_cond/out_up2","cond_6_0001_.*.nc","figs/env_36.pdf","36 hours", 0, 5)
make_plot("../../new_cond/out_up2","cond_7_0001_.*.nc","figs/env_42.pdf","42 hours", 0, 6)
make_plot("../../new_cond/out_up2","cond_8_0001_.*.nc","figs/env_48.pdf","48 hours", 0, 7)

make_plot("../../new_cond/out_up2_comp","cond_1_0001_.*.nc","figs/env_comp_01.pdf","1 hours", 1, 0)
make_plot("../../new_cond/out_up2_comp","cond_2_0001_.*.nc","figs/env_comp_07.pdf","7 hours", 1, 1)
make_plot("../../new_cond/out_up2_comp","cond_3_0001_.*.nc","figs/env_comp_15.pdf","15 hours", 1, 2)
make_plot("../../new_cond/out_up2_comp","cond_4_0001_.*.nc","figs/env_comp_24.pdf","24 hours", 1, 3)
make_plot("../../new_cond/out_up2_comp","cond_5_0001_.*.nc","figs/env_comp_30.pdf","30 hours", 1, 4)
make_plot("../../new_cond/out_up2_comp","cond_6_0001_.*.nc","figs/env_comp_36.pdf","36 hours", 1, 5)
make_plot("../../new_cond/out_up2_comp","cond_7_0001_.*.nc","figs/env_comp_42.pdf","42 hours", 1, 6)
make_plot("../../new_cond/out_up2_comp","cond_8_0001_.*.nc","figs/env_comp_48.pdf","48 hours", 1, 7)

make_plot("../../new_cond/out_up2_size","cond_1_0001_.*.nc","figs/env_size_01.pdf","1 hours", 2, 0)
make_plot("../../new_cond/out_up2_size","cond_2_0001_.*.nc","figs/env_size_07.pdf","7 hours", 2, 1)
make_plot("../../new_cond/out_up2_size","cond_3_0001_.*.nc","figs/env_size_15.pdf","15 hours", 2, 2)
make_plot("../../new_cond/out_up2_size","cond_4_0001_.*.nc","figs/env_size_24.pdf","24 hours", 2, 3)
make_plot("../../new_cond/out_up2_size","cond_5_0001_.*.nc","figs/env_size_30.pdf","30 hours", 2, 4)
make_plot("../../new_cond/out_up2_size","cond_6_0001_.*.nc","figs/env_size_36.pdf","36 hours", 2, 5)
make_plot("../../new_cond/out_up2_size","cond_7_0001_.*.nc","figs/env_size_42.pdf","42 hours", 2, 6)
make_plot("../../new_cond/out_up2_size","cond_8_0001_.*.nc","figs/env_size_48.pdf","48 hours", 2, 7)

make_plot("../../new_cond/out_up2_both","cond_1_0001_.*.nc","figs/env_both_01.pdf","1 hours", 3, 0)
make_plot("../../new_cond/out_up2_both","cond_2_0001_.*.nc","figs/env_both_07.pdf","7 hours", 3, 1)
make_plot("../../new_cond/out_up2_both","cond_3_0001_.*.nc","figs/env_both_15.pdf","15 hours", 3, 2)
make_plot("../../new_cond/out_up2_both","cond_4_0001_.*.nc","figs/env_both_24.pdf","24 hours", 3, 3)
make_plot("../../new_cond/out_up2_both","cond_5_0001_.*.nc","figs/env_both_30.pdf","30 hours", 3, 4)
make_plot("../../new_cond/out_up2_both","cond_6_0001_.*.nc","figs/env_both_36.pdf","36 hours", 3, 5)
make_plot("../../new_cond/out_up2_both","cond_7_0001_.*.nc","figs/env_both_42.pdf","42 hours", 3, 6)
make_plot("../../new_cond/out_up2_both","cond_8_0001_.*.nc","figs/env_both_48.pdf","48 hours", 3, 7)

np.savetxt("data/maximum_ss.txt", maximum_ss)
