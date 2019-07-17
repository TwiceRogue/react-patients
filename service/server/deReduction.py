# -*- coding=utf-8 -*-
__author__ = 'cat'

from sklearn.decomposition import PCA
from sklearn import manifold
import io
import datetime
from models import UpdatedAki as Newcase
from models import Stage
from sklearn.svm import SVC
from sklearn import linear_model
from sklearn.metrics import confusion_matrix
import copy


def read_file(fpath):
    patientList = []
    with io.open(fpath, 'r', encoding='utf-8') as f:
        f.readline()
        for line in f:
            lineArr = line.strip().split(',')
            aPatient = lineArr[1:]
            aPatient[4] = int(aPatient[4])
            int(aPatient[5])
            aPatient[6] = (0 if aPatient[6] == u'女' else 1)
            aPatient[7] = int(aPatient[7])
            aPatient[8] = int(aPatient[8])
            aPatient[9] = (0 if aPatient[9] == u'无' else 1)
            aPatient[10] = int(aPatient[10])
            aPatient[11] = int(aPatient[11])
            aPatient[12] = float(aPatient[12])
            aPatient[13] = float(aPatient[13])
            aPatient[14] = int(aPatient[14])
            aPatient[15] = int(aPatient[15])
            aPatient[16] = float(aPatient[16])
            aPatient[17] = int(aPatient[17])
            aPatient[18] = float(aPatient[18])
            aPatient[20] = (0 if aPatient[20] == u'无' else 1)
            patientList.append(aPatient)
    return patientList


def read_file_aki(filepath):
    patientList = []
    with io.open(filepath, 'r', encoding='utf-8') as f:
        f.readline()
        for line in f:
            lineArr = line.strip().split(',')
            aPatient = lineArr[0:]  # Procedure_data In_hos_date out_hos_date ？
            aPatient[0] = aPatient[0].encode('utf-8')
            aPatient[1] = aPatient[1].encode('utf-8')
            aPatient[2] = aPatient[2].encode('utf-8')
            aPatient[3] = aPatient[3].encode('utf-8')

            aPatient[4] = int(aPatient[4])  # aki_stage
            aPatient[5] = int(aPatient[5])  # 年龄
            aPatient[6] = (0 if aPatient[6] == u'女' else 1)  # 性别
            aPatient[7] = int(aPatient[7])  # anemia 贫血
            # aPatient[8] = aPatient[8].encode('utf-8')

            if aPatient[8] == u'无':  # 糖尿病
                aPatient[8] = 0
            elif aPatient[8] == u'见现病史':
                aPatient[8] = 2
            else:
                aPatient[8] = 1

            if aPatient[9] == u'无':  # 心力衰竭
                aPatient[9] = 0
            elif aPatient[9] == u'见现病史':
                aPatient[9] = 2
            else:
                aPatient[9] = 1

            # aPatient[9] = aPatient[9].encode('utf-8')
            aPatient[10] = int(aPatient[10])  # 主动脉内球囊反搏(IABP)
            aPatient[11] = int(aPatient[11])  # hypotension（低血压）
            aPatient[12] = float(aPatient[12])  # 对比剂用量(mL)
            aPatient[13] = round(float(aPatient[13]), 1)  # gfr（肾小球过滤率）
            aPatient[14] = int(aPatient[14])  # 心肌梗死史
            aPatient[15] = int(aPatient[15])  # Hypercholesterolemia（高胆固醇血症）
            aPatient[16] = float(aPatient[16])  # HDL-C
            aPatient[17] = int(aPatient[17])  # urgent_PCI
            aPatient[18] = float(aPatient[18])  # Pre_Crea
            # if aPatient[19] == u'无':  # 高血压
            #     aPatient[19] = 0
            # elif aPatient[19] == u'见现病史':
            #     aPatient[19] = -1
            # else:
            #     aPatient[19] = 1
            #
            # if aPatient[20] == u'无':  # 主动脉球囊反搏
            #     aPatient[20] = 0
            # elif aPatient[20] == u'见现病史':
            #     aPatient[20] = -1
            # else:
            #     aPatient[20] = 1
            # # aPatient[20] = (0 if aPatient[20] == u'无' else 1)
            # if aPatient[21] == u'无':  # 心肌梗死
            #     aPatient[21] = 0
            # elif aPatient[21] == u'见现病史':
            #     aPatient[21] = -1
            # else:
            #     aPatient[21] = 1
            # if aPatient[22] == u'无':  # 正在吸烟/近期吸烟史(<1年)
            #     aPatient[22] = 0
            # elif aPatient[22] == u'见现病史':
            #     aPatient[22] = -1
            # else:
            #     aPatient[22] = 1
            #
            # if aPatient[22] == u'无':  # 正在吸烟/近期吸烟史(<1年)
            #     aPatient[22] = 0
            # elif aPatient[22] == u'见现病史':
            #     aPatient[22] = -1
            # else:
            #     aPatient[22] = 1
            for k in range(19, 32):
                if aPatient[k] == u'无':  # 高血压	主动脉球囊反搏	心肌梗死	正在吸烟/近期吸烟史(<1年)	血脂异常	肾功能异常	冠心病家族史
                    aPatient[k] = 0  # 早发冠心病家族史	CABG手术史	使用的糖尿病治疗方案	出血性脑血管疾病	外周动脉疾病	慢性肺病
                elif aPatient[k] == u'见现病史':
                    aPatient[k] = 2
                else:
                    aPatient[k] = 1
                    # aPatient[k] = aPatient[k].encode('utf-8')

            aPatient[32] = float(aPatient[32])  # 心率
            aPatient[33] = float(aPatient[33])  # 收缩压
            aPatient[34] = float(aPatient[34])  # 舒张压

            if aPatient[35] == u'威视派克':  # 对比剂类型
                aPatient[35] = 0
            elif aPatient[35] == u'优维显':
                aPatient[35] = 1
            elif aPatient[35] == u'欧乃派克':
                aPatient[35] = 2
            elif aPatient[35] == u'典比乐':
                aPatient[35] = 3
            else:
                aPatient[35] = 4

            aPatient[36] = (0 if aPatient[36] == u'否' else 1)  # 诊断性导管

            if aPatient[37] == u'冠状动脉粥样硬化':  # 造影结论
                aPatient[37] = 0
            elif aPatient[37] == u'冠脉单支病变':
                aPatient[37] = 1
            elif aPatient[37] == u'冠脉双支病变':
                aPatient[37] = 2
            elif aPatient[37] == u'冠脉三支病变':
                aPatient[37] = 3
            elif aPatient[37] == u'冠脉造影未见明显异常':
                aPatient[37] = 4
            else:
                aPatient[37] = 5

            aPatient[38] = float(aPatient[38])  # 左主干冠状动脉>=2mm狭窄比例
            aPatient[39] = float(aPatient[39])  # LAD近段冠状动脉>=2mm狭窄比例
            aPatient[40] = float(aPatient[40])  # LAD中段/远段，对角支冠状动脉>=2mm狭窄比例
            aPatient[41] = float(aPatient[41])  # Circ、OMs、LPDA、LPL冠状动脉>=2mm狭窄比例
            aPatient[42] = float(aPatient[42])  # RCA、RPDA、RPL、AM冠状动脉>=2mm狭窄比例

            if aPatient[43] == u'否':  # 桥血管
                aPatient[43] = 0  #
            elif aPatient[43] == u'NA':
                aPatient[43] = -1
            elif aPatient[43] == u'是':
                aPatient[43] = 1
            else:
                aPatient[43] = -2

            if aPatient[44] == u'早期':  # PCI 状态
                aPatient[44] = 0  #
            elif aPatient[44] == u'NA':
                aPatient[44] = -1
            elif aPatient[44] == u'择期':
                aPatient[44] = 1
            elif aPatient[44] == u'急诊':
                aPatient[44] = 2
            else:
                aPatient[44] = -2
            aPatient[45] = aPatient[45].encode('utf-8')  # PCI 指征
            aPatient[46] = float(aPatient[46])  # D2B 时间(分钟)
            for j in range(47, 56):
                if aPatient[j] == u'否':  # 普通肝素(任意)	阿司匹林(任意)(PCI)	比伐卢定	直接凝血酶抑制剂(其他)	IIb/IIIa受体拮抗剂(任意)	氯吡格雷(
                    aPatient[j] = 0  # PCI)	普拉格雷(PCI)	替卡格雷	噻氯吡啶(PCI)
                elif aPatient[j] == u'NA':
                    aPatient[j] = -1
                elif aPatient[j] == u'是':
                    aPatient[j] = 1
                else:
                    aPatient[j] = -2
            aPatient[56] = float(aPatient[56])  # 术前肌钙蛋白I(ng/mL)
            aPatient[57] = float(aPatient[57])  # 术前血红蛋白(g/L)
            aPatient[58] = float(aPatient[58])  # 术前低密度脂蛋白(LDL)(mmol/L)
            aPatient[59] = float(aPatient[59])  # 术后肌钙蛋白I(ng/mL)(6-24小时峰值)
            aPatient[60] = float(aPatient[60])  # 术后血红蛋白(g/L)
            aPatient[61] = float(aPatient[61])  # 术后低密度脂蛋白(LDL)(mmol/L)

            if aPatient[62] == u'否':  # 对比剂过敏
                aPatient[62] = 0  #
            elif aPatient[62] == u'NA':
                aPatient[62] = -1
            elif aPatient[62] == u'是':
                aPatient[62] = 1
            else:
                aPatient[62] = -2

            patientList.append(aPatient)
    return patientList


def read_file_aki_withnumber(filepath, number):
    patientList = []
    with io.open(filepath, 'r', encoding='utf-8') as f:
        all = f.readlines()
        if number <= 50:

            intersts = all[1:number + 1]
        else:
            intersts = all[number - 49:number + 1]
        # print(intersts)
        for line in intersts:
            lineArr = line.strip().split(',')
            aPatient = lineArr[0:]  # Procedure_data In_hos_date out_hos_date ？
            aPatient[0] = aPatient[0].encode('utf-8')
            aPatient[1] = aPatient[1].encode('utf-8')
            aPatient[2] = aPatient[2].encode('utf-8')
            aPatient[3] = aPatient[3].encode('utf-8')

            aPatient[4] = int(aPatient[4])  # aki_stage
            aPatient[5] = int(aPatient[5])  # 年龄
            aPatient[6] = (0 if aPatient[6] == u'女' else 1)  # 性别
            aPatient[7] = int(aPatient[7])  # anemia 贫血
            aPatient[8] = aPatient[8].encode('utf-8')

            # if aPatient[8] == u'无':  # 糖尿病
            #     aPatient[8] = 0
            # elif aPatient[8] == u'见现病史':
            #     aPatient[8] = -1
            # else:
            #     aPatient[8] = 1

            # if aPatient[9] == u'无':  # 心力衰竭
            #     aPatient[9] = 0
            # elif aPatient[9] == u'见现病史':
            #     aPatient[9] = -1
            # else:
            #     aPatient[9] = 1

            aPatient[9] = aPatient[9].encode('utf-8')
            aPatient[10] = int(aPatient[10])  # 主动脉内球囊反搏(IABP)
            aPatient[11] = int(aPatient[11])  # hypotension（低血压）
            aPatient[12] = float(aPatient[12])  # 对比剂用量(mL)
            aPatient[13] = round(float(aPatient[13]), 1)  # gfr（肾小球过滤率）
            aPatient[14] = int(aPatient[14])  # 心肌梗死史
            aPatient[15] = int(aPatient[15])  # Hypercholesterolemia（高胆固醇血症）
            aPatient[16] = float(aPatient[16])  # HDL-C
            aPatient[17] = int(aPatient[17])  # urgent_PCI
            aPatient[18] = float(aPatient[18])  # Pre_Crea
            # if aPatient[19] == u'无':  # 高血压
            #     aPatient[19] = 0
            # elif aPatient[19] == u'见现病史':
            #     aPatient[19] = -1
            # else:
            #     aPatient[19] = 1
            #
            # if aPatient[20] == u'无':  # 主动脉球囊反搏
            #     aPatient[20] = 0
            # elif aPatient[20] == u'见现病史':
            #     aPatient[20] = -1
            # else:
            #     aPatient[20] = 1
            # # aPatient[20] = (0 if aPatient[20] == u'无' else 1)
            # if aPatient[21] == u'无':  # 心肌梗死
            #     aPatient[21] = 0
            # elif aPatient[21] == u'见现病史':
            #     aPatient[21] = -1
            # else:
            #     aPatient[21] = 1
            # if aPatient[22] == u'无':  # 正在吸烟/近期吸烟史(<1年)
            #     aPatient[22] = 0
            # elif aPatient[22] == u'见现病史':
            #     aPatient[22] = -1
            # else:
            #     aPatient[22] = 1
            #
            # if aPatient[22] == u'无':  # 正在吸烟/近期吸烟史(<1年)
            #     aPatient[22] = 0
            # elif aPatient[22] == u'见现病史':
            #     aPatient[22] = -1
            # else:
            #     aPatient[22] = 1
            for k in range(19, 32):
                # if aPatient[k] == u'无':  # 高血压	主动脉球囊反搏	心肌梗死	正在吸烟/近期吸烟史(<1年)	血脂异常	肾功能异常	冠心病家族史
                #     aPatient[k] = 0  # 早发冠心病家族史	CABG手术史	使用的糖尿病治疗方案	出血性脑血管疾病	外周动脉疾病	慢性肺病
                # elif aPatient[k] == u'见现病史':
                #     aPatient[k] = 2
                # else:
                #     aPatient[k] = 1
                aPatient[k] = aPatient[k].encode('utf-8')

            aPatient[32] = float(aPatient[32])  # 心率
            aPatient[33] = float(aPatient[33])  # 收缩压
            aPatient[34] = float(aPatient[34])  # 舒张压

            if aPatient[35] == u'威视派克':  # 对比剂类型
                aPatient[35] = 0
            elif aPatient[35] == u'优维显':
                aPatient[35] = 1
            elif aPatient[35] == u'欧乃派克':
                aPatient[35] = 2
            elif aPatient[35] == u'典比乐':
                aPatient[35] = 3
            else:
                aPatient[35] = 4

            aPatient[36] = (0 if aPatient[36] == u'否' else 1)  # 诊断性导管

            if aPatient[37] == u'冠状动脉粥样硬化':  # 造影结论
                aPatient[37] = 0
            elif aPatient[37] == u'冠脉单支病变':
                aPatient[37] = 1
            elif aPatient[37] == u'冠脉双支病变':
                aPatient[37] = 2
            elif aPatient[37] == u'冠脉三支病变':
                aPatient[37] = 3
            elif aPatient[37] == u'冠脉造影未见明显异常':
                aPatient[37] = 4
            else:
                aPatient[37] = 5

            aPatient[38] = float(aPatient[38])  # 左主干冠状动脉>=2mm狭窄比例
            aPatient[39] = float(aPatient[39])  # LAD近段冠状动脉>=2mm狭窄比例
            aPatient[40] = float(aPatient[40])  # LAD中段/远段，对角支冠状动脉>=2mm狭窄比例
            aPatient[41] = float(aPatient[41])  # Circ、OMs、LPDA、LPL冠状动脉>=2mm狭窄比例
            aPatient[42] = float(aPatient[42])  # RCA、RPDA、RPL、AM冠状动脉>=2mm狭窄比例

            if aPatient[43] == u'否':  # 桥血管
                aPatient[43] = 0  #
            elif aPatient[43] == u'NA':
                aPatient[43] = -1
            elif aPatient[43] == u'是':
                aPatient[43] = 1
            else:
                aPatient[43] = -2

            if aPatient[44] == u'早期':  # PCI 状态
                aPatient[44] = 0  #
            elif aPatient[44] == u'NA':
                aPatient[44] = -1
            elif aPatient[44] == u'择期':
                aPatient[44] = 1
            elif aPatient[44] == u'急诊':
                aPatient[44] = 2
            else:
                aPatient[44] = -2
            aPatient[45] = aPatient[45].encode('utf-8')  # PCI 指征
            aPatient[46] = float(aPatient[46])  # D2B 时间(分钟)
            for j in range(47, 56):
                if aPatient[j] == u'否':  # 普通肝素(任意)	阿司匹林(任意)(PCI)	比伐卢定	直接凝血酶抑制剂(其他)	IIb/IIIa受体拮抗剂(任意)	氯吡格雷(
                    aPatient[j] = 0  # PCI)	普拉格雷(PCI)	替卡格雷	噻氯吡啶(PCI)
                elif aPatient[j] == u'NA':
                    aPatient[j] = -1
                elif aPatient[j] == u'是':
                    aPatient[j] = 1
                else:
                    aPatient[j] = -2
            aPatient[56] = float(aPatient[56])  # 术前肌钙蛋白I(ng/mL)
            aPatient[57] = float(aPatient[57])  # 术前血红蛋白(g/L)
            aPatient[58] = float(aPatient[58])  # 术前低密度脂蛋白(LDL)(mmol/L)
            aPatient[59] = float(aPatient[59])  # 术后肌钙蛋白I(ng/mL)(6-24小时峰值)
            aPatient[60] = float(aPatient[60])  # 术后血红蛋白(g/L)
            aPatient[61] = float(aPatient[61])  # 术后低密度脂蛋白(LDL)(mmol/L)

            if aPatient[62] == u'否':  # 对比剂过敏
                aPatient[62] = 0  #
            elif aPatient[62] == u'NA':
                aPatient[62] = -1
            elif aPatient[62] == u'是':
                aPatient[62] = 1
            else:
                aPatient[62] = -2

            patientList.append(aPatient)
    return patientList


def read_aki_inDataBase(indexnumber=100):  ###录入原信息
    staff_list = Newcase.objects.all()  # 这里是所有病人数据
    staff_list_toDict = Newcase.objects.values()
    stage_list = Stage.objects.values()
    columns = Newcase._meta.get_fields(include_hidden=True)  ### 主表中每列的属性名 其中中文的已被替换
    primarykey =  Newcase._meta.pk.name
    print primarykey

    # print columns
    attrNameMap = {}  ### 建立colums属性名和真实属性名的关系map
    columns_name = []  # 属性名称 真实名称
    attr_names = []  # 属性名称 指models中的
    for attr in columns:
        # print
        attrs = str(attr).strip().split('.')
        # print attrs

        attr_names.append(attrs[2])
        # print attrs[2]
        if attr.db_column is not None:
            columns_name.append(attr.db_column)
            attrNameMap[attrs[2]] = attr.db_column
        else:
            columns_name.append(attrs[2])

    all_patients_dict = []  ###所有病人的dict
    # print attrNameMap
    idname_list = Newcase.objects.all().values_list(primarykey)
    idname_list = list(set(idname_list))
    idname_list.sort()
    id = 0
    all_patients_dict_time = []
    for idname in idname_list:
        # print idname[0]
        id_no = idname[0]
        one_patient_dict = {}
        slices = Newcase.objects.filter(pk= id_no)
        # print slices.values()
        # one_patient_dict['id'] = id
        one_patient_dict['ID'] = id
        id+=1
        one_patient_dict[primarykey] = id_no
        slices_list = []

        for query in slices.values():
            one_patient_dict_slice = {}
            # print query
            one_patient_dict_slice['ID'] = id
            for key, value in query.items():
                if attrNameMap.has_key(key):
                    one_patient_dict_slice[attrNameMap[key]] = value
                else:
                    one_patient_dict_slice[key] = value
            slices_list.append(one_patient_dict_slice)
        one_patient_dict['slices'] = slices_list
        if id ==1 :
            print one_patient_dict
        all_patients_dict_time.append(one_patient_dict)
    #  all patients with time
    #  the structure is like
    #  [{id:xx,id_no:xx,slices:[{},{},{}]}]
    # print all_patients_dict_time
    if indexnumber <= 50:
        intersts = staff_list[0:indexnumber]
        intersts_dict = staff_list_toDict[0:indexnumber]
        intersts_dict_time = all_patients_dict_time[0:indexnumber]
    else:
        intersts = staff_list[indexnumber - 50:indexnumber]
        intersts_dict = staff_list_toDict[indexnumber - 50:indexnumber]
        intersts_dict_time = all_patients_dict_time[indexnumber - 50:indexnumber]

    for obj in staff_list_toDict:
        one_patient_dict = {}

        for key, value in obj.items():

            if attrNameMap.has_key(key):
                one_patient_dict[attrNameMap[key]] = value
            else:
                one_patient_dict[key] = value
        all_patients_dict.append(one_patient_dict)

    patients_dict = []

    for obj in intersts_dict:
        one_patient_dict = {}
        for key, value in obj.items():
            if attrNameMap.has_key(key):
                one_patient_dict[attrNameMap[key]] = value
            else:
                one_patient_dict[key] = value
        patients_dict.append(one_patient_dict)


    temp = []
    for obj in stage_list:
        obj["attributename"] = obj["attributename"].strip()  #####去掉两边的空格
        temp.append(obj)
    # print temp
    # for obj in stage_list:
    #     aAttribute = []
    #     for col in ["attribute","stage"]:
    stage_list = temp  ##阶段信息

    allData = []
    all_patients_list = []

    for var in staff_list:
        patient = []
        for col in attr_names:
            attr_value = getattr(var, col)
            # if isinstance(attr_value,unicode):
            #     attr_value = attr_value.encode('utf-8')
            # print col
            patient.append(attr_value)
        # response1 += getattr(var,attr_names[3])
        # patient = read_database(patient)
        all_patients_list.append(patient)
    # staff_str = map(str, staff_list)


    patients_list = []
    for var in intersts:
        patient = []
        for col in attr_names:
            attr_value = getattr(var, col)
            # if isinstance(attr_value,unicode):
            #     attr_value = attr_value.encode('utf-8')
            # print col
            patient.append(attr_value)
        # response1 += getattr(var,attr_names[3])
        # patient = read_database(patient)
        patients_list.append(patient)

    def compareStageIndex(elem):  #######对stage_list按照阶段顺序排列
        return int(elem["stageindex"])

    stage_list.sort(key=compareStageIndex)

    columns_name = map(lambda x: x["attributename"], stage_list)

    columns_name.insert(0, 'confidence')  #######对columns_name 按照stage_list的顺序排列

    # print columns_name

    attributeRangeOrCateNum = {}  ## {"attr1name":{categoryNum:x },"attr2name":{low:a,high:b}........}

    for attrIndex in range(0, len(stage_list)):
        categorySet = []
        categoryNum = 0
        low = None
        high = None

        if stage_list[attrIndex]["category"] == "string":
            attributeRangeOrCateNum[stage_list[attrIndex]["attributename"]] = None
        elif stage_list[attrIndex]["category"] == "numerical":

            for aPatient in all_patients_dict:
                if low == None:
                    low = high = aPatient[stage_list[attrIndex]["attributename"]]
                else:
                    if aPatient[stage_list[attrIndex]["attributename"]] < low:
                        low = aPatient[stage_list[attrIndex]["attributename"]]
                    if aPatient[stage_list[attrIndex]["attributename"]] > high:
                        high = aPatient[stage_list[attrIndex]["attributename"]]
            attributeRangeOrCateNum[stage_list[attrIndex]["attributename"]] = {"low": low, "high": high}
        elif stage_list[attrIndex]["category"] == "categorical":
            for aPatient in all_patients_dict:
                if aPatient[stage_list[attrIndex]["attributename"]] in categorySet:
                    continue
                else:
                    categorySet.append(aPatient[stage_list[attrIndex]["attributename"]])
                    categoryNum = categoryNum + 1
            categorySet.sort()
            attributeRangeOrCateNum[stage_list[attrIndex]["attributename"]] = {"categoryNum": categoryNum,
                                                                               "categorySet": categorySet}

    allData.append(all_patients_list)  # 0 所有表里面的病人数据

    allData.append(patients_list)  # 1 选择50个的病人数据

    allData.append(columns_name)  # 2 列名

    allData.append(stage_list)  # 3 属性阶段对应dict

    allData.append(all_patients_dict)  # 4 所有病人dict

    allData.append(patients_dict)  # 5 50个病人dict

    allData.append(attributeRangeOrCateNum) # 6

    allData.append(all_patients_dict_time) # 7 带有时间线层叠数据

    allData.append(intersts_dict_time) # 8 50个的数据时间数据

    # print stage_list

    return allData  # a[0]全部病人   a[1]部分病人 a[2]列名  a[3]属性阶段对应dict a[4]所有病人dict  a[5]50个病人dict a[6]为每属性的范围或类别数


def read_aki_inDataBase2(indexnumber=100):
    staff_list = Newcase.objects.all()  # 这里是所有病人数据
    stage_list = Stage.objects.values()
    temp = []
    for obj in stage_list:
        obj["attributename"] = obj["attributename"].strip()  #####去掉两边的空格
        temp.append(obj)
    # print temp
    # for obj in stage_list:
    #     aAttribute = []
    #     for col in ["attribute","stage"]:
    stage_list = temp  ##阶段信息

    if indexnumber <= 50:
        intersts = Newcase.objects.all()[0:indexnumber]
    else:
        intersts = Newcase.objects.all()[indexnumber - 50:indexnumber]
    # entry_list = list(Newcase.objects.all())
    columns = Newcase._meta.get_fields(include_hidden=True)
    # print columns
    columns_name = []
    attr_names = []  # 属性名称 是指models中的
    for attr in columns:
        # print
        attrs = str(attr).strip().split('.')
        # print attrs
        attr_names.append(attrs[2])
        # print attrs[2]
        if attr.db_column is not None:
            columns_name.append(attr.db_column)
        else:
            columns_name.append(attrs[2])
    # print columns_name
    # print attr_names
    allData = []
    patients_list = []
    # test = Newcase.objects.get(id=1)
    # print test
    # test_attr = getattr(test,attr_names[6])
    # print test_attr
    for var in staff_list:
        patient = []
        for col in attr_names:
            attr_value = getattr(var, col)
            # if isinstance(attr_value,unicode):
            #     attr_value = attr_value.encode('utf-8')
            # print col
            patient.append(attr_value)
        # response1 += getattr(var,attr_names[3])
        patient = read_database(patient)
        patients_list.append(patient)
    # staff_str = map(str, staff_list)
    allData.append(patients_list)  # 所有表里面的病人数据

    patients_list = []
    for var in intersts:
        patient = []
        for col in attr_names:
            attr_value = getattr(var, col)
            # if isinstance(attr_value,unicode):
            #     attr_value = attr_value.encode('utf-8')
            # print col
            patient.append(attr_value)
        # response1 += getattr(var,attr_names[3])
        patient = read_database(patient)
        patients_list.append(patient)
    allData.append(patients_list)  # 选择50个的病人数据
    columns_name.insert(0, 'confidence')
    allData.append(columns_name)  # 列名
    numerical = []
    count = 0
    for col in attr_names:
        attr_value = getattr(staff_list[0], col)
        if isinstance(attr_value, float):
            numerical.append(columns_name[count])
        count += 1
    # print numerical
    allData.append(numerical)
    # print len(allData);
    allData.append(stage_list)
    return allData  # allData len为4 a[0]全部病人   a[1]部分病人 a[2]列名 a[3]数值型列名  a[4]属性阶段对应dict


def read_database(aPatient):
    aPatient[0] = aPatient[0]
    aPatient[1] = aPatient[1]
    aPatient[2] = aPatient[2].encode('utf-8')
    aPatient[3] = aPatient[3].encode('utf-8')

    aPatient[4] = int(aPatient[4])  # aki_stage
    aPatient[5] = int(aPatient[5])  # 年龄
    aPatient[6] = (0 if aPatient[6] == u'女' else 1)  # 性别
    aPatient[7] = int(aPatient[7])  # anemia 贫血
    # aPatient[8] = aPatient[8].encode('utf-8')

    if aPatient[8] == u'无':  # 糖尿病
        aPatient[8] = 0
    elif aPatient[8] == u'见现病史':
        aPatient[8] = 2
    else:
        aPatient[8] = 1

    if aPatient[9] == u'无':  # 心力衰竭
        aPatient[9] = 0
    elif aPatient[9] == u'见现病史':
        aPatient[9] = 2
    else:
        aPatient[9] = 1

    # aPatient[9] = aPatient[9].encode('utf-8')
    aPatient[10] = int(aPatient[10])  # 主动脉内球囊反搏(IABP)
    aPatient[11] = int(aPatient[11])  # hypotension（低血压）
    aPatient[12] = float(aPatient[12])  # 对比剂用量(mL)
    aPatient[13] = round(float(aPatient[13]), 1)  # gfr（肾小球过滤率）
    aPatient[14] = int(aPatient[14])  # 心肌梗死史
    aPatient[15] = int(aPatient[15])  # Hypercholesterolemia（高胆固醇血症）
    aPatient[16] = float(aPatient[16])  # HDL-C
    aPatient[17] = int(aPatient[17])  # urgent_PCI
    aPatient[18] = float(aPatient[18])  # Pre_Crea
    # if aPatient[19] == u'无':  # 高血压
    #     aPatient[19] = 0
    # elif aPatient[19] == u'见现病史':
    #     aPatient[19] = -1
    # else:
    #     aPatient[19] = 1
    #
    # if aPatient[20] == u'无':  # 主动脉球囊反搏
    #     aPatient[20] = 0
    # elif aPatient[20] == u'见现病史':
    #     aPatient[20] = -1
    # else:
    #     aPatient[20] = 1
    # # aPatient[20] = (0 if aPatient[20] == u'无' else 1)
    # if aPatient[21] == u'无':  # 心肌梗死
    #     aPatient[21] = 0
    # elif aPatient[21] == u'见现病史':
    #     aPatient[21] = -1
    # else:
    #     aPatient[21] = 1
    # if aPatient[22] == u'无':  # 正在吸烟/近期吸烟史(<1年)
    #     aPatient[22] = 0
    # elif aPatient[22] == u'见现病史':
    #     aPatient[22] = -1
    # else:
    #     aPatient[22] = 1
    #
    # if aPatient[22] == u'无':  # 正在吸烟/近期吸烟史(<1年)
    #     aPatient[22] = 0
    # elif aPatient[22] == u'见现病史':
    #     aPatient[22] = -1
    # else:
    #     aPatient[22] = 1
    for k in range(19, 32):
        if aPatient[k] == u'无':  # 高血压	主动脉球囊反搏	心肌梗死	正在吸烟/近期吸烟史(<1年)	血脂异常	肾功能异常	冠心病家族史
            aPatient[k] = 0  # 早发冠心病家族史	CABG手术史	使用的糖尿病治疗方案	出血性脑血管疾病	外周动脉疾病	慢性肺病
        elif aPatient[k] == u'见现病史':
            aPatient[k] = 2
        else:
            aPatient[k] = 1
            # aPatient[k] = aPatient[k].encode('utf-8')

    aPatient[32] = float(aPatient[32])  # 心率
    aPatient[33] = float(aPatient[33])  # 收缩压
    aPatient[34] = float(aPatient[34])  # 舒张压

    if aPatient[35] == u'威视派克':  # 对比剂类型
        aPatient[35] = 0
    elif aPatient[35] == u'优维显':
        aPatient[35] = 1
    elif aPatient[35] == u'欧乃派克':
        aPatient[35] = 2
    elif aPatient[35] == u'典比乐':
        aPatient[35] = 3
    else:
        aPatient[35] = 4

    aPatient[36] = (0 if aPatient[36] == u'否' else 1)  # 诊断性导管

    if aPatient[37] == u'冠状动脉粥样硬化':  # 造影结论
        aPatient[37] = 0
    elif aPatient[37] == u'冠脉单支病变':
        aPatient[37] = 1
    elif aPatient[37] == u'冠脉双支病变':
        aPatient[37] = 2
    elif aPatient[37] == u'冠脉三支病变':
        aPatient[37] = 3
    elif aPatient[37] == u'冠脉造影未见明显异常':
        aPatient[37] = 4
    else:
        aPatient[37] = 5

    aPatient[38] = float(aPatient[38])  # 左主干冠状动脉>=2mm狭窄比例
    aPatient[39] = float(aPatient[39])  # LAD近段冠状动脉>=2mm狭窄比例
    aPatient[40] = float(aPatient[40])  # LAD中段/远段，对角支冠状动脉>=2mm狭窄比例
    aPatient[41] = float(aPatient[41])  # Circ、OMs、LPDA、LPL冠状动脉>=2mm狭窄比例
    aPatient[42] = float(aPatient[42])  # RCA、RPDA、RPL、AM冠状动脉>=2mm狭窄比例

    if aPatient[43] == u'否':  # 桥血管
        aPatient[43] = 0  #
    elif aPatient[43] == u'NA':
        aPatient[43] = -1
    elif aPatient[43] == u'是':
        aPatient[43] = 1
    else:
        aPatient[43] = -2

    if aPatient[44] == u'早期':  # PCI 状态
        aPatient[44] = 0  #
    elif aPatient[44] == u'NA':
        aPatient[44] = -1
    elif aPatient[44] == u'择期':
        aPatient[44] = 1
    elif aPatient[44] == u'急诊':
        aPatient[44] = 2
    else:
        aPatient[44] = -2
    aPatient[45] = aPatient[45].encode('utf-8')  # PCI 指征
    aPatient[46] = float(aPatient[46])  # D2B 时间(分钟)
    for j in range(47, 56):
        if aPatient[j] == u'否':  # 普通肝素(任意)	阿司匹林(任意)(PCI)	比伐卢定	直接凝血酶抑制剂(其他)	IIb/IIIa受体拮抗剂(任意)	氯吡格雷(
            aPatient[j] = 0  # PCI)	普拉格雷(PCI)	替卡格雷	噻氯吡啶(PCI)
        elif aPatient[j] == u'NA':
            aPatient[j] = -1
        elif aPatient[j] == u'是':
            aPatient[j] = 1
        else:
            aPatient[j] = -2
    aPatient[56] = float(aPatient[56])  # 术前肌钙蛋白I(ng/mL)
    aPatient[57] = float(aPatient[57])  # 术前血红蛋白(g/L)
    aPatient[58] = float(aPatient[58])  # 术前低密度脂蛋白(LDL)(mmol/L)
    aPatient[59] = float(aPatient[59])  # 术后肌钙蛋白I(ng/mL)(6-24小时峰值)
    aPatient[60] = float(aPatient[60])  # 术后血红蛋白(g/L)
    aPatient[61] = float(aPatient[61])  # 术后低密度脂蛋白(LDL)(mmol/L)

    if aPatient[62] == u'否':  # 对比剂过敏
        aPatient[62] = 0  #
    elif aPatient[62] == u'NA':
        aPatient[62] = -1
    elif aPatient[62] == u'是':
        aPatient[62] = 1
    else:
        aPatient[62] = -2
    return aPatient


def creatDRmatrix_all(patientList):
    DRmatrix = []
    for aPatient in patientList:
        row = []
        row.append(aPatient[4])
        row.append(aPatient[5])
        row.append(aPatient[6])
        row.append(aPatient[7])
        row.append(aPatient[8])
        row.append(aPatient[9])
        row.append(aPatient[10])
        row.append(aPatient[11])
        row.append(aPatient[12])
        row.append(aPatient[13])
        row.append(aPatient[14])
        row.append(aPatient[15])
        row.append(aPatient[16])
        row.append(aPatient[17])
        row.append(aPatient[18])
        row.append(aPatient[20])
        DRmatrix.append(row)
    return DRmatrix


# befor an operation
def creatDRmatrix_before(patientList):
    DRmatrix = []
    for aPatient in patientList:
        row = []
        # row.append(aPatient[4])
        row.append(aPatient[5])
        row.append(aPatient[6])
        row.append(aPatient[7])
        row.append(aPatient[8])
        row.append(aPatient[9])
        # row.append(aPatient[10])
        row.append(aPatient[11])
        # row.append(aPatient[12])
        row.append(aPatient[13])
        row.append(aPatient[14])
        row.append(aPatient[15])
        row.append(aPatient[16])
        row.append(aPatient[17])
        row.append(aPatient[18])
        row.append(aPatient[20])
        DRmatrix.append(row)
    return DRmatrix


# during an operation
def creatDRmatrix_during(patientList):
    DRmatrix = []
    for aPatient in patientList:
        row = []
        # row.append(aPatient[4])
        row.append(aPatient[5])
        row.append(aPatient[6])
        row.append(aPatient[7])
        row.append(aPatient[8])
        row.append(aPatient[9])
        row.append(aPatient[10])
        row.append(aPatient[11])
        row.append(aPatient[12])
        row.append(aPatient[13])
        row.append(aPatient[14])
        row.append(aPatient[15])
        row.append(aPatient[16])
        row.append(aPatient[17])
        row.append(aPatient[18])
        row.append(aPatient[20])
        DRmatrix.append(row)
    return DRmatrix


def dimensionReduction(rdMethod, DRmatrix, n_components=2):
    results = None
    if rdMethod == 'mds':
        mds = manifold.MDS(n_components, n_init=1, max_iter=100, dissimilarity="euclidean")
        results = mds.fit_transform(DRmatrix)
    elif rdMethod == 'tsne':
        tsne = manifold.TSNE(n_components, random_state=1, metric="euclidean")
        results = tsne.fit_transform(DRmatrix)
    elif rdMethod == 'pca':
        pca = PCA(n_components)
        try:
            results = pca.fit_transform(DRmatrix)
        except Exception as e:
            print (e)
    return results


# there should have diferent matrix generations
# for before, during, and after an operation
def getPatientPos(patientList, drMethod, n_components=2):
    starttime = datetime.datetime.now()

    # befor an operation
    # during an operation
    # all the process
    DRmatrix_all = creatDRmatrix_all(patientList)
    DRPosistionMatrix_all = dimensionReduction(drMethod, DRmatrix_all)

    DRmatrix_before = creatDRmatrix_before(patientList)
    DRPosistionMatrix_before = dimensionReduction(drMethod, DRmatrix_before)

    DRmatrix_during = creatDRmatrix_during(patientList)
    DRPosistionMatrix_during = dimensionReduction(drMethod, DRmatrix_during)

    endtime = datetime.datetime.now()
    print ("time for reducing dimension: " + str((endtime - starttime)))

    return DRPosistionMatrix_before, DRPosistionMatrix_during, DRPosistionMatrix_all


def transferDataToJason(patientList, DRPosistionMatrix_before, DRPosistionMatrix_during, DRPosistionMatrix_all):
    allData = []
    allData.append(patientList)
    allData.append(DRPosistionMatrix_before.tolist())
    allData.append(DRPosistionMatrix_during.tolist())
    allData.append(DRPosistionMatrix_all.tolist())
    return allData


def transferData(patientList):
    allData = []
    allData.append(patientList)

    return allData


# if __name__ == '__main__':
#     filePath = '../resources/BBP_data.csv'
#     drMethod = 'PCA'
#     patientList = read_file(filePath)
#     DRmatrix = creatDRmatrix(patientList)
#     DRPosistionMatrix = dimensionReduction(drMethod, DRmatrix)
def creatDRmatrix_in_storyline(patientList, weightArray):
    stage = [5, 6, 7, 8, 11, 13, 14, 15, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]  # 2 入院日期 except
    DRmatrix = []
    for aPatient in patientList:
        row = []

        for index in stage:
            # print index
            # print weightArray
            row.append(aPatient[index] * weightArray[index])
        DRmatrix.append(row)
    return DRmatrix


def creatDRmatrix_early_storyline(patientList, weightArray):
    stage = [32, 33, 34, 36]
    DRmatrix = []
    for aPatient in patientList:
        row = []

        for index in stage:
            row.append(aPatient[index] * weightArray[index])
        DRmatrix.append(row)
    return DRmatrix


def creatDRmatrix_before_storyline(patientList, weightArray):
    stage = [16, 18, 56, 57, 58]
    DRmatrix = []
    for aPatient in patientList:
        row = []

        for index in stage:
            row.append(aPatient[index] * weightArray[index])
        DRmatrix.append(row)
    # print DRmatrix
    return DRmatrix


def creatDRmatrix_during_storyline(patientList, weightArray):
    stage = [10, 12, 17, 20, 35, 37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 52, 53, 54, 55,
             62]  # except 1 手术日期
    DRmatrix = []
    for aPatient in patientList:
        row = []

        for index in stage:
            row.append(aPatient[index] * weightArray[index])
        DRmatrix.append(row)
    return DRmatrix


def creatDRmatrix_after_storyline(patientList, weightArray):
    DRmatrix = []
    stage = [4, 9, 59, 60, 61]
    for aPatient in patientList:
        row = []

        for index in stage:
            row.append(aPatient[index] * weightArray[index])
        DRmatrix.append(row)
    return DRmatrix


def getPatientPos_storyline(patientList_aki, drMethod, weightArray, n_components=1):
    starttime = datetime.datetime.now()

    # befor an operation
    # during an operation
    # all the process

    DRmatrix_in = creatDRmatrix_in_storyline(patientList_aki, weightArray)
    DRPosistionMatrix_in = dimensionReduction(drMethod, DRmatrix_in, 1)

    DRmatrix_early = creatDRmatrix_early_storyline(patientList_aki, weightArray)
    DRPosistionMatrix_early = dimensionReduction(drMethod, DRmatrix_early, 1)

    DRmatrix_before = creatDRmatrix_before_storyline(patientList_aki, weightArray)
    DRPosistionMatrix_before = dimensionReduction(drMethod, DRmatrix_before, 1)
    # print len(DRPosistionMatrix_before)

    DRmatrix_during = creatDRmatrix_during_storyline(patientList_aki, weightArray)
    DRPosistionMatrix_during = dimensionReduction(drMethod, DRmatrix_during, 1)

    DRmatrix_after = creatDRmatrix_after_storyline(patientList_aki, weightArray)
    DRPosistionMatrix_after = dimensionReduction(drMethod, DRmatrix_after, 1)

    endtime = datetime.datetime.now()
    print "time for reducing dimension: " + str((endtime - starttime))

    return DRPosistionMatrix_in, DRPosistionMatrix_early, DRPosistionMatrix_before, DRPosistionMatrix_during, DRPosistionMatrix_after


def transferDataToJason_storyline(patientList_aki, DRPosistionMatrix_in,
                                  DRPosistionMatrix_early, DRPosistionMatrix_before, DRPosistionMatrix_during,
                                  DRPosistionMatrix_after):
    allData = []
    allData.append(patientList_aki)
    # print(DRPosistionMatrix_in.shape)
    allData.append(DRPosistionMatrix_in.tolist())
    allData.append(DRPosistionMatrix_early.tolist())
    allData.append(DRPosistionMatrix_before.tolist())
    allData.append(DRPosistionMatrix_during.tolist())
    allData.append(DRPosistionMatrix_after.tolist())
    return allData



def calculatingSimilarity(allPatientDictList, attributeStage, columsName, weightArray, maxStageIndex, patientID,
                          attributeRangeOrCateNum, similarity_search):

    stopAttribute = ""
    allPatientDictList_normalized = allPatientDictList  #### 将数据归一化
    similarity = []
    copyWeightArray = copy.copy(weightArray)
    for l_weightIndex in range(len(copyWeightArray)):
        if copyWeightArray[l_weightIndex]<0:
            copyWeightArray[l_weightIndex] = -copyWeightArray[l_weightIndex]

    # print allPatientDictList_normalized
    for attrIndex in range(len(columsName)):  #### attributeStage 比 columsName多一个confidence
        if columsName[attrIndex] == "confidence":
            continue
        else:
            if attributeStage[attrIndex - 1]["stageindex"] > maxStageIndex:  ###### 根据搜索的stage剪枝
                break
            else:
                stopAttribute = columsName[attrIndex]
                # if (attrIndex == len(columsName) - 1):
                #     stopAttribute = columsName[]

    for attrIndex in range(len(attributeStage)):
        attrName = attributeStage[attrIndex]["attributename"]

        if (attributeStage[attrIndex]["category"] == "string"):  #####  string型
            continue
        elif attributeStage[attrIndex]["category"] == "numerical":  #####  数值型
            for aPatient in allPatientDictList_normalized:
                aPatient[attrName] = float(aPatient[attrName] - attributeRangeOrCateNum[attrName]["low"]) / \
                                     (float(
                                         attributeRangeOrCateNum[attrName]["high"] - attributeRangeOrCateNum[attrName][
                                             "low"]) if float(
                                         attributeRangeOrCateNum[attrName]["high"] - attributeRangeOrCateNum[attrName][
                                             "low"])!= 0 else 1)
        elif attrName == "aki_stage":  #### 有序性类别
            for aPatient in allPatientDictList_normalized:
                aPatient[attrName] = float(aPatient[attrName]) / 4

        if attrName == stopAttribute:
            break
    # print allPatientDictList[10]

    searchPatient = allPatientDictList[patientID]

    for aPatient in allPatientDictList:  #### 计算相似度
        S = [0] * len(attributeStage)
        F = {}
        W = copy.copy(copyWeightArray)
        Wsum = 0
        Stemp = 0
        stopIndex = -1
        for attrIndex in range(len(attributeStage)):                            #####每个属性单独计算
            attrName = attributeStage[attrIndex]["attributename"]

            stopIndex = stopIndex + 1

            if aPatient[attrName] == "NA" or searchPatient[attrName] == "NA" or attributeStage[attrIndex][
                "category"] == "string":
                W[attrIndex] = 0
                # continue

            elif attributeStage[attrIndex]["category"] == "numerical":
                S[attrIndex] = 1 - abs(aPatient[attrName] - searchPatient[attrName])
                # if aPatient[attrName]<0 or aPatient[attrName]>1:
                #     print "aPatient wrong",aPatient[attrName],attrName
                # if searchPatient[attrName]<0  or searchPatient[attrName]>1:
                #     print "search wrong",searchPatient[attrName]
            elif attrName == "aki_stage":
                S[attrIndex] = 1 - abs(aPatient[attrName] - searchPatient[attrName])
            else:
                if aPatient[attrName] == searchPatient[attrName]:
                    S[attrIndex] = 1
                elif aPatient[attrName] == u'见现病史' and searchPatient[attrName] == u'无':
                    S[attrIndex] = 1
                elif aPatient[attrName] == u'无' and searchPatient[attrName] == u'见现病史':
                    S[attrIndex] = 1
                else:
                    S[attrIndex] = 0
            if attributeStage[attrIndex]["attributename"] == stopAttribute:
                # stopIndex = stopIndex + 1
                break
        for index in range(stopIndex + 1):
            Stemp = Stemp + S[index] * W[index]
            Wsum = Wsum + W[index]
        # if Stemp<0 or Wsum<0:
        #     print Stemp
        F["similarity_level"] = Stemp / Wsum
        F["id"] = aPatient["ID"]
        # if F["similarity_level"] >= similarity_search:
        similarity.append(F)  # 返回全部的相似度

    print stopAttribute
    print stopIndex
    print weightArray[stopIndex]
    similarity.sort(key=lambda x: x["similarity_level"], reverse=True)
    return similarity


def rankSvm(allPatientDictList, attributeStage, columsName, weightArray, maxStageIndex, patientID,
            attributeRangeOrCateNum, similarityRankArray, patientsRankMove, attributeWeightAndLocked):
    searchPatient = allPatientDictList[patientID]
    stopAttribute = ""
    allPatientDictList_normalized = allPatientDictList  #### 将数据归一化
    similarity = []
    pairwiseVector = []
    pairwiseLabel = []
    weightAndLockedArray = []
    optimizeAttrName = []
    print ("similarityRankArray")
    # print similarityRankArray
    # print attributeStage
    print maxStageIndex
    # print patientsRankMove
    # print attributeWeightAndLocked
    for attrIndex in range(len(columsName)):  #### attributeStage 比 columsName多一个confidence
        if columsName[attrIndex] == "confidence":
            continue
        else:
            if attributeStage[attrIndex - 1]["stageindex"] > maxStageIndex:  ###### 根据搜索的stage剪枝
                break
            else:
                stopAttribute = columsName[attrIndex]
                if (attrIndex == len(columsName) - 1):
                    stopAttribute = ""
    print stopAttribute
    for attrIndex in range(len(attributeStage)):  # 归一化
        attrName = attributeStage[attrIndex]["attributename"]
        if attrName == stopAttribute:
            break
        if (attributeStage[attrIndex]["category"] == "string"):  #####  string型
            continue
        elif attributeStage[attrIndex]["category"] == "numerical":  #####  数值型

            for aPatient in allPatientDictList_normalized:
                aPatient[attrName] = float(aPatient[attrName] - attributeRangeOrCateNum[attrName]["low"]) / \
                                     float(
                                         attributeRangeOrCateNum[attrName]["high"] - attributeRangeOrCateNum[attrName][
                                             "low"])
        elif attrName == "aki_stage":  #### 有序性类别z

            for aPatient in allPatientDictList_normalized:
                aPatient[attrName] = float(aPatient[attrName]) / 4
    # print allPatientDictList
    print len(similarityRankArray)
    for aSPatientIndex in range(len(similarityRankArray) - 1):  #### 病人对的向量化
        S = [3] * len(attributeStage)               ## 首先确定了维度
        F = {}
        W = weightArray
        Wsum = 0
        Stemp = 0
        stopIndex = -1

        # print int(similarityRankArray[aSPatientIndex])
        # print similarityRankArray[aSPatientIndex] + ":" +similarityRankArray[aSPatientIndex + 1]
        searchPatient = allPatientDictList_normalized[int(similarityRankArray[aSPatientIndex])]  # 顺序下来的病人对
        aPatient = allPatientDictList_normalized[int(similarityRankArray[aSPatientIndex + 1])]  # 顺序下来的病人对
        for attrIndex in range(len(attributeStage)):
            attrName = attributeStage[attrIndex]["attributename"]
            if attributeStage[attrIndex]["attributename"] == stopAttribute:
                break
            stopIndex = stopIndex + 1

            if aPatient[attrName] == "NA" or searchPatient[attrName] == "NA" or attributeStage[attrIndex][
                "category"] == "string":
                W[attrIndex] = 0
                continue

            elif attributeStage[attrIndex]["category"] == "numerical":
                if not attributeWeightAndLocked[attrName]['locked']:
                    S[attrIndex] = aPatient[attrName] - searchPatient[attrName]
            elif attrName == "aki_stage":
                if not attributeWeightAndLocked[attrName]['locked']:
                    S[attrIndex] = aPatient[attrName] - searchPatient[attrName]
            else:
                if not attributeWeightAndLocked[attrName]['locked']:
                    if aPatient[attrName] == searchPatient[attrName]:
                        S[attrIndex] = 1
                    elif aPatient[attrName] == u'见现病史' and searchPatient[attrName] == u'无':
                        S[attrIndex] = 1
                    elif aPatient[attrName] == u'无' and searchPatient[attrName] == u'见现病史':
                        S[attrIndex] = 1
                    else:
                        S[attrIndex] = 0
        F["pairwise_vector"] = S
        F["id"] = aPatient["id"]
        similarity.append(F)

        while 3 in S:
            S.remove(3)
        # print len(S)
        pairwiseVector.append(S)  # 正样本的选取
        pairwiseLabel.append(1)

        pairwiseVector.append(map(neg, S))  # 负样本由正样本的取负
        pairwiseLabel.append(-1)
        # print len(S)

        ##############################################################
        S = [3] * len(attributeStage)

        searchPatient = allPatientDictList_normalized[patientID]  # 当前搜索病人和所有相似病人之间的病人对
        aPatient = allPatientDictList_normalized[int(similarityRankArray[aSPatientIndex])]
        for attrIndex in range(len(attributeStage)):
            attrName = attributeStage[attrIndex]["attributename"]

            if attributeStage[attrIndex]["attributename"] == stopAttribute:
                break
            stopIndex = stopIndex + 1

            if aPatient[attrName] == "NA" or searchPatient[attrName] == "NA" or attributeStage[attrIndex][
                "category"] == "string":
                W[attrIndex] = 0
                continue

            elif attributeStage[attrIndex]["category"] == "numerical":
                if not attributeWeightAndLocked[attrName]['locked']:
                    S[attrIndex] = aPatient[attrName] - searchPatient[attrName]
            elif attrName == "aki_stage":
                if not attributeWeightAndLocked[attrName]['locked']:
                    S[attrIndex] = aPatient[attrName] - searchPatient[attrName]
            else:
                if not attributeWeightAndLocked[attrName]['locked']:
                    if aPatient[attrName] == searchPatient[attrName]:
                        S[attrIndex] = 1
                    elif aPatient[attrName] == u'见现病史' and searchPatient[attrName] == u'无':
                        S[attrIndex] = 1
                    elif aPatient[attrName] == u'无' and searchPatient[attrName] == u'见现病史':
                        S[attrIndex] = 1
                    else:
                        S[attrIndex] = 0
        F["pairwise_vector"] = S
        F["id"] = aPatient["id"]
        similarity.append(F)
        while 3 in S:
            S.remove(3)

        pairwiseVector.append(S)  # 正样本的选取
        pairwiseLabel.append(1)

        # print "S:"
        # print S

        pairwiseVector.append(map(neg, S))  # 负样本由正样本的取负
        pairwiseLabel.append(-1)

        ################################################################################

        for moveid in patientsRankMove:  # 移动病人的单独和每个病人的病人对
            S = [3] * len(attributeStage)
            movePatient = allPatientDictList_normalized[moveid]
            for attrIndex in range(len(attributeStage)):
                attrName = attributeStage[attrIndex]["attributename"]

                if attributeStage[attrIndex]["attributename"] == stopAttribute:
                    break
                stopIndex = stopIndex + 1

                if aPatient[attrName] == "NA" or movePatient[attrName] == "NA" or attributeStage[attrIndex][
                    "category"] == "string":
                    W[attrIndex] = 0
                    continue

                elif attributeStage[attrIndex]["category"] == "numerical":
                    if not attributeWeightAndLocked[attrName]['locked']:
                        S[attrIndex] = aPatient[attrName] - movePatient[attrName]
                elif attrName == "aki_stage":
                    if not attributeWeightAndLocked[attrName]['locked']:
                        S[attrIndex] = aPatient[attrName] - movePatient[attrName]
                else:
                    if not attributeWeightAndLocked[attrName]['locked']:
                        if aPatient[attrName] == movePatient[attrName]:
                            S[attrIndex] = 1
                        elif aPatient[attrName] == u'见现病史' and movePatient[attrName] == u'无':
                            S[attrIndex] = 1
                        elif aPatient[attrName] == u'无' and movePatient[attrName] == u'见现病史':
                            S[attrIndex] = 1
                        else:
                            S[attrIndex] = 0
            F["pairwise_vector"] = S
            F["id"] = aPatient["id"]
            similarity.append(F)
            while 3 in S:
                S.remove(3)
            pairwiseVector.append(S)  # 正样本的选取
            if similarityRankArray.index(moveid) < aSPatientIndex:
                label = 1
            else:
                label = -1
            pairwiseLabel.append(label)

            # print "S:"
            # print S

            pairwiseVector.append(map(neg, S))  # 负样本由正样本的取负
            pairwiseLabel.append(-label)

            # print "-S:"
            # print map(neg,S)
            # print "-S:"
            # print map(neg,S)
    # print similarity


    print "shujuchangdu" + str(len(allPatientDictList))
    # print pairwiseVector
    # print pairwiseLabel
    for attrIndex in range(len(attributeStage)):  # 归一化
        attrName = attributeStage[attrIndex]["attributename"]
        if attrName == stopAttribute:
            break
        elif attributeStage[attrIndex]["category"] == "string":
            continue
        else:
            if not attributeWeightAndLocked[attrName]['locked']:
                optimizeAttrName.append(attrName)
                weightAndLockedArray.append(attributeWeightAndLocked[attrName]['weight'])

    # print weightArray
    # print len(weightArray)
    print weightAndLockedArray
    print len(weightAndLockedArray)
    # print pairwiseVector
    # print pairwiseVector[0]
    print len(pairwiseVector[0])
    svm = linear_model.SGDClassifier()
    svm.fit(pairwiseVector, pairwiseLabel, coef_init=weightAndLockedArray)

    print svm.coef_
    print len(svm.coef_[0])

    print svm.score(pairwiseVector, pairwiseLabel)
    print len(pairwiseVector)
    predict_label = svm.predict(pairwiseVector)
    conf_mat = confusion_matrix(pairwiseLabel, predict_label, labels=[-1, 1])
    print conf_mat
    print len(pairwiseLabel)
    print len(predict_label)
    # print optimizeAttrName
    return svm.coef_,optimizeAttrName


def rankSvmLabel(allPatientDictList, attributeStage, columsName, weightArray, maxStageIndex, patientID,
                 attributeRangeOrCateNum, labeledAsSimiPatients, labeledNotSimiPatients, attributeWeightAndLocked):
    searchPatient = allPatientDictList[patientID]
    stopAttribute = ""
    allPatientDictList_normalized = allPatientDictList  #### 将数据归一化
    similarity = []
    pairwiseVector = []
    pairwiseLabel = []
    weightAndLockedArray = []
    optimizeAttrName = []
    print ("similarityRankArray")
    # print similarityRankArray
    print attributeStage
    print "maxStageIndex:"
    print maxStageIndex
    # print patientsRankMove
    # print attributeWeightAndLocked
    # for attrIndex in range(len(columsName)):  #### attributeStage 比 columsName多一个confidence
    #     if columsName[attrIndex] == "confidence":
    #         continue
    #     else:
    #         if attributeStage[attrIndex]["stageindex"] > maxStageIndex:  ###### 根据搜索的stage剪枝
    #             continue
    #         else:
    #             stopAttribute = columsName[attrIndex]
    #             if (attrIndex == len(columsName) - 1):
    #                 stopAttribute = ""
    # print stopAttribute
    for attrIndex in range(len(attributeStage)):  # 归一化
        attrName = attributeStage[attrIndex]["attributename"]
        if attributeStage[attrIndex]["stageindex"] > maxStageIndex:
            continue
        if (attributeStage[attrIndex]["category"] == "string"):  #####  string型
            continue
        elif attributeStage[attrIndex]["category"] == "numerical":  #####  数值型

            for aPatient in allPatientDictList_normalized:
                aPatient[attrName] = float(aPatient[attrName] - attributeRangeOrCateNum[attrName]["low"]) / \
                                     float(
                                         attributeRangeOrCateNum[attrName]["high"] - attributeRangeOrCateNum[attrName][
                                             "low"])
        elif attrName == "aki_stage":  #### 有序性类别z

            for aPatient in allPatientDictList_normalized:
                aPatient[attrName] = float(aPatient[attrName]) / 4
    # print allPatientDictList
    print len(labeledAsSimiPatients)
    for aSPatientIndex in range(len(labeledAsSimiPatients) - 1):  #### 病人对的向量化
        S = [3] * len(attributeStage)  ## 首先确定了维度
        F = {}
        W = weightArray
        Wsum = 0
        Stemp = 0
        stopIndex = -1

        # print int(similarityRankArray[aSPatientIndex])
        # print similarityRankArray[aSPatientIndex] + ":" +similarityRankArray[aSPatientIndex + 1]
        searchPatient = allPatientDictList_normalized[int(labeledAsSimiPatients[aSPatientIndex])]  #

        for aPatientIndex in labeledNotSimiPatients:
            if int(allPatientDictList_normalized[aPatientIndex]['ID']) not in labeledAsSimiPatients:
                aPatient = allPatientDictList_normalized[aPatientIndex]  # 相似和不相似病人之间的病人对
                for attrIndex in range(len(attributeStage)):
                    attrName = attributeStage[attrIndex]["attributename"]
                    if attributeStage[attrIndex]["stageindex"] > maxStageIndex:
                        continue
                    stopIndex = stopIndex + 1

                    if aPatient[attrName] == "NA" or searchPatient[attrName] == "NA":
                        S[attrIndex] = 0
                        continue
                    elif attributeStage[attrIndex]["category"] == "string":
                        continue
                    elif attributeStage[attrIndex]["category"] == "numerical":
                        if not attributeWeightAndLocked[attrName]['locked']:
                            S[attrIndex] = aPatient[attrName] - searchPatient[attrName]
                    elif attrName == "aki_stage":
                        if not attributeWeightAndLocked[attrName]['locked']:
                            S[attrIndex] = aPatient[attrName] - searchPatient[attrName]
                    else:
                        if not attributeWeightAndLocked[attrName]['locked']:
                            if aPatient[attrName] == searchPatient[attrName]:
                                S[attrIndex] = 1
                            elif aPatient[attrName] == u'见现病史' and searchPatient[attrName] == u'无':
                                S[attrIndex] = 1
                            elif aPatient[attrName] == u'无' and searchPatient[attrName] == u'见现病史':
                                S[attrIndex] = 1
                            else:
                                S[attrIndex] = 0
                F["pairwise_vector"] = S
                F["id"] = aPatient["ID"]
                similarity.append(F)
            else:
                continue

        while 3 in S:
            S.remove(3)
        # print len(S)
        pairwiseVector.append(S)  # 正样本的选取
        pairwiseLabel.append(1)

        pairwiseVector.append(map(neg, S))  # 负样本由正样本的取负
        pairwiseLabel.append(-1)
        # print len(S)

    ##############################################################


    for aSPatientIndex in range(len(labeledNotSimiPatients)):
        S = [3] * len(attributeStage)  ## 首先确定了维度
        F = {}
        W = weightArray
        Wsum = 0
        Stemp = 0
        stopIndex = -1
        searchPatient = allPatientDictList_normalized[patientID]  # 当前搜索病人和所有不相似病人之间的病人对
        aPatient = allPatientDictList_normalized[int(labeledNotSimiPatients[aSPatientIndex])]
        for attrIndex in range(len(attributeStage)):
            attrName = attributeStage[attrIndex]["attributename"]

            if attributeStage[attrIndex]["stageindex"] > maxStageIndex:
                continue
            stopIndex = stopIndex + 1

            if aPatient[attrName] == "NA" or searchPatient[attrName] == "NA":
                S[attrIndex] = 0
                continue
            elif attributeStage[attrIndex]["category"] == "string":
                continue
            elif attributeStage[attrIndex]["category"] == "numerical":
                if not attributeWeightAndLocked[attrName]['locked']:
                    S[attrIndex] = aPatient[attrName] - searchPatient[attrName]
            elif attrName == "aki_stage":
                if not attributeWeightAndLocked[attrName]['locked']:
                    S[attrIndex] = aPatient[attrName] - searchPatient[attrName]
            else:
                if not attributeWeightAndLocked[attrName]['locked']:
                    if aPatient[attrName] == searchPatient[attrName]:
                        S[attrIndex] = 1
                    elif aPatient[attrName] == u'见现病史' and searchPatient[attrName] == u'无':
                        S[attrIndex] = 1
                    elif aPatient[attrName] == u'无' and searchPatient[attrName] == u'见现病史':
                        S[attrIndex] = 1
                    else:
                        S[attrIndex] = 0
        F["pairwise_vector"] = S
        F["id"] = aPatient["ID"]
        similarity.append(F)
        while 3 in S:
            S.remove(3)

        pairwiseVector.append(S)  # 正样本的选取
        pairwiseLabel.append(-1)

        # print "S:"
        # print S

        pairwiseVector.append(map(neg, S))  # 负样本由正样本的取负
        pairwiseLabel.append(1)

        ################################################################################

    for aSPatientIndex in range(len(labeledAsSimiPatients)):
        S = [3] * len(attributeStage)  ## 首先确定了维度
        F = {}
        W = weightArray
        Wsum = 0
        Stemp = 0
        stopIndex = -1
        searchPatient = allPatientDictList_normalized[patientID]  # 当前搜索病人和所有相似病人之间的病人对
        aPatient = allPatientDictList_normalized[int(labeledAsSimiPatients[aSPatientIndex])]
        for attrIndex in range(len(attributeStage)):
            attrName = attributeStage[attrIndex]["attributename"]

            if attributeStage[attrIndex]["stageindex"] > maxStageIndex:
                continue
            stopIndex = stopIndex + 1

            if aPatient[attrName] == "NA" or searchPatient[attrName] == "NA" :
                S[attrIndex] = 0
                continue
            elif attributeStage[attrIndex]["category"] == "string":
                continue
            elif attributeStage[attrIndex]["category"] == "numerical":
                if not attributeWeightAndLocked[attrName]['locked']:
                    S[attrIndex] = aPatient[attrName] - searchPatient[attrName]
                    print attrName
            elif attrName == "aki_stage":
                if not attributeWeightAndLocked[attrName]['locked']:
                    S[attrIndex] = aPatient[attrName] - searchPatient[attrName]
                    print attrName
            else:
                if not attributeWeightAndLocked[attrName]['locked']:
                    print attrName
                    if aPatient[attrName] == searchPatient[attrName]:
                        S[attrIndex] = 1
                    elif aPatient[attrName] == u'见现病史' and searchPatient[attrName] == u'无':
                        S[attrIndex] = 1
                    elif aPatient[attrName] == u'无' and searchPatient[attrName] == u'见现病史':
                        S[attrIndex] = 1
                    else:
                        S[attrIndex] = 0
        F["pairwise_vector"] = S
        F["id"] = aPatient["ID"]
        similarity.append(F)
        # print "S:"
        # print len(S)
        while 3 in S:
            S.remove(3)
        # print len(S)
        pairwiseVector.append(S)
        pairwiseLabel.append(-1)

        # print "S:"
        # print S

        pairwiseVector.append(map(neg, S))  # 负样本由正样本的取负
        pairwiseLabel.append(1)

    # print similarity



    print "shujuchangdu" + str(len(allPatientDictList))
    # print pairwiseVector
    # print pairwiseLabel
    for attrIndex in range(len(attributeStage)):  # 找到一共有几个计算的属性
        attrName = attributeStage[attrIndex]["attributename"]
        if attributeStage[attrIndex]["stageindex"] > maxStageIndex:
            continue
        elif attributeStage[attrIndex]["category"] == "string":
            continue
        else:
            if not attributeWeightAndLocked[attrName]['locked']:
                print attrName
                optimizeAttrName.append(attrName)
                weightAndLockedArray.append(attributeWeightAndLocked[attrName]['weight'])

    # print weightArray
    # print len(weightArray)
    print weightAndLockedArray
    print len(weightAndLockedArray)
    # print pairwiseVector
    print len(pairwiseVector[0])
    # for i in pairwiseVector:
    #     print len(i)
    print optimizeAttrName
    svm = linear_model.SGDClassifier()
    svm.fit(pairwiseVector, pairwiseLabel, coef_init=weightAndLockedArray)

    print svm.coef_
    print len(svm.coef_[0])

    print svm.score(pairwiseVector, pairwiseLabel)
    print len(pairwiseVector)
    predict_label = svm.predict(pairwiseVector)
    conf_mat = confusion_matrix(pairwiseLabel, predict_label, labels=[-1, 1])
    print 'conf_mat:'
    print conf_mat
    print 'conf_mat over'
    print len(pairwiseLabel)
    print len(predict_label)
    # print optimizeAttrName
    return svm.coef_, optimizeAttrName


def neg(x):
    if x == 1.0:
        x = 1
    elif x == 0.0:
        x = 0
    else:
        x = -x
    # x = -x
    return x


def saveWeight(weightArray,attributeStage):

    for aAttrIndex in range(len(attributeStage)):
        if attributeStage[aAttrIndex]["category"] == 'string':
            continue

        # print 1
        # print attributeStage[aAttrIndex]["attributename"].strip()
        # print attributeStage[aAttrIndex]
        # print Stage.objects.values()[aAttrIndex]["attributename"]
        obj = Stage.objects.get(attributename=attributeStage[aAttrIndex]["attributename"].strip())
        obj.weight = float(weightArray[aAttrIndex])
        obj.save()
    print weightArray
    return None