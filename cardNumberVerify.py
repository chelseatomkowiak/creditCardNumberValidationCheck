#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:47:48 2019

@author: chelsea.vizer
"""

# assign each digit to a variable
userInput = [int(i) for i in str(input("Enter an 8 digit number...  "))]
firstDigit = userInput[0]
secondDigit = userInput[1]
thirdDigit = userInput[2]
fourthDigit = userInput[3]
fifthDigit = userInput[4]
sixthDigit = userInput[5]
seventhDigit = userInput[6]
eighthDigit = userInput[7]
# calculate the sum of all digits
sum1 = eighthDigit + sixthDigit + fourthDigit + secondDigit
# other calculations to figure out whether credit card number is valid or not
two = 2
sevenDoubled = int(two * seventhDigit)
fiveDoubled = int(two * fifthDigit)
threeDoubled = int(two * thirdDigit)
oneDoubled = int(two * firstDigit)
# concatenate the previous 4 numbers into one long number
concatenate = {sevenDoubled + fiveDoubled + threeDoubled + oneDoubled}
concatenate = ("{}{}{}{}".format(sevenDoubled, fiveDoubled, threeDoubled, oneDoubled))
#print(concatenate)
#concatenate in array form
conArray = [int(i) for i in str(concatenate)]
# count number of digits in concatenate
count = len(concatenate)
# assign each digit in concatenate to it's own variable
if count == 1:
    conFirstDigit = conArray[0]
    sum2 = conFirstDigit
if count == 2:
    conFirstDigit = conArray[0]
    conSecondDigit = conArray[1]
    sum2 = (conFirstDigit + conSecondDigit)
if count == 3:
    conFirstDigit = conArray[0]
    conSecondDigit = conArray[1]
    conThirdDigit = conArray[2]
    sum2 = (conFirstDigit + conSecondDigit + conThirdDigit)
if count == 4:
    conFirstDigit = conArray[0]
    conSecondDigit = conArray[1]
    conThirdDigit = conArray[2]
    conFourthDigit = conArray[3]
    sum2 = (conFirstDigit + conSecondDigit + conThirdDigit + conFourthDigit)
if count == 5:
    conFirstDigit = conArray[0]
    conSecondDigit = conArray[1]
    conThirdDigit = conArray[2]
    conFourthDigit = conArray[3]
    conFifthDigit = conArray[4]
    sum2 = (conFirstDigit + conSecondDigit + conThirdDigit + conFourthDigit + conFifthDigit)
if count == 6:
    conFirstDigit = conArray[0]
    conSecondDigit = conArray[1]
    conThirdDigit = conArray[2]
    conFourthDigit = conArray[3]
    conFifthDigit = conArray[4]
    conSixthDigit = conArray[5]
    sum2 = (conFirstDigit + conSecondDigit + conThirdDigit + conFourthDigit + conFifthDigit + conSixthDigit)
if count == 7:
    conFirstDigit = conArray[0]
    conSecondDigit = conArray[1]
    conThirdDigit = conArray[2]
    conFourthDigit = conArray[3]
    conFifthDigit = conArray[4]
    conSixthDigit = conArray[5]
    conSeventhDigit = conArray[6]
    sum2 = (conFirstDigit + conSecondDigit + conThirdDigit + conFourthDigit + conFifthDigit + conSixthDigit + conSeventhDigit)
if count == 8:
    conFirstDigit = conArray[0]
    conSecondDigit = conArray[1]
    conThirdDigit = conArray[2]
    conFourthDigit = conArray[3]
    conFifthDigit = conArray[4]
    conSixthDigit = conArray[5]
    conSeventhDigit = conArray[6]
    conEighthDigit = conArray[7]
    sum2 = (conFirstDigit + conSecondDigit + conThirdDigit + conFourthDigit + conFifthDigit + conSixthDigit + conSeventhDigit + conEighthDigit)
totalSum = (sum1 + sum2)
# Make totalSum an array
totalSumArray = [int(i) for i in str(totalSum)]
# assign last digit of totalSum to a variable
finalNumber = totalSumArray[-1]
# if that variable is 0, card # is not valid
if finalNumber == 0:
    print("That credit card number is valid.")
else:
    print("That credit card number is not valid, please try again.")