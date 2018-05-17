__author__ = 'jnaneswar'


class recamanSeries:
    def __init__(self, filename='generateRecamanSeries_output', num=0, maxNumber=100):
        self.outputFile = filename
        self.initialNumber = num
        self.finalNumber = maxNumber


    def writeOutput(self):
        """Write Recaman's series to generateRecamanSeries_output file"""
        with open(self.outputFile, mode='wt', encoding='utf-8') as f:
            f.writelines("{0}\n".format(r)
                        for r in range(self.initialNumber, self.finalNumber))



class main:
    def main(self):
        rSeries = recamanSeries()
        rSeries.writeOutput()

if __name__ == '__main__':
    mainHandler = main()
    mainHandler.main()
