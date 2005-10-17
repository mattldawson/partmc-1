C Simulation with Golovin kernel and fixed timestepping.

CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

      program MonteCarlo
 
      integer MM, n_bin, n_loop, scal
      real*8 t_max, del_t, rho_p, N_0, p_max, V_0, t_print
      parameter (MM = 10000)       ! number of particles
      parameter (n_bin = 160)      ! number of bins
      parameter (n_loop = 1)       ! number of loops
      parameter (scal = 3)         ! scale factor for bins
      parameter (t_max = 600d0)    ! total simulation time (seconds)
      parameter (del_t = 1d0)      ! timestep (seconds)
      parameter (rho_p = 1000d0)   ! particle density (kg m^{-3})
      parameter (N_0 = 1d9)        ! particle number concentration (#/m^3)
      parameter (p_max = 0.01d0)   ! maximum coagulation probability
      parameter (V_0 = 4.1886d-15) ! mean volume of initial distribution
      parameter (t_print = 60)     ! interval between printing (s)

      integer M, i_loop, k
      real*8 V(MM), V_comp, dlnr
      real*8 n_ini(n_bin), bin_v(n_bin), bin_r(n_bin)
      real*8 bin_g(n_bin), bin_n(n_bin)

      real*8 pi
      parameter (pi = 3.14159265358979323846d0)

      external kernel_golovin

      open(30,file='out_golovin_fix.d')
      call print_header(n_loop, n_bin, nint(t_max / t_print) + 1)
      call srand(10)

      do i_loop = 1,1

         call make_grid(n_bin, scal, rho_p, bin_v, bin_r, dlnr)
         
         ! define initial exponential distribution
         do k = 1,n_bin
            n_ini(k) = pi/2d0 * (2d0*bin_r(k))**3 * MM/V_0
     &           * exp(-(bin_v(k) / V_0))
         enddo

         call compute_volumes(n_bin, MM, n_ini, bin_r, dlnr, V, M)
         V_comp = M / N_0

         call mc_fix(MM, M, V, V_comp, kernel_golovin, n_bin,
     &        bin_v, bin_r, g, bin_n, dlnr, t_max, del_t, p_max, t_print,
     &        i_loop)

      enddo

      end

CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
