#coding:utf8
#批量判断日志中的IP是否为百度蜘蛛
import socket,re
# print socket.gethostbyaddr('123.125.71.71')
logs=open('20151030.log','r').readlines()
ips={}
for x in logs:
    # print x.strip()
    ip=re.findall('(\d+.\d+.\d+.\d+)',x.strip())[0]
    ips[ip]=0
# print ips
for ip in ips:
    # print ip
    try:
        data=socket.gethostbyaddr(ip)
        # print data
        if "baidu.com" in data[0]:
            print "baiduspider:%s"%ip
        elif "googlebot.coom" in data[0]:
            print "googlebot:%s"%ip
    except:
        print '正常IP'
        pass



