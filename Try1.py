print('����muti()��ʼ�����\n')

def muti():
    print('��ӭ����ʹ�ñ����µľ���˷��������������⻹��������')
    print('')
    print('****************************************************************************')
    print('��ʾ��')
    print('��������֧��������С����������������ڵ���������֮����Ͽո���򼸸��򼸸�໣���')
    print('****************************************************************************') 
    print('')
    print('������������ʼ�ɣ�\n')
    left(None, None, None, '��һ��')
    
def left(second_matrix, second_hang, second_lie, being_used):
    
    n = input('���ȸ�����{0}�����м��аȣ�'.format(being_used)).strip()
    while not n.isdigit():
        print('���������һ�����������������԰�')
        n = input('���ȸ�����{0}�����м��аȣ�'.format(being_used)).strip()
    n = int(n)
    i = 1
    first_matrix = []
    while i <= n:
        read_in = input('��ү����{0}����ĵ�{1}��: '.format(being_used, i))
        start_with_num = read_in.strip()
        num_list = start_with_num.split(' ')
        while '' in num_list:
            num_list.remove('')
        num_list = check_valid(num_list)
        if being_used == '��':
            check_len = second_hang
        elif i == 1:
            check_len = len(num_list)
        while check_len != len(num_list):
            read_in = input('���г��������������ǲ���ɵ������Ӧ��Ϊ{0}������ż�ϣ������䣡��'.format(check_len))
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
    
    if being_used == '��һ��':
        print('Ӵ������һ�������Ѿ���������ǣ�������������ڶ�������ȣ�')
        right(first_matrix, first_hang, first_lie, '�ڶ���')
    
    if being_used == '��':
        find_result(first_hang,first_lie,second_hang,second_lie, first_matrix, second_matrix)
        
def right(first_matrix, first_hang, first_lie, being_used):
    
    m = first_lie
    j = 1
    second_matrix = []    
    while j <= m:
        read_in = input('��ү����{0}����ĵ�{1}�У�'.format(being_used, j))
        start_with_num = read_in.strip()
        num_list = start_with_num.split(' ')
        while '' in num_list:
            num_list.remove('')
        num_list = check_valid(num_list)
        if j == 1:
            check_len = len(num_list)
        while check_len != len(num_list):
            read_in = input('���г��������������ǲ���ɵ������Ӧ��Ϊ{0}������ż�ϣ������䣡��'.format(check_len))
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
    
    print('�𾪣�99%���˶���֪�����Ľ����Ȼ������')
    position_of_row = 0
    while position_of_row < first_hang:
        position_of_element = 0
        while position_of_element < second_lie - 1:
            print(result[position_of_row][position_of_element], end=' ')
            position_of_element += 1
        print(result[position_of_row][position_of_element])
        position_of_row += 1
    
    keep_going = input('���л��ڽ���ϼ������������ʾ��������˻����ҳ˼����,�����κ������Ķ����ͽ�����໣� ')
    if keep_going.strip() == '�ҳ�':
        right(result, first_hang, second_lie, '��')
    elif keep_going.strip() == '���':
        left(result, first_hang, second_lie, '��')    
    else:
        print('�����������ӻ�')

def check_valid(list):
    found = 0
    for i in list:
        try:
            float(i)
            answer = False
        except ValueError:
            answer = True
        if answer and found == 0:
            read_in = input('���к��������ʲô��ֵĶ�����������һ�°ȣ�')
            found += 1
            start_with_num = read_in.strip()
            num_list = start_with_num.split(' ')  
            while '' in num_list:
                num_list.remove('')
            return check_valid(num_list)
    if found == 0:
        return list
            
            
            
    
            
            
            
    