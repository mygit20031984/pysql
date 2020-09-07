import json

Input_jsonFile = "C:/Users/Owner/PycharmProjects/pysql/Test_Files/gtest.json"

inputFile = open(Input_jsonFile)
data = json.load(inputFile)
print(data)
