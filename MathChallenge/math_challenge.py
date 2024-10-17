#!/usr/bin/bash python3

def MathChallenge(num):
    num_str = str(num)
    for i in range(len(num_str)-1, 0, - 1):
        if num_str[ i-1 ] < num_str[i]:
            return int( num_str[:i-1] + num_str[i] + num_str[i-1] + num_str[i+1:]  )
    return -1
print( MathChallenge( 123 ) )
print( MathChallenge( 11121 ) )
print( MathChallenge( 41352 ) )
print( MathChallenge( 999 ) )
