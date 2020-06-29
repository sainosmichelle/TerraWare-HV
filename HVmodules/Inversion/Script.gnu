set terminal pngcairo enhanced dashed size 1550.0, 800.0
set style line 1 lc rgb "black" lt -1 lw 0.7 dt 4
set style line 2 lc rgb "black" lt -1 lw 0.3 dt 5
set xtics font "Arial black, 11" autofreq
set ytics font "Arial black, 11" autofreq 
set mxtics 4 
set mytics 4 
set grid xtics mxtics ls 1,ls 2 
set grid ytics mytics ls 1,ls 2 
unset key 
set output 'InvertModelHVSR.png' 
set yrange [*:] reverse
plot 'InvertModelHVSR.dat' u 2:1 w l lt -1 lw 2 linecolor 3 , 'InvertModelHVSR.dat' u 3:1 w l lt -1 lw 2 linecolor 3 , 'InvertModelHVSR.dat' u 4:1 w l lt -1 lw 2 linecolor 3,'InitialModelHVSR.dat' u 2:1 w l lt -1 lw 2 linecolor 4 , 'InitialModelHVSR.dat' u 3:1 w l lt -1 lw 2 linecolor 2 , 'InitialModelHVSR.dat' u 4:1 w l lt -1 lw 2 linecolor 3 
unset yrange 
set terminal pngcairo enhanced dashed size 1550.0, 800.0
set style line 1 lc rgb "black" lt -1 lw 0.7 dt 4
set style line 2 lc rgb "black" lt -1 lw 0.3 dt 5
set yrange restore
set autoscale y  
set xtics font "Arial black, 11" autofreq
set ytics font "Arial black, 11" autofreq 
set mxtics 4 
set mytics 4 
set grid xtics mxtics ls 1,ls 2 
set grid ytics mytics ls 1,ls 2 
unset key 
set output 'DataHVSR.png' 
plot 'DataHVSR.dat' u 1:2 with lines lt -1 lw 1.5 linecolor 3,'DataHVSR.dat' u 1:3 with lines lt -1 lw 1.5 linecolor 2 
set terminal pngcairo enhanced dashed size 1550.0, 800.0
set title 'Convergencia' 
set xlabel ' Iteracion [n]'
set ylabel ' Error  [mGal^2]'
set autoscale y   
set output 'ConvergenciaEData.png' 
set logscale x 
set logscale y 
plot 'ConvergenceEData.txt' u 1 with lines lt -1 lw 2 linecolor 3 t "" 
set terminal pngcairo enhanced dashed size 1550.0, 800.0
set title 'Convergencia' 
set xlabel ' Iteracion [n]'
set ylabel ' Error  [mGal^2]'
set autoscale y   
set output 'ConvergenciaEGrad.png' 
set logscale x 
set logscale y 
plot 'ConvergenceEGrad.txt' u 1 with lines lt -1 lw 2 linecolor 3 t "" 
set terminal pngcairo enhanced dashed size 1550.0, 800.0
set title 'Convergencia' 
set xlabel ' Iteracion [n]'
set ylabel ' Error  [mGal^2]'
set autoscale y   
set output 'ConvergenciaETotal.png' 
set logscale x 
set logscale y 
plot 'ConvergenceETotal.txt' u 1 with lines lt -1 lw 2 linecolor 3 t "" 
