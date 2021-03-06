#!/bin/bash

# exit on error
set -e
# turn on command echoing
set -v
# make sure that the current directory is the one where this script is
cd ${0%/*}

../../test_poisson_sample 4 50 10000000 > out/poisson_4_approx.dat
../../test_poisson_sample 4 50 0        > out/poisson_4_exact.dat
../../numeric_diff --by col --rel-tol 2e-3 out/poisson_4_exact.dat out/poisson_4_approx.dat
