'''
지금시각은 ?
11시 이전이면 굿모닝
17시 이전이면 굿애프터눈
22시 이전이면 굿이브닝
나머지는 굿나잇
'''
import datetime

now = datetime.datetime.now()

print('현재는', now)
hour = now.hour
print('현재시각은', hour)

if hour < 11:
    print("굿모닝")
elif hour < 17:
    print("굿에프터눈")
elif hour < 22:
    print("굿이브닝")
else:
    print("굿나잇")

print('----------------------------')

print('올해는?',now.year,'년')
print('현자 달은?', now.month,'월')
print('오늘은?',now.day,'일')