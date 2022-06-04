def next_edge(side1,side2):
    third_edge=0
    third_edge=side1+side2-1
    print("Third Edge: "+str(third_edge))
next_edge(8,10)
next_edge(5,7)
next_edge(9,2)

# def football_points(*numbers):
#     sum=0
#     sum=numbers[0]*3+numbers[1]*1+numbers[2]*0
#     print("Points obtains: "+str(sum))

# football_points(3,4,2)
# football_points(5,0,2)
# football_points(0,0,1)

# def animals(*animal):
#     count=0
#     count=animal[0]*2+animal[1]*4+animal[2]*4
#     print("No of legs: "+str(count))
# animals(2,3,5)
# animals(1,2,3)
# animals(5,2,8)

# def difference_max_min(numbers):
#     numbers.sort()
#     size=len(numbers)
#     min=numbers[0]
#     max=numbers[size-1]
#     difference=max-min
#     print("Difference: "+str(difference))
   
# difference_max_min([44,32,86,19])
# difference_max_min([10,4,1,4,-10,-50,32,21])