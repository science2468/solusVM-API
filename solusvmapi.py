#The source code author：(https://github.com/frankplus/solusvm-apistatus) has not been updated.
#原作者没有更新，这是更新后的代码。原作者的代码运行后会出现 正则匹配错误，具体就是第31行的match.group（1）无效
import requests
import re
import time

def humanFileSize(size):
    if(size >= 1<<40):
        size = size/(1<<40)
        return '%.2f' % size + ' TiB'
    if(size >= 1<<30):
        size = size/(1<<30)
        return '%.2f' % size + ' GiB'
    if(size >= 1<<20):
        size = size/(1<<20)
        return '%.2f' % size + ' MiB'
    if(size >= 1<<10):
        size = size/(1<<10)
        return '%.2f' % size + ' KiB'
    return '%.2f' % size + ' Bytes'

solusvmapi = {
        'key':"***", #solusvm api key
        'hash':"***", #solusvm api hash
        'action':'info',
        'bw':'true'
        }
r = requests.get('https://nerdvm.racknerd.com/api/client/command.php', params=solusvmapi)
match = re.match(r'<bw>(\d*),(\d*),(\d*),(\d*)<\/bw>', r.text)

total = int(match.group(1))
used = int(match.group(2))
percent = int(match.group(4))

print('  Data usage for this month: '+humanFileSize(used)+' of '+humanFileSize(total)+' used. ('+'%.2f' %percent+' %)')

time.sleep(2) #windows shell sleep 2s
