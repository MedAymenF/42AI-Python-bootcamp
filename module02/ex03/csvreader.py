class CsvReader():
    def __init__(self, filename=None, sep=',',
                 header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.corrupted = False

        try:
            self.file = open(filename, 'r')
        except Exception as e:
            print("Problem opening file")
            raise e
            return None

        if header:
            self.header = self.file.readline().split(sep=self.sep)
            self.header = [field.strip() for field in self.header]
        else:
            self.header = None

        self.data = []
        for line in self.file:
            row = line.strip().split(sep=self.sep)
            row = [field.strip() for field in row if len(field)]
            self.data.append(row)
            if (len(row) != len(self.data[0])):
                self.corrupted = True
                return None

        if skip_top:
            self.data.pop(0)
        if skip_bottom:
            self.data.pop(-1)

    def __enter__(self):
        if (self.corrupted):
            return None
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()

    def getdata(self):
        return self.data

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
        else:
            data = file.getdata()
            print(data)
            header = file.getheader()
            print(header)
