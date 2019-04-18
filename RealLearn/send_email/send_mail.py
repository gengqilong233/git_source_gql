from Commondb import SqlSelectAll
from CommonReadExcle import Write_Excle
import CommonData
import schedule
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
import time

def xiaodan():
    CommonData.environment = '可切换数据库'
    sql = '''select (case c.new_sign when 1 then '新签' when 0 then '续费' end)'是否新签',
    a.name'活动名称', c.signer'乙方(家长姓名)', s.name'学员(学员姓名)',  d.value'年级', (c.period *c.origin_price/100)'学费原价格', 
    (c.period * c.contract_unit_price/100)'学费折后价格',
    c.unit_price_name'课时包类型', '学费折后价格大写', 
    (case c.teacher_level when 1 then '常规' when 2 then '五星' end)'课时类型',
    (select group_concat(sub.subject_name)
        from tms_contract_property tcp
        left join curriculum_plans_property cpp on tcp.property_id = cpp.curr_plan_property_id 
        left join subject sub on sub.subject_id = cpp.subject_id
        where tcp.contract_id  = c.contract_id
        group by c.contract_id)'科目名称（学科）',
    (select group_concat(cp.curr_plan_name)
        from tms_contract_property tcp
        left join curriculum_plans_property cpp on tcp.property_id = cpp.curr_plan_property_id 
        left join curriculum_plans cp on cp.curr_plan_id = cpp.curr_plan_id
        where tcp.contract_id  = c.contract_id
        group by c.contract_id)'购买课程名称',
    (c.period+c.donate_period)'总计课时', c.minute_per_period'课时分钟数',
    (select group_concat(g.name, g.price)
        from tms_contract_activity_gift tcag
        left join tms_gift g on g.id = tcag.gift_id
        where tcag.contract_id = c.contract_id
        group by c.contract_id
        )'活动礼品名称及金额',
    s.student_no'学员编号', c.contract_id'协议编号', group_concat(tcp.pay_date)'付款日期', (c.period * c.contract_unit_price/100)'协议金额',
    group_concat(tcp.sum/100)'付款金额',
    group_concat((case tcp.pay_method_new 
                           when 'haier' then '海尔分期' 
                           when 'kufenqi' then '库分期支付'
                           when 'msh' then '马上花无须凭证'
                           when 'zhongyin' then '中银消费金融'
                           when 'huabei' then '花呗分期'
                           when 'jd' then '京东白条无须凭证'
                           when 'haimi' then '海米管家无须凭证'
                           when 'alishop' then '淘宝'
                           when 'hjzy' then '沪江中银需要凭证'
                           when 'alioffline' then '支付宝未生成链接扫码需要凭证'
                           when 'xingye' then '兴业账户需要凭证'
                           when 'nonghang' then '农行账户需要凭证'
                           when 'hjqk' then '沪江全款需要凭证'
                           when 'weixinoffline' then '微信未生成链接扫码需要凭证'
                           when 'cash' then '现金支付需要凭证'
                           when 'card' then '现场刷卡需要凭证'
                           when 'lebaifen' then '招商银行掌上生活'
                           when 'baidu' then '百度支付无须凭证'
                           when 'ali' then '支付宝无须凭证'
                           when 'wftgp' then '网银支付无需凭证'
                           when 'wftWeixin' then '微信支付无须凭证'
                           when 'yinlianWeixin' then '微信支付无须凭证'
                           when 'yinlianAli' then '支付宝无须凭证'
                           end))'付款方式',
    (c.period * c.contract_unit_price/100)'合计价款', '合计价款大写'
    from view_tms_contract c
    left join view_student s on s.student_intention_id = c.student_intention_id
    left join hls_ddic d on d.code = c.grade
    left join view_tms_sale_activity a on c.activity_id = a.id
    left join view_tms_contract_payment tcp on tcp.contract_id = c.contract_id
    left join view_tms_coupon_usage tcu on c.contract_id = tcu.contract_id
    left join tms_coupon tc on tcu.coupon_id = tc.id
    left join tms_gift tg on tc.donate_gift = tg.id
    where d.type = 'ST009'
    and s.name not like %s
    and s.account_type = 1
    and c.activity_id in(46,45,67,68,69,70)
    and c.status = '3'
    and c.new_sign = 1
    and tcp.pay_status in(4,2)
    group by c.contract_id'''
    result = [('是否新签','活动名称','乙方(家长姓名)',	'学员(学员姓名)','年级','学费原价格', '学费折后价格','课时包类型',
               '学费折后价格大写','课时类型','科目名称（学科）','购买课程名称','总计课时','课时分钟数','活动礼品名称及金额',
               '学员编号','协议编号'	,'付款日期','协议金额','付款金额','付款方式','合计价款','合计价款大写')]
    result = result + SqlSelectAll(sql, ('%'+'测试'+'%'))
    # print(result)
    Write_Excle(r'e:\Desktop\小单组.xlsx',result)

    # host = 'smtp.qq.com', sender = '965456595@qq.com', receiver = '965456595@qq.com', password = 'bmgyvnvwcjhybdce',
    # subject = 'Python send HTML&extra', messag = """
    #                                                 <p>Python send HTML&extra</p>
    #                                                 <p><a href="http://www.baidu.com">这是一个链接</a></p>
    #                                                 """, type = 'html', extra = r'e:\Desktop\线上问题.txt', extra_name = 'ce1.txt'):

    host = 'smtp.qq.com'

    sender = '965456595@qq.com'
    receiver = 'shiyan007766@hfjy.com'
    copy_receiver = 'gengql@hfjy.com,yutongfu@hfjy.com'  # shiyan007766@hfjy.com
    all_receivcer = [receiver] + copy_receiver.split(',')
    password = 'bmgyvnvwcjhybdce'

    now = time.strftime('%Y-%m-%d %H:%M:%S')
    code = 'utf-8'

    message = MIMEMultipart()

    message['From'] = Header('gengql@hfjy.com', 'utf-8')
    message['To'] = Header('shiyan007766@hfjy.com', 'utf-8')
    message['Cc'] = Header('gengql@hfjy.com,yutongfu@hfjy.com')
    message['Subject'] = Header('小单组%s数据'%str(now), code)

    msg = MIMEText('请查收附件，日期：%s' %str(now), 'plain', code)
    extra = MIMEApplication(open(r'e:\Desktop\小单组.xlsx', 'rb').read())
    extra.add_header('Content-Disposition', 'attachment', filename='小单组%s数据.xlsx'%str(now))

    message.attach(msg)
    message.attach(extra)

    try:
        smtpObj = smtplib.SMTP(host, 25)
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, all_receivcer, message.as_string())
        print('发送成功 %s' %str(now))
    except Exception as e:
        print(e)


# xiaodan()

schedule.every(1).days.at('08:00').do(xiaodan)

while True:
    schedule.run_pending()





















# xiaodan()
# print(SqlSelectAll('''
# select name'姓名', student_no'编号' from student where name like %s
# ''', ('%'+'测试'+'%')))

# student_intention_id= %s



