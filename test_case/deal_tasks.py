#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Project：complain 
# @File：deal_tasks.py
# @IDE：PyCharm 
# @Date：2021/3/19 9:42 
# @Author: zhangy
from config import config
from common import findme
from common import login
import json
import  requests


def find_the_tasks(token):
    '''

    :param token:
    :return:
    '''
    list = findme.findme(token)
    #print(list)
    url = config.url+"/uap/flow/my/"+list["loginName"]+"/processtask?keywords=&startTime=&endTime=&type_=&orgIds=&userName=y1&page=1&pageSize=10&arriveSort=1"
    #print(url)
    headers = {
        "Authorization":token,
        "Content-Type":"application/json"
    }
    res = requests.get(url=url,headers=headers)
    #print(res.text)
    return res.json()["data"]["procList"]["list"]
#token = login.access_Token_Login(config.username,config.password)
#find_the_tasks(token)
#print(find_the_tasks(token))

def choosetheway(token):
    '''

    :param token:
    :return:
    '''
    list = find_the_tasks(token)
    url =config.url+"/uap/flow/formview/"+list[0]["processDefinitionId"]+"/"+list[0]["tasks"][0]["taskDefinitionKey"]
    #print(url)
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    res =requests.get(url=url,headers=headers)
    #print(res.text)
    return res.json()["data"]["buttons"][0]["action"]
#token=login.access_Token_Login(config.username,config.password)
#print(choosetheway(token))

def procereslut():
    token = login.access_Token_Login(config.username, config.password)
    list = find_the_tasks(token)
    #print(list)
    url = config.url+"/uap/flow/ifDisplayProcessingResult?processInstanceId="+list[0]["tasks"][0]["processInstanceId"]
    #print(url)
    headers ={
        "Authorization":token
    }
    res = requests.get(url=url,headers=headers)
    print(res.text)
    return res.json()["data"]
#token=login.access_Token_Login(config.username,config.password)
procereslut()
print(procereslut())

def dealTasks(token):
    '''

    :param token:
    :return:
    '''
    action =choosetheway(token)
    list1 = find_the_tasks(token)
    display = procereslut()
    #print(list1)
    #print(action)
    if action == "complete" :
        url = config.url+"/uap/flow/complete/task/"+list1[0]["tasks"][0]["id"]
    else:
        url= config.url+"/uap/flow/transmit/"+list1[0]["tasks"][0]["id"]
    if display == True:
        data = {
            "action": action,
            "name": "回复",
            "taskId": list1[0]["tasks"][0]["id"],
            "processingResult": 1
        }
    else:
        data = {
            "action": action,
            "name": "回复",
            "taskId": list1[0]["tasks"][0]["id"]

        }
    print(url)
    headers ={
        "Authorization":token,
        "Content-Type":"application/json"
    }
    data =data
    print(data)
    data1=json.dumps(data)
    res = requests.post(url=url,headers=headers,data=data1)
    print(res.text)
token=login.access_Token_Login(config.username,config.password)
dealTasks(token)
