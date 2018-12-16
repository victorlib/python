
# -*- coding: utf-8 -*-  
import json
import re
dic = {
    "控制柜":"Control Cabinet",
    "送风机启动柜":"Supply Fan Start-up Cabinet",
    "下层送风机启动柜":"Down Supply Fan Start-up Cabinet",
    "上层回风机启动柜":"Up Return Fan Start-up Cabinet",
    "变频器":"VFD Brand",
    "无":"N/A",
    "英威腾":"INVT",
    "安川":"YASKAWA",
	"预留点位："	:"Reserved Control Point:",
    "启停方式":"Start-up Cabinet Type",
	"DDC控制柜":	"DDC Control Cabinet",
    "变频启动柜":"VF Type",
    "本地启动柜":"Local Control",
    "远程启动柜":"Remote Control",
    "温度控制柜":"Temp. Control Cabinet",
    "控制方式":"Control Mode",
    "回风温度控制":"R.A Temp. Control",
    "送风温度控制":"S.A Temp. Control",
    "回风温湿度控制":"R.A Temp.&Hum. Control",
    "送风温湿度控制":"S.A Temp.&Hum. Control",
    "通讯接口":"Communication Port",
    "品牌：":"Brand:",
    "风阀执行器":"Damper Actuator",
    "水阀及执行器":"Water valve and Actuator",
    "预留控制点：":"Reserved Control Point:",
    "冷水阀及执行器阀门类型":"Chiller Water valve and Actuator valve Type",
    "二通阀":"Two-way valve",
    "三通阀":"Three-way valve",
    "其他控制部件：":"Other Accessories:",
    "新风温湿度传感器：":"F.A Temp.&Hum. Sensor:",
    "回风温湿度传感器：":"R.A Temp.&Hum. Sensor:",
    "送风温湿度传感器：":"S.A Temp.&Hum. Sensor:",
    "卡乐":"CAREL",
    "预留点位":"Reserved Control Point",
    "模拟量输入":"AI",
    "模拟量输出":"AO",
    "数字量输入":"DI",
    "数字量输出":"DO",
	"风压传感器：\n(西门子品牌)":"Air Pressure Sensor:\n(SIEMENS Brand )",
	"风速传感器：\n(西门子品牌)":"Velocity Sensor:\n(SIEMENS Brand )",
	"防冻开关：\n(西门子品牌)":"Anti-freezing Switch:\n(SIEMENS Brand )",
	"冷盘后温度传感器：":"Temp. Sensor after chiller coil:",
    "预留电流":"Reserved Current",
    "电机控制方式":"Motor Control Mode",
    "手动设定频率":"Set Frequency Manually",
    "风速控制风机变频":"Velocity Control",
    "风压控制风机变频":"Pressure Control ",
    "新风温度传感器：":"F.A Temp. Sensor:",
    "回风温度传感器：":"R.A Temp. Sensor:",
    "送风温度传感器：":"S.A Temp. Sensor:",
    "冷盘后温度传感器":"Temp. Sensor after chiller coil",
    "控制部件清单输出":"Output",
    "确定":"Confirm",
    "功能":"Features",
    "取消":"Cancel"
}

str3 = r'(.*if\s\()_T\(\"([\u4e00-\u9fa5]+.*)\"\)\s*(.*)\s*(.*)(\).*)'
re_test = re.compile(str3)
strtest = '				if (_T("送风温湿度控制")==strControlType || _T("回风温湿度控制")==strControlType) {'

list1 = []
list2 = []
f = open("example1.txt","r", encoding='utf-8')
fnew = open("example2.txt","w", encoding='utf-8')

lines = f.readlines()      #读取全部内容 ，并以列表方式返回
pp = "||"
for line in lines:
    m = re_test.match(line)
    if m:
        value = dic.get(m.group(2),"Tencent")
        pp = ' || ' if '==' in m.group(3) else ' && '
        result = m.group(1) + "_T(\"" + m.group(2) + "\")" + m.group(3) + m.group(4) + pp + "_T(\"" + value + "\")" + m.group(3) + m.group(4) + m.group(5)
        print(result)
        fnew.write(result)
        fnew.write('\n')
    else:
        
        fnew.write(line)

f.close()
fnew.close()
