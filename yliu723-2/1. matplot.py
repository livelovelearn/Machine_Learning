# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 23:13:52 2015
code to plot figures in analysis
@author: yancheng
"""
import matplotlib.pyplot as plt
###### PartI: Neural Network (cancer) weights optimized by RHC, SA or GA instead of backprop############
###Correct percentage vs training iteration times

x = [5,55,105,155,205,255,305,355,405,455,505,555,605,655,705,755,805,855,905,955]
y1 = [65,72.14285714,82.85714286,88.57142857,86.42857143,92.14285714,88.57142857,87.85714286,90.71428571,91.42857143,90.71428571,93.57142857,90.71428571,92.85714286,92.14285714,92.85714286,97.14285714,95,92.85714286,95.71428571]
y2 = [65,60,34.28571429,61.42857143,32.85714286,21.42857143,35,35,35,50.71428571,49.28571429,55,55.71428571,66.42857143,62.14285714,85,69.28571429,89.28571429,85,82.14285714,]
y3 = [81.42857143,87.85714286,89.28571429,87.85714286,89.28571429,90,90,91.42857143,90.71428571,92.14285714,90.71428571,91.42857143,92.85714286,91.42857143,92.85714286,90.71428571,93.57142857,93.57142857,93.57142857,93.57142857]

plt.plot(x, y1, 'r-', label='RHC')
plt.plot(x, y2, 'b-', label='SA')
plt.plot(x, y3, 'g-', label='GA')

plt.title("Neural Network (cancer)",fontsize = 18)
plt.xlabel("# of training iterations",fontsize = 18)
plt.ylabel("accuracy %",fontsize = 18)
plt.legend()
plt.show()

##tweak SA parameters
###Correct percentage vs training iteration times

x = [5,55,105,155,205,255,305,355,405,455,505,555,605,655,705,755,805,855,905,955]
y1 = [65,60,34.28571429,61.42857143,32.85714286,21.42857143,35,35,35,50.71428571,49.28571429,55,55.71428571,66.42857143,62.14285714,85,69.28571429,89.28571429,85,82.14285714,]
y2 = [36.42857143,62.14285714,53.57142857,63.57142857,73.57142857,79.28571429,90.71428571,75,90,90.71428571,94.28571429,89.28571429,87.85714286,90.71428571,92.85714286,88.57142857,92.85714286,95.71428571,94.28571429,91.42857143]
plt.plot(x, y1, 'r-', label='T=1e11, cooling=0.95')
plt.plot(x, y2, 'b-', label='T=100, cooling=0.90')


plt.title("Neural Network (cancer)--Simulated Annealing",fontsize = 18)
plt.xlabel("# of training iterations",fontsize = 18)
plt.ylabel("accuracy %",fontsize = 18)
plt.legend()
plt.show()

###Correct percentage vs training sample size

x = [2,4,8,16,32,64,128,256,512]
y1 = [68.57142857,78.57142857,77.14285714,87.85714286,93.57142857,93.57142857,97.85714286,97.14285714,96.42857143]
y2 = [68.57142857,70,75.71428571,85,81.42857143,82.14285714,87.14285714,94.28571429,89.28571429]
y3 = [68.57142857,77.14285714,80,83.57142857,91.42857143,94.28571429,97.85714286,97.85714286,95.71428571]

plt.plot(x, y1, 'r-', label='RHC')
plt.plot(x, y2, 'b-', label='SA')
plt.plot(x, y3, 'g-', label='GA')

plt.title("Neural Network (cancer)",fontsize = 18)
plt.xlabel("# of training sample size",fontsize = 18)
plt.ylabel("accuracy %",fontsize = 18)
plt.legend()
plt.show()


###Part II: Random Optimization problems####
###fitness vs # of iterations -- OneMax

x = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350, 370, 390, 410, 430, 450, 470, 490]
y1 = [107.0, 116.0, 128.0, 138.0, 150.0, 163.0, 177.0, 185.0, 189.0, 193.0, 197.0, 198.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0]
y2 = [90.0, 89.0, 93.0, 110.0, 123.0, 148.0, 162.0, 175.0, 182.0, 189.0, 192.0, 193.0, 195.0, 197.0, 199.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0]
y3 = [116.0, 115.0, 116.0, 123.0, 120.0, 126.0, 122.0, 117.0, 117.0, 121.0, 113.0, 115.0, 133.0, 126.0, 125.0, 126.0, 124.0, 125.0, 126.0, 118.0, 128.0, 128.0, 119.0, 126.0, 134.0]
y4 = [150.0, 166.0, 173.0, 178.0, 188.0, 188.0, 194.0, 193.0, 194.0, 194.0, 194.0, 198.0, 198.0, 197.0, 200.0, 198.0, 198.0, 198.0, 198.0, 200.0, 199.0, 200.0, 200.0, 199.0, 199.0]

plt.plot(x, y1, 'r-', label='RHC')
plt.plot(x, y2, 'b-', label='SA')
plt.plot(x, y3, 'g-', label='GA')
plt.plot(x, y4, 'k-', label='MIMIC')

plt.title("Random Optimization (One-Max)",fontsize = 18)
plt.xlabel("# of iterations",fontsize = 18)
plt.ylabel("Fitness",fontsize = 18)
plt.legend()
plt.show()


###tweak GA parameters
###fitness vs # of population size -- OneMax GA

x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195]
y1 = [101.0, 105.0, 102.0, 107.0, 111.0, 107.0, 110.0, 112.0, 118.0, 124.0, 123.0, 114.0, 121.0, 123.0, 120.0, 128.0, 123.0, 133.0, 123.0, 123.0, 128.0, 133.0, 127.0, 131.0, 136.0, 138.0, 123.0, 136.0, 138.0, 135.0, 133.0, 138.0, 141.0, 145.0, 133.0, 130.0, 130.0, 140.0, 143.0]

plt.plot(x, y1, 'r-')


plt.title("Random Optimization (One-Max)",fontsize = 18)
plt.xlabel("GA population size",fontsize = 18)
plt.ylabel("Fitness",fontsize = 18)
plt.legend()
plt.show()

###fitness vs # of crossoverRate -- OneMax GA

x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195]
y1 = [117.0, 113.0, 114.0, 118.0, 117.0, 129.0, 129.0, 136.0, 124.0, 136.0, 127.0, 133.0, 135.0, 139.0, 135.0, 130.0, 133.0, 132.0, 134.0, 140.0, 136.0, 144.0, 136.0, 141.0, 145.0, 144.0, 147.0, 145.0, 142.0, 152.0, 149.0, 152.0, 140.0, 145.0, 154.0, 149.0, 154.0, 150.0, 145.0]

plt.plot(x, y1, 'r-')


plt.title("Random Optimization (One-Max)",fontsize = 18)
plt.xlabel("GA crossover rate",fontsize = 18)
plt.ylabel("Fitness",fontsize = 18)
plt.legend()
plt.show()

###fitness vs # of mutationRate -- OneMax GA

x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195]
y1 = [117.0, 115.0, 118.0, 120.0, 126.0, 118.0, 131.0, 132.0, 124.0, 128.0, 128.0, 124.0, 134.0, 128.0, 131.0, 137.0, 126.0, 137.0, 125.0, 139.0, 136.0, 137.0, 132.0, 142.0, 131.0, 138.0, 145.0, 137.0, 135.0, 139.0, 136.0, 136.0, 136.0, 133.0, 140.0, 134.0, 133.0, 142.0, 133.0]

plt.plot(x, y1, 'r-')


plt.title("Random Optimization (One-Max)",fontsize = 18)
plt.xlabel("GA mutation rate",fontsize = 18)
plt.ylabel("Fitness",fontsize = 18)
plt.legend()
plt.show()


###fitness vs # of iterations -- knapsack

x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290]
y1 = [1.018117526997608e-07, 1.064208460986168e-07, 432.67750105347056, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893, 496.05799881036893]
y2 = [8.064220346858773e-08, 4.9446679765653245e-08, 5.921373157968187e-08, 7.555562347249389e-08, 8.142180014032604e-08, 8.648042596761202e-08, 8.439444761293451e-08, 7.70508795408381e-08, 6.594394990777776e-08, 729.0405218397688, 813.2318940910112, 813.2318940910112, 813.2318940910112, 813.2318940910112, 813.2318940910112, 813.2318940910112, 813.2318940910112, 813.2318940910112, 813.2318940910112, 813.2318940910112, 813.2318940910112, 813.2318940910112, 813.2318940910112, 813.2318940910112, 813.2318940910112, 813.2318940910112, 813.2318940910112, 813.2318940910112, 813.2318940910112]
y3 = [682.2624829168651, 770.9836415240021, 829.2895701007893, 933.0537753121607, 914.7090919996658, 959.6489169091936, 1053.8976383748025, 1092.501494424457, 1117.938787215727, 1092.9923561877074, 1092.9923561877074, 1092.9923561877074, 1092.501494424457, 1092.9923561877074, 1092.9923561877074, 1118.4296489789774, 1128.7061067827544, 1148.8883250081208, 1148.7863380187084, 1148.7863380187084, 1148.7863380187084, 1148.7863380187084, 1148.7863380187084, 1148.7863380187084, 1148.7863380187084, 1148.7863380187084, 1148.7863380187084, 1149.5606781168358, 1148.7863380187084]
y4 = [1098.5021312388778, 1161.6957593323573, 1161.6957593323573, 1161.6957593323573, 1161.2048975691068, 1161.2048975691068, 1161.2048975691068, 1161.6957593323573, 1161.2048975691068, 1161.2048975691068, 1161.2048975691068, 1161.2048975691068, 1161.6957593323573, 1161.6957593323573, 1161.2048975691068, 1161.2048975691068, 1161.2048975691068, 1161.2048975691068, 1161.2048975691068, 1161.6957593323573, 1161.2048975691068, 1161.2048975691068, 1161.2048975691068, 1161.6957593323573, 1161.6957593323573, 1161.6957593323573, 1161.6957593323573, 1161.6957593323573, 1161.6957593323573]

plt.plot(x, y1, 'r-', label='RHC')
plt.plot(x, y2, 'b-', label='SA')
plt.plot(x, y3, 'g-', label='GA')
plt.plot(x, y4, 'k-', label='MIMIC')

plt.title("Random Optimization (knapsack)",fontsize = 18)
plt.xlabel("# of iterations",fontsize = 18)
plt.ylabel("Fitness",fontsize = 18)
plt.legend()
plt.show()

###fitness vs # of evaluation -- travelingSalesMan

x = [500, 50500, 100500, 150500, 200500, 250500, 300500, 350500, 400500, 450500]
y2 = [0.041650600234639124, 0.135616614005359, 0.135616614005359, 0.135616614005359, 0.135616614005359, 0.135616614005359, 0.135616614005359, 0.135616614005359, 0.135616614005359, 0.135616614005359]
y1 = [0.08853791549372551, 0.13276509567876124, 0.13276509567876124, 0.13276509567876124, 0.13276509567876124, 0.13276509567876124, 0.13276509567876124, 0.13276509567876124, 0.13276509567876124, 0.13276509567876124]
y3 = [0.059010424947184344, 0.1688190989085543, 0.16829588386247663, 0.16766499498176574, 0.16766499498176574, 0.16766499498176574, 0.1658987211933221, 0.16780821632312382, 0.16780821632312387, 0.16780821632312384]
y4 = [0.05077876419526826, 0.09521164911850305, 0.10580473016726429, 0.1071550970190015, 0.11739625923631619, 0.11399001108559856, 0.12224870868462161, 0.12187152801630798, 0.12180992124445815, 0.12348613084475475]

plt.plot(x, y1, 'r-', label='RHC')
plt.plot(x, y2, 'b-', label='SA')
plt.plot(x, y3, 'g-', label='GA')
plt.plot(x, y4, 'k-', label='MIMIC')

plt.title("Random Optimization (TSP)",fontsize = 18)
plt.xlabel("# of evaluations",fontsize = 18)
plt.ylabel("Fitness",fontsize = 18)
plt.legend()
plt.show()

###fitness vs # of iterations -- travelingSalesMan

x = [1, 101, 201, 301, 401, 501, 601, 701, 801, 901]
y1 = [0.03920634225765702, 0.05954704212716756, 0.06849998179975984, 0.07665451586075134, 0.08903375364193282, 0.09373959244265509, 0.09536453240285081, 0.09643067642820176, 0.09743609568283927, 0.0977217926629018]
y2 = [0.04034552798000711, 0.03786732833735157, 0.040797956390005906, 0.03868516598606998, 0.04219454489484142, 0.0367531908059395, 0.03893856677880282, 0.03594542364015769, 0.03732751947075881, 0.03852392344703177]
y3 = [0.05169945770241529, 0.1510590007548645, 0.140851032721558, 0.15447954994980517, 0.15674172721243176, 0.15848542399252336, 0.15750666174066735, 0.15610251630810737, 0.1567487135891464, 0.15750666174066735]
y4 = [0.0493996440530149, 0.08026249192640827, 0.09689454113655183, 0.10375858781800973, 0.10804000494591445, 0.10988083370482522, 0.1087292457296244, 0.11572958683034511, 0.11415304456773057, 0.10982322554705719]

plt.plot(x, y1, 'r-', label='RHC')
plt.plot(x, y2, 'b-', label='SA')
plt.plot(x, y3, 'g-', label='GA')
plt.plot(x, y4, 'k-', label='MIMIC')

plt.title("Random Optimization (TSP)",fontsize = 18)
plt.xlabel("# of iterations",fontsize = 18)
plt.ylabel("Fitness",fontsize = 18)
plt.legend()
plt.show()