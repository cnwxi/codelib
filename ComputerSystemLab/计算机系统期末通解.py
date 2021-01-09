"""

_|          _|  _|      _|  _|      _|  @Time : 2021.1.9 16:38
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : 计算机系统期末通解
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""
import random

# # 组索引位数，行数，块偏移位数要求
# s = int(input("s="))
# E = int(input("E="))
# b = int(input("b="))
# 命中、替换次数要求
# hits = int(input("hits="))
# evictions = int(input("evictions="))
# # 组访问要求
# sets = int(input("sets="))
# # 学号
# your_id = input("your_id=")

m_count = 0
totle = 0

s = 7
E = 5
b = 4
hits = 17
evictions = 33
sets = 18
your_id = '201826010221'
cmd = None
ls = ['L', 'S']

record_hits = hits
record_eviction = evictions

file_handle = open(your_id + '.trace', mode='w')

if 2 ** s < sets:
    print('没有那么多组')
else:
    tmpS = 0
    tag = 0
    # 完成组访问要求
    for i in range(sets):
        tmpS = i
        if hits > 0:
            cmd = 'M'
            hits -= 1
            m_count += 1
        else:
            cmd = random.choice(ls)
        file_handle.writelines('%s %x,1\n' % (cmd, tmpS << b))
        totle += 1
    tmptag = 1
    tmpS = 0
    # 替换前提：某个组被占满
    for j in range(E - 1):
        if hits > 0:
            cmd = 'M'
            hits -= 1
            m_count += 1
        else:
            cmd = random.choice(ls)
        file_handle.writelines('%s %x,1\n' % (cmd, (tmptag << (b + s)) + (tmpS << b)))
        totle += 1
        tmptag += 1
    # 完成替换和命中任务
    while evictions > 0:
        if hits > 0:
            cmd = 'M'
            hits -= 1
            m_count += 1
        else:
            cmd = random.choice(ls)
        file_handle.writelines('%s %x,1\n' % (cmd, (tmptag << (b + s)) + (tmpS << b)))
        totle += 1
        evictions -= 1
        tmptag += 1
    # 完成剩余的命中要求
    tmptag -= 1
    min_tag = tmptag - (E - 1)
    tmpb = 1
    max_b = 2 ** b - 1
    if hits > 0:
        cmd_M = hits // 2
        cmd_LS = 0
        if hits % 2 != 0:
            cmd_LS = 1
        cmd = 'M'
        for k in range(cmd_M):
            file_handle.writelines('%s %x,1\n' % (cmd, (tmptag << (b + s)) + (tmpS << b) + tmpb))
            m_count += 1
            totle += 1
            tmpb += 1
            if tmpb > max_b:
                tmpb = 0
                if tmptag > min_tag:
                    tmptag -= 1
        cmd = random.choice(ls)
        file_handle.writelines('%s %x,1\n' % (cmd, (tmptag << (b + s)) + (tmpS << b) + tmpb))
        totle += 1
    file_handle.close()
    print('**************************************************')
    print('trace文件生成完毕')
    print('**************************************************')
    print('totle=', totle)
    rate = m_count / totle
    print("m_count/totle=", format(rate, '.2f'), end=' ')

    if rate < 1 / 3:
        miss = sets + E - 1 + record_eviction
        print('< 1/3')
        file_handle = open(your_id + '.txt', mode='w')
        file_handle.writelines('s=%d,E=%d,hits=%d,evictions=%d\n' % (s, E, record_hits, record_eviction))
        file_handle.writelines('要访问%d个组，则至少有%d次（冷）不命中。\n' % (sets, sets))
        file_handle.writelines('存在替换,则有一个组的所有行都要被访问，所以（冷）不命中次数再加%d。\n' % (E - 1))
        file_handle.writelines('每次替换会先出现不命中，总不命中次数增加%d次。\n' % record_eviction)
        file_handle.writelines('一条指令中最多出现1次不命中。所以至少有%d条指令。\n' % miss)
        file_handle.writelines('命中次数为%d少于不命中次数的1/3=%s条。\n' % (record_hits, format(miss / 3, '.1f')))
        file_handle.writelines('M操作最少都有一次命中,所以M操作最多%d条。\n' % record_hits)
        file_handle.writelines('所以无法满足M操作数至少为总操作数的1/3。\n')
        file_handle.close()
        print('**************************************************')
        print('txt文件生成完毕')
        print('**************************************************')
    else:
        print('\n**************************************************')
    print('./scim -s %d -E %d -b %d -t ./%s' % (s, E, b, your_id + '.trace'))
    print('**************************************************')
