import pandas as pd
import xml.etree.ElementTree as et

xtree = et.parse("C:/Users/Owner/PycharmProjects/pysql/Test_Files/file_xml.xml")
xroot = xtree.getroot()

df_cols = ["name", "email", "grade", "age"]
rows = []

for node in xroot:
    s_name = node.attrib.get("name")
    s_mail = node.find("email").text if node is not None else None
    s_grade = node.find("grade").text if node is not None else None
    s_age = node.find("age").text if node is not None else None

    rows.append({"name": s_name, "email": s_mail, "grade": s_grade, "age": s_age})

out_df = pd.DataFrame(rows, columns=df_cols)
print(out_df)
