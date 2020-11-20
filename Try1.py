print('输入muti()开始计算嗷\n')

def muti():
    print('欢迎大佬使用本萌新的矩阵乘法计算器，有问题还请多多包含嗷')
    print('')
    print('****************************************************************************')
    print('提示：')
    print('本计算器支持整数与小数，但请务必在相邻的两个数字之间打上空格（想打几个打几个嗷！）')
    print('****************************************************************************') 
    print('')
    print('发不多唆，开始吧！\n')
    left(None, None, None, '第一个')
    
def left(second_matrix, second_hang, second_lie, being_used):
    
    n = input('请先告诉我{0}矩阵有几行叭：'.format(being_used)).strip()
    while not n.isdigit():
        print('请大佬输入一个正整数，重新试试叭')
        n = input('请先告诉我{0}矩阵有几行叭：'.format(being_used)).strip()
    n = int(n)
    i = 1
    first_matrix = []
    while i <= n:
        read_in = input('给爷输入{0}矩阵的第{1}行: '.format(being_used, i))
        start_with_num = read_in.strip()
        num_list = start_with_num.split(' ')
        while '' in num_list:
            num_list.remove('')
        num_list = check_valid(num_list)
        if being_used == '新':
            check_len = second_hang
        elif i == 1:
            check_len = len(num_list)
        while check_len != len(num_list):
            read_in = input('该行长度有误，你他喵是不是傻，长度应该为{0}，气死偶嘞，重新输！：'.format(check_len))
            start_with_num = read_in.strip()
            num_list = start_with_num.split(' ')  
            while '' in num_list:
                num_list.remove('') 
            num_list = check_valid(num_list)
        num_list = list(map(lambda x: float(x), num_list))
        first_matrix.append(num_list)
        i += 1
    
    first_hang = n
    first_lie = check_len
    
    if being_used == '第一个':
        print('哟西，第一个矩阵已经输入完成惹，接下来请输入第二个矩阵叭！')
        right(first_matrix, first_hang, first_lie, '第二个')
    
    if being_used == '新':
        find_result(first_hang,first_lie,second_hang,second_lie, first_matrix, second_matrix)
        
def right(first_matrix, first_hang, first_lie, being_used):
    
    m = first_lie
    j = 1
    second_matrix = []    
    while j <= m:
        read_in = input('给爷输入{0}矩阵的第{1}行：'.format(being_used, j))
        start_with_num = read_in.strip()
        num_list = start_with_num.split(' ')
        while '' in num_list:
            num_list.remove('')
        num_list = check_valid(num_list)
        if j == 1:
            check_len = len(num_list)
        while check_len != len(num_list):
            read_in = input('该行长度有误，你他喵是不是傻，长度应该为{0}，气死偶嘞，重新输！：'.format(check_len))
            start_with_num = read_in.strip()
            num_list = start_with_num.split(' ')  
            while '' in num_list:
                num_list.remove('') 
            num_list = check_valid(num_list)
        num_list = list(map(lambda x: float(x), num_list))
        second_matrix.append(num_list)
        j += 1 
        
        
    second_hang = m
    second_lie = check_len
    
    find_result(first_hang,first_lie,second_hang,second_lie, first_matrix, second_matrix)


def find_result(first_hang, first_lie, second_hang, second_lie, first_matrix, second_matrix):
    
    result = []
    hang1 = 0
    while hang1 < first_hang:
        result_line = []
        lie2 = 0
        result_num = 0
        while lie2 < second_lie:
            result_num = 0
            lie1 = 0
            while lie1 < first_lie:
                result_num += first_matrix[hang1][lie1] * second_matrix[lie1][lie2]
                lie1 += 1
            result_line.append(result_num)
            lie2 += 1
        result.append(result_line)
        hang1 += 1
    
    print('震惊！99%的人都不知道最后的结果居然是它！')
    position_of_row = 0
    while position_of_row < first_hang:
        position_of_element = 0
        while position_of_element < second_lie - 1:
            print(result[position_of_row][position_of_element], end=' ')
            position_of_element += 1
        print(result[position_of_row][position_of_element])
        position_of_row += 1
    
    keep_going = input('大佬还在结果上继续运算嘛？（提示：输入左乘或者右乘继续嗷,输入任何其他的东东就结束了嗷） ')
    if keep_going.strip() == '右乘':
        right(result, first_hang, second_lie, '新')
    elif keep_going.strip() == '左乘':
        left(result, first_hang, second_lie, '新')    
    else:
        print('撒油拉拉，挥挥')

def check_valid(list):
    found = 0
    for i in list:
        try:
            float(i)
            answer = False
        except ValueError:
            answer = True
        if answer and found == 0:
            read_in = input('该行好像混入了什么奇怪的东西，重新输一下叭：')
            found += 1
            start_with_num = read_in.strip()
            num_list = start_with_num.split(' ')  
            while '' in num_list:
                num_list.remove('')
            return check_valid(num_list)
    if found == 0:
        return list
            
            
            
    
            
            
            
    