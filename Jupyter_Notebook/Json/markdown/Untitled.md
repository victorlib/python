

```python
import json

file_name = "Contorl_Access"
with open(file_name+".txt") as f:
    dict = json.load(f)
    for key in dict:
        print('map_array_[2][_T("'+key+'")]'+'='+'_T("'+dict[key]+'");')
```

    map_array_[2][_T("控制柜")]=_T("Control Cabinet");
    map_array_[2][_T("送风机启动柜")]=_T("Supply Fan Start-up Cabinet");
    map_array_[2][_T("下层送风机启动柜")]=_T("Down Supply Fan Start-up Cabinet");
    map_array_[2][_T("上层回风机启动柜")]=_T("Up Return Fan Start-up Cabinet");
    map_array_[2][_T("模块控制柜")]=_T("Module Control Cabinet");
    map_array_[2][_T("变频器")]=_T("VFD Type");
    map_array_[2][_T("无")]=_T("N/A");
    map_array_[2][_T("英威腾")]=_T("INVT");
    map_array_[2][_T("安川")]=_T("YASKAWA");
    map_array_[2][_T("启停方式")]=_T("        Type");
    map_array_[2][_T("变频启动柜")]=_T("VF Type");
    map_array_[2][_T("本地启动柜")]=_T("Local Control");
    map_array_[2][_T("远程启动柜")]=_T("Remote Control");
    map_array_[2][_T("温度控制柜")]=_T("Temp. Control Cabinet");
    map_array_[2][_T("控制方式")]=_T("Control Mode");
    map_array_[2][_T("回风温度控制")]=_T("RA Temp. Control ");
    map_array_[2][_T("送风温度控制")]=_T("SA Temp. Control ");
    map_array_[2][_T("回风温湿度控制")]=_T("RA Temp.&Hum. Control");
    map_array_[2][_T("送风温湿度控制")]=_T("SA Temp.&Hum. Control");
    map_array_[2][_T("通讯接口")]=_T("Communication Port");
    map_array_[2][_T("电机控制方式")]=_T("Motor Control Mode");
    map_array_[2][_T("手动设定频率")]=_T("Set Frequency Manually");
    map_array_[2][_T("风速控制风机变频")]=_T("Control Fan Speed by Air Velocity");
    map_array_[2][_T("风压控制风机变频")]=_T("Control Fan Speed by Air Pressure");
    map_array_[2][_T("品牌")]=_T("Brand");
    map_array_[2][_T("风阀执行器")]=_T("Damper Actuator");
    map_array_[2][_T("水阀及执行器")]=_T("Water Valve and Actuator");
    map_array_[2][_T("预留控制点")]=_T("Reserved Control Point");
    map_array_[2][_T("冷水阀及执行器阀门类型")]=_T("Water Valve and Actuator Type");
    map_array_[2][_T("二通阀")]=_T("Two-way Valve");
    map_array_[2][_T("三通阀")]=_T("Three-way Valve");
    map_array_[2][_T("其他控制部件：")]=_T("Other Accessories:");
    map_array_[2][_T("新风温湿度传感器")]=_T("FA Temp.&Hum. Sensor");
    map_array_[2][_T("回风温湿度传感器")]=_T("RA Temp.&Hum. Sensor");
    map_array_[2][_T("送风温湿度传感器")]=_T("SA Temp.&Hum. Sensor");
    map_array_[2][_T("卡乐")]=_T("CAREL");
    map_array_[2][_T("预留点位")]=_T("Reserved Control Point");
    map_array_[2][_T("模拟量输入")]=_T("AI");
    map_array_[2][_T("模拟量输出")]=_T("AO");
    map_array_[2][_T("数字量输入")]=_T("DI");
    map_array_[2][_T("数字量输出")]=_T("DO");
    map_array_[2][_T("预留电流")]=_T("Reserved Current");
    map_array_[2][_T("新风温度传感器")]=_T("FA Temp. Sensor");
    map_array_[2][_T("回风温度传感器")]=_T("RA Temp. Sensor");
    map_array_[2][_T("送风温度传感器")]=_T("SA Temp. Sensor");
    map_array_[2][_T("冷盘后温度传感器")]=_T("Temp. Sensor after Cooling Coil");
    map_array_[2][_T("控制部件清单输出")]=_T("Output");
    map_array_[2][_T("确定")]=_T("Confirm");
    map_array_[2][_T("取消")]=_T("Cancel");
    map_array_[2][_T("新风温湿度传感器：")]=_T("FA Temp.Hum. Sensor:");
    map_array_[2][_T("回风温湿度传感器：")]=_T("RA Temp.Hum. Sensor:");
    map_array_[2][_T("送风温湿度传感器：")]=_T("SA Temp.Hum. Sensor:");
    map_array_[2][_T("新风温度传感器：")]=_T("FA Temp. Sensor:");
    map_array_[2][_T("回风温度传感器：")]=_T("RA Temp. Sensor:");
    map_array_[2][_T("送风温度传感器：")]=_T("SA Temp. Sensor:");
    map_array_[2][_T("预留控制点：")]=_T("Reserved Control Point:");
    map_array_[2][_T("预留点位：")]=_T("Reserved Control Point:");
    map_array_[2][_T("冷盘后温度传感器：")]=_T("Temp. Sensor after Cooling Coil:");
    map_array_[2][_T("风压传感器：
    (西门子品牌)")]=_T("Air Pressure Sensor: 
    (SIEMENS Brand)");
    map_array_[2][_T("风速传感器：
    (西门子品牌)")]=_T("Velocity Sensor: 
    (SIEMENS Brand)");
    map_array_[2][_T("防冻开关：
    (西门子品牌)")]=_T("Anti-freezing Switch: 
    (SIEMENS Brand)");
    map_array_[2][_T("预留控制点0~10V")]=_T("Reserved Control Point0~10V");
    map_array_[2][_T("预留控制点4~20mA")]=_T("Reserved Control Point4~20mA");
    map_array_[2][_T("DDC控制柜")]=_T("DDC Control Cabinet");
    map_array_[2][_T("控制柜：")]=_T("Control Cabinet:");
    map_array_[2][_T("直接启动(无变频)")]=_T("Direct Start (Without VF)");
    map_array_[2][_T("品牌：")]=_T("Brand:");
    map_array_[2][_T("温控器品牌")]=_T("Thermostat Brand");
    map_array_[2][_T("RS485通讯模块")]=_T("RS485 Communication Module");
    map_array_[2][_T("有")]=_T("Applied");
    map_array_[2][_T("西门子")]=_T("SIEMENS");
    map_array_[2][_T("室内型")]=_T("Indoor");
    map_array_[2][_T("室外型")]=_T("Outdoor");
    
