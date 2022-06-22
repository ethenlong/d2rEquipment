#!python3
# -*- coding: utf-8 -*-
"""
本脚本可以获取QQ2018(v9.0)群所有成员详细资料，请根据提示做对应的操作
作者：yinkaisheng@foxmail.com
"""
import os
import sys
import time

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # not required after 'pip install uiautomation'
import uiautomation as auto


def GetPersonDetail():
    detailWindow = auto.WindowControl(searchDepth=1, ClassName='TXGuiFoundation', SubName='的资料')
    details = ''
    for control, depth in auto.WalkControl(detailWindow):
        if isinstance(control, auto.EditControl):
            details += control.Name + control.GetValuePattern().Value + '\n'
    details += '\n' * 2
    detailWindow.Click(-10, 10)
    return details


def main():
    # auto.Logger.WriteLine('请把鼠标放在QQ群聊天窗口中右下角群成员列表中的一个成员上面，3秒后获取\n', auto.ConsoleColor.Cyan, writeToFile=False)
    # time.sleep(3)
    # listItem = auto.ControlFromCursor()
    # print(listItem.ControlType)
    # if listItem.ControlType != auto.ControlType.ListItemControl:
    #     auto.Logger.WriteLine('没有放在群成员上面，程序退出！', auto.ConsoleColor.Cyan, writeToFile=False)
    #     return
    # consoleWindow = auto.GetConsoleWindow()
    # if consoleWindow:
    #     consoleWindow.SetActive()
    # qqWindow = listItem.GetTopLevelControl()
    qqWindow = auto.WindowControl(searchDepth=1, Name='暗黑2重置斗鱼直播拍卖群（天尽头）')
    qqWindow.SetActive()
    for k in range(1, 100):
        print(k)
        for j in range(1, 17):
            qqWindow.SendKey(0x09)  # tab
            time.sleep(0.3)

        qqWindow.SendKey(0x28, 0.1)  # down暗黑2重置版讨论区
        qqWindow.SendKey(0x0D, 0.1)  # enter
        # send keys in edit
        qqWindow.SendKeys('老哥好，来加入暗黑2大家庭吧，点击链接加群：https://jq.qq.com/?_wv=1027&k=HXqsC14c{ENTER}')
        time.sleep(2)
        qqWindow.RightClick(x=170, y=160)
        for i in range(1, 4):
            qqWindow.SendKey(0x28, 0.1)
        qqWindow.SendKey(0x0D, 0.1)
        time.sleep(3)

    # memberList = qqWindow.ListControl(searchDepth=18, Name='成员列表').ListControl(searchDepth=1, Name="")
    # print(memberList.ControlType)
    # for item in memberList.GetChildren()[10:]:
    #     print(item.Name)
    #     person = memberList.ListItemControl(searchDepth=1, Name=item.Name)
    #     time.sleep(1)
    #     item.Click()
    #     time.sleep(0.1)
    #     person.SendKey(0x0D, 0.1)
    #     time.sleep(0.5)
    #     # person.WheelDown()
    #     # time.sleep(0.5)
    #     curTab = qqWindow.TabItemControl(searchDepth=10, Name=item.Name)
    #     curTab.RightClick()
    #     time.sleep(0.5)
    #     for i in range(1, 7):
    #         curTab.SendKey(0x28, 0.1)
    #
    #     curTab.SendKey(0x0D, 0.1)
    #     time.sleep(3)

    # list = listItem.GetParentControl()
    # allListItems = list.GetChildren()
    # for li in allListItems:
    #     auto.Logger.WriteLine(li.Name)
    #     pass
    # auto.Logger.WriteLine('是否获取成员详细信息？按F9继续，F10退出', auto.ConsoleColor.Cyan, writeToFile=False)
    # while True:
    #     if auto.IsKeyPressed(auto.Keys.VK_F9):
    #         break
    #     elif auto.IsKeyPressed(auto.Keys.VK_F10):
    #         return
    #     time.sleep(0.05)
    # auto.Logger.WriteLine('\n3秒后开始获取QQ群成员详细资料，您可以一直按住F10键暂停脚本', auto.ConsoleColor.Cyan, writeToFile=False)
    # time.sleep(3)
    # qqWindow.SetActive()
    # #确保群里第一个成员可见在最上面
    # list.Click()
    # list.SendKeys('{Home}', waitTime = 1)
    # for listItem in allListItems:
    #     if listItem.ControlType == auto.ControlType.ListItemControl:
    #         if auto.IsKeyPressed(auto.Keys.VK_F10):
    #             if consoleWindow:
    #                 consoleWindow.SetActive()
    #             auto.Logger.WriteLine('\n您暂停了脚本，按F9继续\n', auto.ConsoleColor.Cyan, writeToFile=False)
    #             while True:
    #                 if auto.IsKeyPressed(auto.Keys.VK_F9):
    #                     break
    #                 time.sleep(0.05)
    #             qqWindow.SetActive()
    #         listItem.RightClick(waitTime=2)
    #         menu = auto.MenuControl(searchDepth= 1, ClassName = 'TXGuiFoundation')
    #         menuItems = menu.GetChildren()
    #         for menuItem in menuItems:
    #             if menuItem.Name == '查看资料':
    #                 menuItem.Click(40)
    #                 break
    #         auto.Logger.WriteLine(listItem.Name, auto.ConsoleColor.Green)
    #         auto.Logger.WriteLine(GetPersonDetail())
    #         listItem.Click()
    #         auto.SendKeys('{Down}')


if __name__ == '__main__':
    main()
