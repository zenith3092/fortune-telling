#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for career

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_career = True
userDefinedDICT = {"問": ["問", "算", "請問", "問一下"], "想": ["想", "想要", "要"], "事業": ["事業", "工作", "工程", "案子", "標案", "事業運", "募資", "計畫", "企劃", "企劃案", "事業狀況", "投資案", "工作狀況"], "單身": ["單身", "母胎單身"], "屢屢": ["屢屢", "一次次", "不斷", "一直", "一次次的"], "愛情": ["愛情", "感情", "婚姻", "姻緣", "正緣", "桃花", "桃花運", "愛情運", "感情運", "感情狀況", "相處狀況"], "最近": ["最近", "近期", "這陣子"], "求職": ["求職", "求職運", "找工作", "面試", "求職狀況", "求職情況"], "考運": ["考試", "升學", "升高中", "升大學", "會考", "考會考", "學測", "考學測", "考研究所", "期中考", "期末考", "月考", "模擬考", "檢定考", "檢定", "上機考", "考運", "考試運", "考試情形", "考試狀況"], "脫單": ["脫單", "脫離單身"], "運勢": ["運勢", "流年", "運氣", "手氣"], "順利": ["順利", "順心", "太順利", "太順心"], "另一半": ["另一半", "男友", "女友", "老公", "老婆", "太太", "先生"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_career:
        print("[career] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我][想][問][事業]":
        if args[3] in userDefinedDICT["事業"]:
            resultDICT["ask"]="事業"

    if utterance == "[我][想][問][事業][順]不[順利]":
        if args[3] in userDefinedDICT["事業"]:
            resultDICT["ask"]="事業"

    if utterance == "[我][想][問][最近]的[事業]":
        if args[4] in userDefinedDICT["事業"]:
            resultDICT["ask"]="事業"

    if utterance == "[我][想][問][最近]的[事業]如何":
        if args[4] in userDefinedDICT["事業"]:
            resultDICT["ask"]="事業"

    if utterance == "[我][想][問][最近]的[新][計畫]會不[會][成功]":
        if args[5] in userDefinedDICT["事業"]:
            resultDICT["ask"]="事業"

    if utterance == "[我][想][問]關於[事業]的部分":
        if args[3] in userDefinedDICT["事業"]:
            resultDICT["ask"]="事業"

    if utterance == "[最近][事業]不太好":
        if args[1] in userDefinedDICT["事業"]:
            resultDICT["ask"]="事業"

    if utterance == "[最近]有[一個][新]的[投資案]":
        if args[3] in userDefinedDICT["事業"]:
            resultDICT["ask"]="事業"

    if utterance == "和[同事]相處不[太順利]":
        resultDICT["ask"]="事業"

    return resultDICT