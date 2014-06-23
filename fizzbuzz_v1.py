#!/usr/bin/python

import sys, getopt

def fizzbuzz(n):
 
    if n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)
 
def main(argv):
   start = 1
   end = 100
   try:
      opts, args = getopt.getopt(argv,"hs:e:")
   except getopt.GetoptError:
      print 'fizzbuzz.py -s <startvalue> -e <endvalue>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'fizzbuzz.py -s <startvalue> -e <endvalue>'
         sys.exit()
      elif opt in ("-s"):
         start = int(arg)
      elif opt in ("-e"):
         end = int(arg)     
   print "\n".join(fizzbuzz(n) for n in range(start, end))

if __name__ == "__main__":
   main(sys.argv[1:])


