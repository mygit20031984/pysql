import pandas as pd
import xml.etree.ElementTree as ET

tree = ET.parse("C:/Users/Owner/PycharmProjects/pysql/Test_Files/file_xml.xml")
root = tree.getroot()

final = []
for elem in root:
    temp = {}

    for i in list(elem):
        if i:
            for c in list(i):
                temp[c.tag] = c.text
        else:
            temp[i.tag] = i.text
    final.append(temp)

df = pd.DataFrame(final)
print(df)
