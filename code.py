import random
import statistics
import plotly.figure_factory as ff


dice_result = []

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    dice_result.append(dice1+ dice2)

mean = sum(dice_result)/len(dice_result)
print("The mean value is: "+str(mean))

median = statistics.median(dice_result)
print("The median of Data is:"+str(median))

mode = statistics.mode(dice_result)
print("The mode value of the data is: "+str(mode));

std_dev = statistics.stdev(dice_result)
print("The standard deviation: "+ str(std_dev))

fig = ff.create_distplot([dice_result],["Result"], show_hist =False)
fig.show()


firstStdevstart,firstStdevend=mean-std_dev,mean+std_dev
list1stdev=[result for result in dice_result if result>firstStdevstart and result<firstStdevend]
print("{}% of data lies within 1 standard deviation".format(len(list1stdev)*100.0/len(dice_result)))

secondStdevStart,secondstdevend=mean-(2*std_dev),mean+(2*std_dev)
list2=[result for result in dice_result if result>secondStdevStart and result<secondstdevend]
print("{}% of data lies within 2 standard deviation".format(len(list2)*100.0/len(dice_result)))

thirdstart,thirdend=mean-(3*std_dev),mean+(3*std_dev)

list3=[result for result in dice_result if result>thirdstart and result<thirdend]
print("{}% of data lies within 3 standard deviation".format(len(list3)*100.0/len(dice_result)))



