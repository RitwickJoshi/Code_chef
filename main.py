def sub_lists(list1,n):
    sublist = [[]] 
    sub=[]
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            sub=(list1[i],list1[j])
            if list1[i]==list1[j] and len(sub)!=0:
                pass
            elif len(sub)!=0:
                sublist.append(sub)

    return sublist


t = int(input())
final_answer=[]
for _ in range(t):
    if t<=10:
        k,n = list(map(int,input().split()))

        
        A=list(map(int,input().split()))

        sub_sequence = sub_lists(A,n)

    sum_list=[]
    add=0
    for item in range(1,len(sub_sequence)):
        add = 0
        for each in sub_sequence[item]:
            add+=each
        sum_list.append(add)
    final_answer.append(sum_list.index(min(sum_list))+1)
    sum_list.clear()

for each_index in final_answer:
    print(each_index)
