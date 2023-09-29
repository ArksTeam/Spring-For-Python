import time

class Log:
    def __init__(self, logFileName, formatString='[Time {}] {}'):
        self.logFileName = logFileName
        self.formatString = formatString
        self.file = None

    def __enter__(self):
        self.file = open(self.logFileName, 'a')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def writeNewLog(self, text):
        self.file.write(self.formatString.format(str(time.time()), text))

    def readLogLine(self):
        with open(self.logFileName, 'r') as file:
            return file.readlines()

    def readLogOneLine(self, num):
        logTextList = self.readLogLine()
        logOnlyLineText = logTextList[num]
        return logOnlyLineText

    def readTextLog(self):
        with open(self.logFileName, 'r') as file:
            txt = file.read()
            return str(txt)
