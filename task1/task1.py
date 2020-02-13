import sys
import math
from decimal import Decimal


f = open(sys.argv[1], 'r')
args = [int(line.strip()) for line in f]
f.close()

def percentile(args, perc):
    
    args.sort()
    size = len(args)
    result = Decimal(sorted(args)[int(math.ceil((size * perc)/100)) - 1])
    result = result.quantize(Decimal('1.00'))
    return result
    

a = percentile(args, 90)
b = percentile(args, 50)
c = percentile(args, 100)
d = percentile(args, 0.1)
e = Decimal(sum(args)/len(args))
e = e.quantize(Decimal('1.00'))

print (a, b, c, d, e, sep='\n')
