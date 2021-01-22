class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        try:
            self.file = open(filename, 'r')
        except Exception as e:
            print("Problem opening file")
            raise e
            return None
        if header:
            self.header = self.file.readline()
        else:
            self.header = None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()

    def getdata(self):
        return self.file.readline().split(sep=self.sep)

    def getheader(self):
        return self.header



if __name__ == "__main__":
    with CsvReader('good.csv', header=True) as file:
        data = file.getdata()
        print(data)
        header = file.getheader()
        print(header)

    with CsvReader('bad.csv', header=True) as file:
        if file is None:
            print("File is corrupted")
