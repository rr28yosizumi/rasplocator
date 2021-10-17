from .src import locator
from .src.outputter import csv_outputter

def main():
    loc = locator.Locator()
    loc.setup()
    out = csv_outputter.CsvOutputter('./test.csv')
    for data in loc.logging():
        out.put_data(data)
    out.finish()

if __name__ == '__main__':
    main()
    