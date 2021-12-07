from src import locator
from src.outputter import csv_outputter

MAXCOUNT = 100
def main():
    loc = locator.Timeinterval_Locator()
    out = csv_outputter.CsvOutputter('./test.csv')
    count = 0
    for data in loc.logging():
        out.put_data(data)
        count += 1
        if count > MAXCOUNT:
            break
    out.finish()

if __name__ == '__main__':
    main()
    