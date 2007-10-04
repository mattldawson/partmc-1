#!/bin/sh

cat <<ENDINFO

Sedimentation Bidisperse Test-case
----------------------------------

Starting from many small particles and one large particle, we simulate
with the Monte Carlo code. For this case, we can write an ODE in one
variable (either number of small particles or volume of large
particle), which we solve as a comparison.

The output plots show both small-particle number and large-particle
volume. We disable doubling to avoid generating multiple large
particles, which would result in large-large coagulations and so the
ODE would no longer be valid. While this means that the simulation is
not all that interesting physically, it is an interesting test-case
that sectional codes cannot do well. The lack of resolution towards
the end of the Monte Carlo simulation is expected.

ENDINFO
sleep 1

echo ../src/partmc sedi_bidisperse_mc.spec
../src/partmc sedi_bidisperse_mc.spec
echo ./sedi_bidisperse_ode
./sedi_bidisperse_ode

echo ./sedi_bidisperse_plot.py
./sedi_bidisperse_plot.py
echo "Now view out/sedi_bidisperse_*.pdf"
