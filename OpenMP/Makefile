EXEC=pi

FC=gfortran

FOPT=-O2 -fopenmp

$(EXEC): pi.f90
	$(FC) $(FOPT) -o $(EXEC) pi.f90


clean:
	rm -f *.o $(EXEC)

.PHONY: clean
