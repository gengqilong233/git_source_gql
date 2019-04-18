# from kafka import KafkaConsumer
#
#
# consumer = KafkaConsumer('lessonMessage',bootstrap_servers=['192.168.0.118:9092'])
# for message in consumer:
#     print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,
#                                           message.value))


from pykafka import KafkaClient

client = KafkaClient(hosts='192.168.0.118:9092')
print(client.topics)

topic = client.topics['test']
print(topic)

# 生产者
producer = topic.get_producer()
d  = {"topic":"test",'ceshi':'ceshiaaaaaaaaaa'}

producer.produce(b'ces1221')		#消息类型，表示开始上课}
producer.produce(b'333')
print("22")
producer.produce(b'444')
print('111111')
producer.stop()

# 消费者
consumer = topic.get_simple_consumer()  # .get_balanced_consumer(consumer_group='1', auto_commit_enable=True)
for message in consumer:
    if message is not None:
        print(message.value)


# str({
#             "content": {
#             "studentId ": 641507,	#学生ID
#             "teacherId ": 569063,	#老师ID
#             "planEndTimeStamp": "2018 - 11 - 27 10: 00: 00",	#计划结束时间
#             "startLessonTimeStamp ": "2018 - 11 – 27 08: 30: 10.324",	#实际开始上课时间
#             "lessonPlanId ": 5650236,	#//课程id
#             "planStartTimeStamp ": "2018 - 11 - 27 08: 30: 00", 	#计划开始上课时间
#             "lessonType": 1	#课程类型（1正式课，2试听课，3体验课）
#             },
# 	    "type": "STARTLESSON"}).encode()






