class ReadFile():
    def readInputFile(self):
        inputFileName = raw_input("Please upload the input file --> ")
        inputFile = inputFileName + ".txt"
        return inputFile

    def howManyLinesAreInTheInputFile(self, inputFile):
        with open(inputFile) as f:
            sumOfInputFileRows = sum(1 for _ in f)

        return sumOfInputFileRows

    def prepareDataForCalculation(self, inputFileName, howManyLinesAreInFile):
        xAndYandContraint = []

        from itertools import islice
        with open(inputFileName) as fin:
            for line in islice(fin, 1, howManyLinesAreInFile):
                x, y, constraint = line.split()
                xAndYandContraint.append(x)
                xAndYandContraint.append(y)
                xAndYandContraint.append(constraint)

        return xAndYandContraint
