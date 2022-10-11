import requests
import time
import random

def post_leave_info(vid,skey,date,days,grade):
    arr = date + ' ' + '06:00:00'
    s_t = time.strptime(arr, "%Y-%m-%d %H:%M:%S")
    stampCount = int(time.mktime(s_t))
    for i in range(int(days)):
        cookies = {
            'wwapp.vid': vid,
            'wwoa.h5_approval.skey': skey,
            # 'wwrtx.i18n_lan': 'zh',
            # 'wwapp.cst': '077ECB50D91E1B89AE83598E2528D2C36BD8A6A55266D6EB5203612567A92E3E5CFA4B63C3A3CED4DF6A28B338785927',
            # 'wwapp.deviceid': '21f512b7-5023-41d3-b473-ee55c7640d16',
            # 'wwapp.st': '7C5BCE853F0BA77E76143BF1FB0A68F4796648B08182E5C8DADBA449911171B555A95AE0F8A681231F66EECA826197B8665CE6EC8058B3A89A64CED9EB5ADA5AB05BA0A9E85FD67EE05DC6D59F17D6D6D338EADC3B7364AD65D29D639DF9A873A2DBA97E581F4871BB0CC51554C33062F4E9F9BF1D2B3907BECCEDED103EB02F54ED6958C4FFD7E316644BEF41ADA1B33DF7A16B5CF32223AD2DD3EC5BF3BA33CC9CB7F48AD920BB61430CFEF243DB5C0CE274B5D9BEC21D7CD4E2CF01FF887EE04DCA2558EDDD4F49AC21BEB2DC8FAE5549E0FFC2CBA4BCF89DFC685F496A151A1172D55272BFAA353B540476EA9B2E',
            'wwapp.vid': vid,
            # 'wwapp.corpid': '1970324942121571',
            # 'wwapp.sessionkey': '',
            # 'wwapp.termid': '65538',
            # 'ww_rtkey': '40j1602',
            # 'wwh5.skey': 'nGQ8XmdbCJgGhD_JycSeOTm3qry6FyKHZ4VIo3rsCv9resAFkigCOS5clQLoahNc',
            # 'wwh5.vid': '1688857179397824',
            # 'wwrtx.ltype': '2',
            # 'wwrtx.c_gdpr': '0',
        }

        headers = {
            'Accept': '*/*',
            'Origin': 'https://app.work.weixin.qq.com',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'wwapp.vid=1688857179397824; wwoa.h5_approval.skey=dqcn0MGehxiYVCX75fokPgBxRCOuq_lf293PqUlim02pGEtsn1-iqNsBhwNMZ8cw2NbUYOcH40wCMA4K6HNIgA; wwrtx.i18n_lan=zh; wwapp.cst=40A5754FBB038CD0C103630F081C5F8BC1653DC244489199A2D30C7F99C2271EBA2FA21E83753BF1A37E90C64D1173FB; wwapp.deviceid=21f512b7-5023-41d3-b473-ee55c7640d16; wwapp.st=A004A55537BC928145935E7CE18A90788DFBC7A36F659BBC956C7690094E41B5E6ACEA2D43069CA3867C57C568A8C85510B3168DC91065B25AE3811B71075EC360A998CA757FE75CB1B5915B63567AAEB144F34BFD0EF0270B7480F3B0C247E8CC786DE55959FD51356F88F53C4E1B8A6CE2F8C8E5A1D790B7E1D829934B3BF9149D3526DE6667AD47AFB4E979E880CE66B8841535B70DD2522921CDDF1CBE9D9AFB6BFB90ABA19AE8D80797764E2F547FF0F4948808936D2C53E864ED357A64DA00B8B1A3C297672373391DFF16BB5346515D740837F7B84345379828543DF5F4AA7D83FBF6BC1A48C27C92E6258A08; wwapp.vid=1688857179397824; wwapp.corpid=1970324942121571; wwapp.sessionkey=; wwapp.termid=65538; wwh5.skey=nGQ8XmdbCJgGhD_JycSeOTm3qry6FyKHZ4VIo3rsCv9resAFkigCOS5clQLoahNc; wwh5.vid=1688857179397824; wwrtx.ltype=2; wwrtx.c_gdpr=0',
            # 'Content-Length': '8802',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Host': 'app.work.weixin.qq.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Language/zh ColorScheme/Light DistType/publish wxwork/4.0.16 (MicroMessenger/6.2) WeChat/2.0.4',
            'Referer': 'https://app.work.weixin.qq.com/wework_admin/approval_v3',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }

        params = {
            'lang': 'zh_CN',
            'ajax': '1',
            'f': 'json',
            'random': '107123',
        }

        data = {
            'is_approval_v3': 'true',
            'params': '{"apply_data":{"contents":[{"id":"vacation-1563793073898","control":"Vacation","title":[{"text":"外出类型","lang":"zh_CN"},{"text":"Leave Type","lang":"en"}],"auth":"Modifiable","value":{"vacation":{"selector":{"options":[{"key":2,"value_i18n":[{"text":"事假","lang":"zh_CN"}],"value_org":"事假","value":[{"text":"事假","lang":"zh_CN"}]}],"exp_type":0,"type":"single"},"attendance":{"date_range":{"type":"hour","new_begin":'+str(stampCount+random.randint(-1200,1200))+',"new_end":'+str(stampCount+59400+random.randint(-1200,1200))+',"new_duration":2520,"slice_info":{"real_begin_time":'+str(stampCount+random.randint(-1200,1200))+',"real_end_time":'+str(stampCount+59400+random.randint(-1200,1200))+',"day_items":[{"daytime":1665417600,"time_sections":[],"state":3,"duration":2520}],"state":3,"modify_duration":0,"duration":2520,"user_begin_time":'+str(stampCount+random.randint(-1200,1200))+',"user_end_time":'+str(stampCount+59400+random.randint(-1200,1200))+',"weekend_excluded":false,"extra_time_excluded":false,"new_flag":2}},"slice_info":{"real_begin_time":'+str(stampCount+random.randint(-1200,1200))+',"real_end_time":'+str(stampCount+59400+random.randint(-1200,1200))+',"day_items":[{"daytime":1665417600,"time_sections":[],"state":3,"duration":2520}],"state":3,"modify_duration":0,"duration":2520,"user_begin_time":'+str(stampCount+random.randint(-1200,1200))+',"user_end_time":'+str(stampCount+59400+random.randint(-1200,1200))+',"weekend_excluded":false,"extra_time_excluded":false,"new_flag":2},"type":1}}},"display":1,"hidden":0},{"id":"Tips-1653095388758","control":"Tips","title":[{"text":"说明","lang":"zh_CN"}],"auth":"Modifiable","value":{"tips":[{"text":"学生返校时间不得超过当天22：30，否则视为无效备案。","lang":"zh_CN"}]},"display":1,"hidden":0},{"id":"item-1497581399901","control":"Textarea","title":[{"text":"外出事由","lang":"zh_CN"},{"text":"Leave Reason","lang":"en"}],"auth":"Modifiable","value":{"text":"取件"},"display":1,"hidden":0},{"id":"Selector-1653487773558","control":"Selector","title":[{"text":"外出区域","lang":"zh_CN"}],"auth":"Modifiable","value":{"selector":{"options":[{"key":"option-1653487859452","value":[{"text":"西海岸新区","lang":"zh_CN"}]}],"exp_type":0,"type":"single","op_relations":[]}},"display":1,"hidden":0},{"id":"Text-1653095060798","control":"Text","title":[{"text":"具体地点","lang":"zh_CN"}],"auth":"Modifiable","value":{"text":"'+random.choice(['山科西门','山科北门','山科南门','辛安街道','长江路','香江路','黄河路'])+'"},"display":1,"hidden":0},{"id":"Text-1653095290230","control":"Text","title":[{"text":"交通方式","lang":"zh_CN"}],"auth":"Modifiable","value":{"text":"'+ random.choice(['步行','骑车'])+'"},"display":1,"hidden":0},{"id":"item-1497581426169","control":"File","title":[{"text":"说明附件","lang":"zh_CN"},{"text":"Attachment","lang":"en"}],"auth":"Modifiable","value":{"files":[]},"display":1,"hidden":0},{"id":"Textarea-1653489035124","control":"Textarea","title":[{"text":"说明","lang":"zh_CN"}],"auth":"Modifiable","value":{"text":""},"display":1,"hidden":0}]},"timezone_info":"","choose_party":{"partyid":"1688854328422487","party_name":"'+grade+'级硕士研究生","name":[{"text":"'+grade+'级硕士研究生","lang":"zh_CN"}]},"template_id":"3WK88NxsMpNh89EsQgEs8XVNGTDmukyejBb5vRCB","process_node_list":[{"id":"APPROVAL-bd197-18639","type":"APPROVAL","appro":{"type":"APV_TAG","members":{"vids":[]},"leader":{"order":"LOW_2_HIGH","level":1,"recursive_search_leader":true,"skip_empty_leader":true,"vids":[]},"tag":{"tag_ids":["6755401709074067"],"vids":[]},"self":{"vids":[]},"self_select":{"type":"SELF_SELECT_MULTI","range_type":"UN_LIMITED","vids":[]},"apv_rel":"APV_REL_OR","multi_leader":{"part_order":"UP_2_DOWN","level":1,"vids":[]},"member_with_tag":{"part_order":"DOWN_2_UP","level":1,"vids":[]},"member_control":{"vids":[]},"approver_collection":{"vids":[]},"member_leader":{"order":"LOW_2_HIGH","level":1,"recursive_search_leader":true,"skip_empty_leader":true,"vids":[]},"multi_member_leader":{"part_order":"DOWN_2_UP","level":1,"vids":[]}},"cc":{"leaders":[]},"name":[{"text":"Specified Tag","lang":"en"},{"text":"请假外出学院审批人","lang":"zh_CN"}],"auth_list":[{"id":"vacation-1563793073898","auth":"ViewOnly"},{"id":"item-1497581399901","auth":"ViewOnly"},{"id":"item-1497581426169","auth":"ViewOnly"},{"id":"Tips-1653095388758","auth":"ViewOnly"},{"id":"Text-1653095060798","auth":"ViewOnly"},{"id":"Text-1653095290230","auth":"ViewOnly"},{"id":"Selector-1653487773558","auth":"ViewOnly"},{"id":"Textarea-1653489035124","auth":"ViewOnly"}],"invalid_type":"Invalid_Approver_AutoAgree","self_select_vids":[],"fixed_vids":[],"invalid_string":"未找到审批人，将自动同意","editable":false,"deleteable":false,"addable":false,"self_select_single":false,"relation":"","new_relation":"或签","relation_string":"","orderable":false,"icon_class":"approver","is_type_self_select":false,"appro_type":"APV_TAG","name_string":"请假外出学院审批人","members_data":[{"vid":10000,"name":"审批人为空","avatar":"https://wwcdn.weixin.qq.com/node/wework/xcx/approval/icon-approval-avatar-default.png","reason":"empty","deleteable":false,"from":"server"}],"members_self_select":[],"members_all_data":[{"vid":10000,"name":"审批人为空","avatar":"https://wwcdn.weixin.qq.com/node/wework/xcx/approval/icon-approval-avatar-default.png","reason":"empty","deleteable":false,"from":"server"}],"lowercase_type":"approval"}],"visual_meta":{"feature_flag_edit":true,"is_approver_change":1,"is_notify_change":1}}',
        }

        response = requests.post('https://app.work.weixin.qq.com/wework_admin/approval/api/create_approval', params=params,
                                 cookies=cookies, headers=headers, data=data)


        if response.json()['data']['response']['errcode'] == 0:
            nowDate = time.localtime(stampCount)
            print(time.strftime("%Y-%m-%d",nowDate)+"请假成功！")
        else :
            nowDate = time.localtime(stampCount)
            print(time.strftime("%Y-%m-%d", nowDate) + "请假失败！")

        stampCount = stampCount + 86400 #6：00-22：30要经历59400秒

    print('已通过本服务完成'+str(days)+'天的请假，以防万一，请前往企业微信-"消息"-"审批"处核实')