import xml.etree.ElementTree as ET
import sys
import os
import csv
from pretty_process import *

# 自定义一个转换的代码类
class Transformer():
    def __init__(self):
        self.outputPath = 'data/output_mods.xml'
        self.dcPath = 'data/dc_ok.xml'
        self.modsPath = 'data/mods_ok.xml'
        self.configList = None
        self.configPath = "config.csv"
        self.dcData = None
        self.modsData = None

    def setOutputPath(self,path):
        self.outputPath = path

    def setDcPath(self,path):
        self.dcPath = path

    def setModsPath(self,path):
        self.modsPath = path

    def setConfigPath(self,path):
        self.configPath = path

    # 读取配置文件到这个类中
    def loadConfig(self):
        self.configList = list()
        with open(self.configPath,newline='') as csvfile:
            reader = csv.reader(csvfile,delimiter=',')
            for row in reader:
                self.configList.append(row)
        # print(self.configList)

    # 从文件中解析dcdata和modsdata
    def loadData(self):
        self.dcData = ET.parse(self.dcPath)
        self.modsData = ET.parse(self.modsPath)

    def transform(self):
        self.preProcess()
        self.loadConfig()
        self.loadData()
        dcroot = self.dcData.getroot()
        modsroot = self.modsData.getroot()
        print("the roots are:",dcroot.tag,modsroot.tag)
        print(self.configList)
        for wordList in self.configList:
            dcword = wordList[0]
            modsword = wordList[1]
            # print(dcword,modsword)
            # 设置mods 的文件
            dctext = None
            for item in dcroot.iter(dcword):
                dctext = item.text
            for item in modsroot.iter(modsword):
                item.text = dctext
        self.modsData.write(self.outputPath)
        self.afterProcess()

    def preProcess(self):
        preprocess()

    def afterProcess(self):
        afterProcess()

if __name__ == '__main__':
    transformer = Transformer()
    transformer.transform()