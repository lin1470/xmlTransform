def preprocess():
    print('preprocess')
    attribute = None
    with open('data/mods.xml','r') as xmlfile:
        content = xmlfile.readlines()
        # print(content)
        secondLine = content[1:2][0][0:-1]
        wordLength = len(secondLine.split(' ')[0][1:])
        attribute = secondLine[2+wordLength:-1]
        # print(attribute)
    with open('data/attributeConfig.txt','w') as attfile:
        attfile.write(attribute)

    with open('data/mods_ok.xml','w') as writefile:
        lineCount = 0
        for row in content:
            lineCount += 1
            if lineCount == 2:
                row = row.replace(attribute,'',len(attribute))
                print(attribute,'\n',row)
                writefile.write(row)
            else:
                writefile.write(row)

def afterProcess():
    print("afterprocess")
    attribute = None
    with open('data/attributeConfig.txt','r') as attrfile:
        attribute = attrfile.readline()
        print(attribute)
    xmltitle = '<?xml version="1.0"?>\n'
    with open('data/output_mods.xml','r+') as outputfile:
        firstline = outputfile.readline()[0:-2] + ' '+ attribute + '>\n'
        content = outputfile.readlines()
        outputfile.seek(0,0)
        outputfile.write(xmltitle+firstline)
        for row in content:
            outputfile.write(row)


