# Maxwell Vale
# CS 01 Section 1
# Assignment Number 1

# Ex C.1.1 9 - 3 --> 6
# Ex C.1.2 8 * 2.5 --> 20.0
# Ex C.1.3 9 / 2 --> 4.5
# Ex C.1.4 9 / -2 --> -4.5
# Ex C.1.5 9 % 2 --> 1
# Ex C.1.6 9 % -2 --> -1
# Ex C.1.7 -9 % 2 --> 1
# Ex C.1.8 9 / -2.0 --> -4.5
# Ex C.1.9 4 + 5 * 3 --> 19
# Ex C.1.10 (4 + 5) * 3 --> 35

# Ex C.2.1 x = 100 --> 100
# Ex C.2.2 x = x + 10 --> 110
# Ex C.2.3 x += 20 --> 130
# Ex C.2.4 x = x - 40 --> 90
# Ex C.2.5 x -= 50 --> 40
# Ex C.2.6 x *= 3 --> 120
# Ex C.2.7 x /= 5 --> 24.0
# Ex C.2.8 x %= 3 --> 0.0

# Ex C.3 x += x - x when x = 3
# The first thing that Python will evaluate in the statement is the x-x
# component. After subsituting x into x - x, we get 3 - 3. So, this part of
# the statement evaluates to 0. So, the expression is now x += 0, which can
# be rewritten as x = x + 0. Now, Python will evaluate the right side of the
# statement to find out what the new assignment for x is. Subbing in for x,
# the statement becomes x = 3 + 0. Then, simplifying the right side of the
# statement, we are left with x = 3. So, now the variable x is assigned the
# value of 3.

# Ex C.4.1a 1j + 2.4j --> 3.4j
# Ex C.4.2a 4j * 4j --> (-16+0j)
# Ex C.4.3a (1+2j) / (3+4j) --> (0.44+0.08j)
# Ex C.4.1b (1+2j) * (1+2j) --> (-3+4j)
# Ex C.4.2b 1+2j * 1+2j --> (1+4j)
# The last two answers give different results because of the lack of the
# parentheses in the second expression. Python handles complex numbers by
# grouping the imaginary and real parts together whenever there are
# parentheses. This is pretty clear because all of the answers are returned
# with () around them.

# Ex C.5.1 cmath.sin(-1.0+2.0j) --> (-3.165778513216168+1.959601041421606j)
# Ex C.5.2 cmath.log(-1.0+3.4j) --> (1.2652585805200263+1.856847768512215j)
# Ex C.5.3 cmath.exp(-cmath.pi * 1.0j) --> (-1-1.2246467991473532e-16j)
# Since both math and cmath libraries have functions of the same name, you
# want to be able to tell which library it is coming from. Ex: math.sqrt()
# cmath.sqrt()

# Ex C.6.1 "foo" + 'bar' --> 'foobar'
# Ex C.6.2 "foo" 'bar' --> 'foobar'
# Ex C.6.3 a + b --> 'foobar'
# Ex C.6.4 a b --> SyntaxError: invalid syntax

# Ex C.7 'A\nB\nC'

# Ex C.8 80 * '-'

# Ex C.9 'first line\nsecond line\nthird line'

# Ex C.10.1
x = 3
y = 12.5
print ("The rabbit is {}.".format(x))
# Ex C.10.2
print ("The rabbit is {} years old.".format(x))
# Ex C.10.3
print ("{} is average.".format(y))
# Ex C.10.4
print ("{} * {}".format(y,x))
# Ex C.10.5
print ("{} * {} is {}.".format(y,x,x*y))

# Ex C.11
num = float(input("Enter a number: "))
print (num)

# Ex C.12
def quadratic(a,b,c,x):
    term1 = a * x ** 2
    term2 = b * x
    term3 = c
    return term1 + term2 + term3
# If I didn't use the ** operator, I could have just multiplied x by itself
# x * x

# Ex C.13
def GC_content(sequence):
    ''' Function GC_content will take the argument sequence and return the ratio
    of C and G characters in the string, sequence, to the total number of
    characters in the string. (C+G)/total

    Args:
    sequence --> A string comprised of the characters A, T, G, and C only

    Return:
    Returns a float that represents the ratio of C and G characters in
    sequence to the length of sequence '''
    seq = sequence.upper()
    countC = seq.count('C')
    countG = seq.count('G')
    return (countC + countG) / len(sequence)

print(GC_content('ACCAGTGTAG'))
print(GC_content('ATATATATA'))
print(GC_content('GCGGCCATGCATGGGG'))
