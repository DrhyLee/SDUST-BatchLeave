from post_leave_info import post_leave_info
import time
import random

if __name__ == '__main__':
    print('欢迎使用批量请假系统，使用本系统请认真仔细阅读本repository下的readme.md\n使用本系统可能存在的风险请君知晓\n请您先进入企业微信，使用Ctrl+Shift+Command+D(Windows用户Ctrl+Shift+Alt+D)进入开发者模式。\n进入请假界面，右键任意空白位置，进入检查元素，进入存储空间点击左侧Cookie\n并寻找wwapp.vid和wwoa.h5_approval.skey两个值\n')
    vid = input('请首先输入vid:\n')
    skey = input('请输入skey:\n')
    grade = input('请输入你的年级，例如输入 2022 :\n')
    date = input('请输入你想从哪一天开始请假，例如输入 2022-10-12：\n')
    days = input('请输入你想请多少天假(温馨提醒，切勿贪多哦！):\n')
    post_leave_info(vid,skey,date,days,grade)






