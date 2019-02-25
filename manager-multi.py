import csv


# Waves
wave6 = "wave6-confidence.csv"
wave5 = "wave5-confidence.csv"
wave4 = "wave4-confidence.csv"
wave3 = "wave3-confidence.csv"

# Some vars
countryList = []
continentList = []

# Gapminder files
gapminder = "indicatorpolityiv.csv"
#gapminder = "indicatorpolityiv.csv"
#gapminder = "indicatorpolityiv.csv"
#gapminder = "indicatorpolityiv.csv"
#gapminder = "indicatorpolityiv.csv"
#gapminder = "indicatorpolityiv.csv"

# Whatever you wanna name the output file
outputFileName = "democracy-score.csv"

with open(wave6, 'r') as csv_file1:
    csv_reader1 = csv.reader(csv_file1)
    next(csv_reader1)
    for line in csv_reader1:
        if line[0] not in countryList:
            countryList.append(line[0])
            continentList.append(line[1])

    def no_empty_cells(row):
        for i in range(len(row)):
            if len(row[i]) == 0:
                return False
            return True

    with open(wave5, 'r') as csv_file2:
        csv_reader2 = csv.reader(csv_file2)
        for line in csv_reader2:
            if line[0] not in countryList:
                countryList.append(line[0])
                continentList.append(line[1])

    with open(wave4, 'r') as csv_file3:
        csv_reader3 = csv.reader(csv_file3)
        for line in csv_reader3:
            if line[0] not in countryList:
                countryList.append(line[0])
                continentList.append(line[1])

    with open(wave3, 'r') as csv_file4:
        csv_reader4 = csv.reader(csv_file4)
        for line in csv_reader4:
            if line[0] not in countryList:
                countryList.append(line[0])
                continentList.append(line[1])

    with open(gapminder, 'r') as csv_file_gap:
        csv_reader2 = csv.reader(csv_file_gap)

        with open(outputFileName, 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter=',')

            lineCountGap = 0
            lineLen = 0

            for line in csv_reader2:
                if lineCountGap == 0:
                    lineCountGap += 1
                    line[0] = "name"
                    line.insert(1, "group")
                    csv_writer.writerow(line)

                elif (line[0] in countryList) and (no_empty_cells(line)):
                    idx = countryList.index(line[0])
                    line.insert(1, continentList[idx])
                    csv_writer.writerow(line)

