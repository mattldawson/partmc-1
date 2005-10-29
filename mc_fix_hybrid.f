C     Monte Carlo with fixed timestep and a hybrid array.

CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

      subroutine mc_fix_hybrid(MM, M, V, n_bin, MH, VH, V_comp, bin_v,
     $     bin_r, bin_g, bin_n, dlnr, kernel, t_max, t_print, t_progress
     $     , del_t, loop)

      integer MM           ! INPUT: physical dimension of V
      integer M            ! INPUT/OUTPUT: logical dimension of V
      real*8 V(MM)         ! INPUT/OUTPUT: particle volumes (m^3)
      integer n_bin        ! INPUT: number of bins
      integer MH(n_bin)    ! OUTPUT: number of particles per bin
      real*8 VH(n_bin,MM)  ! OUTPUT: particle volumes
      real*8 V_comp        ! INPUT/OUTPUT: computational volume (m^3)

      real*8 bin_v(n_bin)  ! INPUT: volume of particles in bins (m^3)
      real*8 bin_r(n_bin)  ! INPUT: radius of particles in bins (m)
      real*8 bin_g(n_bin)  ! OUTPUT: mass in bins               
      integer bin_n(n_bin) ! OUTPUT: number in bins
      real*8 dlnr          ! INPUT: bin scale factor

      external kernel      ! INPUT: kernel function
      real*8 t_max         ! INPUT: final time (seconds)
      real*8 t_print       ! INPUT: interval to output data (seconds)
      real*8 t_progress    ! INPUT: interval to print progress (seconds)
      real*8 del_t         ! INPUT: timestep
      integer loop         ! INPUT: loop number of run

      real*8 time, last_print_time, last_progress_time
      real*8 k_max(n_bin, n_bin), n_samp_real
      integer n_samp, i_samp, n_coag, i, j, tot_n_samp, tot_n_coag
      logical do_print, do_progress, did_coag, bin_change
      real*8 t_start, t_end, t_est

c      write(*,*)'start of mc_fix_hybrid'

      last_progress_time = 0d0
      time = 0d0
      tot_n_coag = 0
      call moments(MM, M, V, V_comp, n_bin, bin_v, bin_r, bin_g, bin_n,
     $     dlnr)
c      write(*,*)'done moments'
      call check_event(time, t_print, last_print_time, do_print)
      if (do_print) call print_info(time, V_comp, n_bin, bin_v, bin_r,
     $     bin_g, bin_n, dlnr)
      call array_to_hybrid(MM, M, V, n_bin, bin_v, MH, VH)
c      write(*,*)'done array_to_hybrid'
      call est_k_max_binned(n_bin, bin_v, kernel, k_max)
c      write(*,*)'done k_max_binned'

      call cpu_time(t_start)
      do while (time < t_max)
c         write(*,*)'main loop time = ', time
         tot_n_samp = 0
         n_coag = 0
         do i = 1,n_bin
            do j = 1,n_bin
               ! FIXME: are we handling i == j correctly?
c               write(*,*)'i,j = ', i, j
               call compute_n_samp_hybrid(n_bin, MH, i, j, V_comp,
     $              k_max, del_t, n_samp_real)
c               write(*,*)'n_samp_real = ', n_samp_real
               ! probabalistically determine n_samp to cope with < 1 case
               n_samp = int(n_samp_real)
               if (dble(rand()) .lt. mod(n_samp_real, 1d0)) then
                  n_samp = n_samp + 1
               endif
               tot_n_samp = tot_n_samp + n_samp
               do i_samp = 1,n_samp
                  call maybe_coag_pair_hybrid(MM, M, n_bin, MH, VH,
     $                 V_comp, bin_v, bin_r, bin_g, bin_n, dlnr, i, j,
     $                 del_t, k_max(i,j), kernel, did_coag, bin_change)
                  if (did_coag) n_coag = n_coag + 1
               enddo
c               write(*,*)'did samples'
            enddo
         enddo
         tot_n_coag = tot_n_coag + n_coag
         if (M .lt. MM / 2) then
            call double_hybrid(MM, M, n_bin, MH, VH, V_comp, bin_v,
     $           bin_r, bin_g, bin_n, dlnr)
         endif

c         write(*,*)'about to check_hybrid()'
! DEBUG
         call check_hybrid(MM, M, n_bin, MH, VH, bin_v, bin_r)
! DEBUG

         time = time + del_t

         call check_event(time, t_print, last_print_time, do_print)
         if (do_print) call print_info(time, V_comp, n_bin, bin_v, bin_r
     $        , bin_g, bin_n, dlnr)

         call check_event(time, t_progress, last_progress_time,
     $        do_progress)
         if (do_progress) then
            call cpu_time(t_end)
            t_est = (t_max - time) / time * (t_end - t_start)
            write(6,'(a6,a8,a9,a11,a9,a11,a10)') 'loop', 'time', 'M',
     $           'tot_n_samp', 'n_coag', 'tot_n_coag', 't_est'
            write(6,'(i6,f8.1,i9,i11,i9,i11,f10)') loop, time, M,
     $           tot_n_samp, n_coag, tot_n_coag, t_est
         endif
      enddo

      return
      end

CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

      subroutine compute_n_samp_hybrid(n_bin, MH, i, j, V_comp, k_max,
     $     del_t, n_samp_real)

      integer n_bin              ! INPUT: number of bins
      integer MH(n_bin)          ! INPUT: number particles per bin
      integer i                  ! INPUT: first bin 
      integer j                  ! INPUT: second bin
      real*8 V_comp              ! INPUT: computational volume
      real*8 k_max(n_bin,n_bin)  ! INPUT: maximum kernel values
      real*8 del_t               ! INPUT: timestep (s)
      real*8 n_samp_real         ! OUTPUT: number of samples per timestep
                                 !         for bin-i to bin-j events
      
      real*8 r_samp
      real*8 n_possible ! use real*8 to avoid integer overflow

c      write(*,*)'in compute_n_samp_hybrid'

      if (i .eq. j) then
         n_possible = dble(MH(i)) * (dble(MH(j)) - 1d0)
      else
         n_possible = dble(MH(i)) * dble(MH(j))
      endif
c      write(*,*)'n_possible = ', n_possible

c      write(*,*)'i,j = ', i, j
c      write(*,*)'k_max(i,j) = ', k_max(i,j)
      r_samp = k_max(i,j) * 1d0/V_comp * del_t
c      write(*,*)'r_samp = ', r_samp
      n_samp_real = r_samp * n_possible
c      write(*,*)'n_samp_real = ', n_samp_real

      return
      end

CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
