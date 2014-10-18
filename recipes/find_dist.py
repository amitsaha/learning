# INPUT SAMPLE:

# Your program should accept as its first argument a path to a filename. Input example is the following

# (25, 4) (1, -6)
# (47, 43) (-25, -11)
# All numbers in input are integers between -100 and 100.

# OUTPUT SAMPLE:

# Print results in the following way.

# 26
# 90

import re
points_pattern = re.compile('-{0,1}\d+, -{0,1}\d+')
with open('points.dat') as f:
    for line in f:
        points = re.findall(points_pattern, line.rstrip('\n'))
        point1 = [float(x) for x in points[0].split(',')]
        point2 = [float(x) for x in points[1].split(',')]
        print ((point2[1]-point1[1])**2 + (point2[0]-point1[0])**2)**0.5
        
        
    
