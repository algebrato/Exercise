#!/usr/bin/gnuplot

set terminal pdf fontscale 0.44 size 10,10
set output "ssh_connection_refused.pdf"
set size 0.5,0.5
set origin 0,0
set multiplot
	set size 1,0.5
	set origin 0,0
	set style data histogram
	set style histogram cluster gap 1
	set style fill solid border -1
	set boxwidth 1
	set title "SSH - Connection failed for invalid users"
	p './Nation_Uniq.dat' u 1:xticlabel(2) title 'Connection by invalid users'
	
	set size 1,0.5
	set origin 0,0.5
	set style data histogram
	set style histogram cluster gap 1
	set style fill solid border -1
	set boxwidth 1
	set title "SSH - Connection failed for correct users"
	p './Nation_Uniq2.dat' u 1:xticlabel(2) title 'Connection by correct users'
unset multiplot
