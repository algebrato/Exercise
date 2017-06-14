program test_pi

        use ISO_FORTRAN_ENV

        implicit none

        real(kind=8)    :: step, x, s, pi_greco
        integer(kind=int64) :: num_steps, i

        num_steps=1000000000

        s= 0d0
        step = 1.0d0 / num_steps

        !OMP PARALLEL
        !OMP DO PRIVATE(x) REDUCTION(+:s)
            do i = 1, num_steps
                x = (i-0.5d0) * step
                s = s + 4.0d0 / (1.0d0 + x*x)
            end do
        !OMP END DO        
        !OMP END PARALLEL

        pi_greco = s * step

        write(*,'(A,1F12.10,A)') "Obtained value of PI: ", pi_greco

end program test_pi
