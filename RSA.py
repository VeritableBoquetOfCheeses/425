"""
#Name: William Scott
#Class: CSC 447
#Date: Mar 2nd, 2017
#File Name: 447RSA.py
#Description: This file is to demonstrate a simplified version of the RSA encryption
#algorithm and employ it as a means to better understand assymetric encryption and 
#exposure to a language I've never used before.  I could've done this in C, C++, Java, 
#COBOL(though not likely) or Visual Basic.  I'm glad I picked Python.
"""
#COMPILE WITH "python3" COMMAND WHEN EXECUTING#
import sys
import math
from fractions import gcd
import random
import string
import array

#Application functions | Remember that indentation dictates control blocks in code#

#generateD(int, int) generates the multiplicative modulo inverse for the RSA private key component#

def generateD(e_temp, phi_temp):
	d_temp = 2
	while (d_temp < 10000000):
		if((d_temp * e_temp) % phi_temp == 1):
			return d_temp
		d_temp += 1

#end generateD()#

#isPrime(int) checks whether or not the integer entered is prime or not#
def isPrime(numToCheck):
	if (numToCheck < 1000 and numToCheck >= 25):
		for divisor in range(2, numToCheck):
			if not (numToCheck % divisor):
				print ("That is not a prime number. Please try again: ")
				return False
	else:
		print ("The number", numToCheck, "is not between 25 and 999; please enter a three-digit-or-less prime number.")
		return False
	return True
#end isPrime()#

def generateE(numToCheck, phi):
	if numToCheck > 1:
		for divisor in range(2, numToCheck):
			if not (numToCheck % divisor):
				return False
	else:
		return False
	return True
#end generateE()#

#sameInput(int, int) function#
def sameInput(pValue, qValue):
	if qValue == pValue:
		print ("That q-value is equal to the given p-value; please enter a different three-digit prime integer")
		return False
	return True
#end sameInput()#

#User input | check if prime after input - if not prime, re-request integer submission#
	#annotated as p & q#
print("Please enter P-value\n\tRequirements: no longer than 3-digits and prime")
p = int(input())
while not isPrime(p):
	p = int(input())

print("Please enter Q-value\n\tRequirements: no longer than 3-digits and prime")
q = int(input())
while not isPrime(q) or not sameInput(p,q):
	q = int(input())

#Calculate n#
	# n is the modulus for the public key and the private keys#
n = p * q

#Calculate the totient#
	# phi(n) = (p-1)(q-1)#
phiOfN = (p - 1) * (q - 1)

#Calculate e#
	# 1 < e < phi(n)#
	# e & phi(n) must be coprime | GCD is 1, no other factors in common#
	# e is the public key exponent#
e = random.randint(2, phiOfN)
while not generateE(e, phiOfN) or (gcd(e, phiOfN) > 1):
	e = random.randint(2, phiOfN)

#Calculate d#
d = generateD(e, phiOfN)

#Provide plain text#
print ("Please provide some plain text, whatever you desire, to be encrypted then decrypted:")
planeText = input()
tester = planeText.encode('utf-8')
cipherText = array.array('i',(0 for i in range(0,len(tester))))
decryptedInterim = array.array('i',(0 for i in range(0,len(tester))))

#Encrypt plainText#
	#C = p^e mod n#
for index in range(len(tester)):
	cipherText[index] = (tester[index]**e) % n

#Make cipher text readable for output#
cipherInStringFormat = ""
for index in range(len(tester)):
	cipherInStringFormat += str(cipherText[index])

#Decrypt cipher text back into plain text#
	#P = c^d mod n#
for index in range(len(tester)):
	decryptedInterim[index] = (cipherText[index]**d) % n

#Make decrypted cipher text readable for output#
decryptedCipher = ""
for index in range(len(tester)):
	decryptedCipher += chr(decryptedInterim[index])

#Output as per instructions
print("\n\nFINAL OUTPUT:\n\n")
print ("- p value:", p, "| q value:", q, "\n- n value:", n, "\n- phi(n) value:", phiOfN, "\n- e value:", e, "| d value:", d )
print ("- Plain text:", planeText, "\n- Cipher text:", cipherInStringFormat, "\n- Decrypted text:", decryptedCipher)