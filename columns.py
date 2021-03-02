import xml.etree.cElementTree as ET

mytree=ET.parse('taxi.xml')
myroot=mytree.getroot()
#print(myroot[0][0].attrib)

allcolumns=[]
for x in myroot[0]:
    value=x.tag
    allcolumns.append(value)

print(allcolumns)

'''record={}
    for tag in ('vendor','people'):
        value=x.find(tag).text
        record[tag]=value
    print(record)'''











