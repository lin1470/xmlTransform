# xmlTransform
直接运行main.py  
需要注意的是:  
1. 首先这程序需要提供配置文件config.csv,左边是dc原数据标签,右边是要转换到mods的标签
2. 程序中各个数据的路径配置如下:(具体在Transformer中)
```
self.outputPath = 'data/output_mods.xml' // 输出的moods数据路径
        self.dcPath = 'data/dc_ok.xml'  // dc原数据路径
        self.modsPath = 'data/mods_ok.xml' //处理后的Mods路径
        self.configList = None
        self.configPath = "config.csv"  // 标签的配置路径
        self.dcData = None
        self.modsData = None
```
