# --------------------------------------------------------------------------------------------------------------------*
# Author: AratioD @2016
# MULTIPLES OF X AND Y
# Data Structure: One Main program and three class files.
# Main class: MultiplesXY.py
# Data class file 1/3: ReadFile.py: Class: ReadFile
# Data class file 2/3: Calculate.py: Class: Calculate
# Data class file 3/3: WriteFile.py: Class: HypotenusePrintClass
# --------------------------------------------------------------------------------------------------------------------*

# IMPORT all four classes
from ReadFile import ReadFile
readfile = ReadFile()

from Calculate import Calculate
calculate = Calculate()

from WriteFile import WriteFile
writefile = WriteFile()

# MAIN PROGRAM---------------------------------------------------------------------------------------------------------*

# Read the input data name from keyboard and returns the file name
inputDatafileName = readfile.readInputFile()

# Calculated the row amount of the file
rowAmount = readfile.howManyLinesAreInTheInputFile(inputDatafileName)

# Prepares input data to file transforms it to array
xAndYconstraint = readfile.prepareDataForCalculation(inputDatafileName, rowAmount)

resultDeposit = calculate.findTheMultiples(xAndYconstraint)

# Sort data and write results into file
writefile.writeDataIntoFile(resultDeposit)