import csv



wave = "wave6-confidence.csv"
#wave = "wave5-confidence.csv"
#wave = "wave4-confidence.csv"
#wave = "wave3-confidence.csv"

countryList = []

gapminder = "indicatorpolityiv.csv"

with open(wave, 'r') as csv_file1:
    csv_reader1 = csv.reader(csv_file1)

    next(csv_reader1)

    def no_empty_cells(row):
        for i in range(len(row)):
            if len(row[i]) == 0:
                return False
            return True

    for line in csv_reader1:
        countryList.append(line[0])

    with open(gapminder, 'r') as csv_file2:
        csv_reader2 = csv.reader(csv_file2)

        with open('new_file.csv', 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter=',')

            lineCount2 = 0
            lineLen = 0

            for line in csv_reader2:
                if lineCount2 == 0:
                    lineLen = len(line)
                    lineCount2 += 1
                    csv_writer.writerow(line)

                elif (line[0] in countryList) and (no_empty_cells(line)):
                    csv_writer.writerow(line)

