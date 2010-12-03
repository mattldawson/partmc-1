#!/bin/bash

# turn on command echoing
set -v
# make sure that the current directory is the one where this script is
cd ${0%/*}

../../extract_aero_species out/average_compsizenum_0001_ out/average_compsizenum_species.txt
../../numeric_diff out/average_species.txt out/average_compsizenum_species.txt 0 0.1 0 0 2 0