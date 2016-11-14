class WriteFile():
    def writeDataIntoFile(self, resultDeposit):
        inputFileName = raw_input("Please give a output file name --> ")
        file = open(inputFileName + ".txt", "w")

        #
        for key, value in sorted(resultDeposit.items(), key=lambda item: (item[0], item[1])):
            file.write("%s: %s" % (key, sorted(value)))

            # Writes a empty line into program.
            file.write("\n")

        file.close()
