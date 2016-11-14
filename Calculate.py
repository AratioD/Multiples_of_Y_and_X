class Calculate():
    def findTheMultiples(self, xAndYcontraint):

        resultDeposit = {}

        # Takes every third from the loop
        for i in range(0, len(xAndYcontraint), 3):

            x = int(xAndYcontraint[i])
            y = int(xAndYcontraint[i + 1])
            constraint = int(xAndYcontraint[i + 2])

            k = 1
            while True:
                # Calculates the values
                xValue = x * k
                yValue = y * k

                if ((xValue) <= constraint):
                    resultDeposit.setdefault(constraint, []).append(xValue)
                    # resultDeposit.append(xValue)

                if ((yValue) <= constraint):
                    resultDeposit.setdefault(constraint, []).append(yValue)
                    # resultDeposit.append(yValue)

                # Breaks the code if both is ok.
                if (xValue > constraint and yValue > constraint):
                    break

                k = k + 1

        return resultDeposit
