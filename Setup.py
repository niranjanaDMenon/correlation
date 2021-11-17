import (module) numpy
import numpy as np


def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        print(row)
        for row in csv_reader:
            print(row)
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

            return {"x": marks_in_percentage,"y":days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(data["x"],datasource["y"])


def setup():
    data_path = "./data/Student Marks vs Days Present"

    datasource = getDataSource(data_path)
    print(datasource)

    findCorrelation(datasource)

    setup()
    