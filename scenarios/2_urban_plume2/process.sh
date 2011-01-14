#!/bin/sh

# exit on error
set -e
# turn on command echoing
set -v

# The data should have already been generated by ./run.sh

../../build/extract_env out/urban_plume2_wc_0001_ out/urban_plume2_wc_env.txt
../../build/extract_gas out/urban_plume2_wc_0001_ out/urban_plume2_wc_gas.txt
../../build/extract_aero_total out/urban_plume2_wc_0001_ out/urban_plume2_wc_aero_total.txt
../../build/extract_aero_species out/urban_plume2_wc_0001_ out/urban_plume2_wc_aero_species.txt
../../build/extract_aero_size_num 1e-9 1e-6 100 out/urban_plume2_wc_0001_ out/urban_plume2_wc_aero_size_num.txt
../../build/extract_aero_size_mass 1e-9 1e-6 100 out/urban_plume2_wc_0001_ out/urban_plume2_wc_aero_size_mass.txt

../../build/extract_aero_particle_mass out/urban_plume2_wc_0001_00000001.nc out/urban_plume2_wc_aero_particle_mass_00000001.txt
../../build/extract_aero_particle_mass out/urban_plume2_wc_0001_00000006.nc out/urban_plume2_wc_aero_particle_mass_00000006.txt
../../build/extract_aero_particle_mass out/urban_plume2_wc_0001_00000008.nc out/urban_plume2_wc_aero_particle_mass_00000008.txt
../../build/extract_aero_particle_mass out/urban_plume2_wc_0001_00000025.nc out/urban_plume2_wc_aero_particle_mass_00000025.txt

../../build/extract_env out/urban_plume2_nc_0001_ out/urban_plume2_nc_env.txt
../../build/extract_gas out/urban_plume2_nc_0001_ out/urban_plume2_nc_gas.txt
../../build/extract_aero_total out/urban_plume2_nc_0001_ out/urban_plume2_nc_aero_total.txt
../../build/extract_aero_species out/urban_plume2_nc_0001_ out/urban_plume2_nc_aero_species.txt
../../build/extract_aero_size_num 1e-9 1e-6 100 out/urban_plume2_nc_0001_ out/urban_plume2_nc_aero_size_num.txt
../../build/extract_aero_size_mass 1e-9 1e-6 100 out/urban_plume2_nc_0001_ out/urban_plume2_nc_aero_size_mass.txt

../../build/extract_aero_particle_mass out/urban_plume2_nc_0001_00000001.nc out/urban_plume2_nc_aero_particle_mass_00000001.txt
../../build/extract_aero_particle_mass out/urban_plume2_nc_0001_00000006.nc out/urban_plume2_nc_aero_particle_mass_00000006.txt
../../build/extract_aero_particle_mass out/urban_plume2_nc_0001_00000008.nc out/urban_plume2_nc_aero_particle_mass_00000008.txt
../../build/extract_aero_particle_mass out/urban_plume2_nc_0001_00000025.nc out/urban_plume2_nc_aero_particle_mass_00000025.txt

# Now run 'gnuplot -persist <filename>.gnuplot' to plot the data
