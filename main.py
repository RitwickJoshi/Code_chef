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
if t<=10:
    k,n = list(map(int,input().split()))

    
    A=list(map(int,input().split()))

    sub_sequence = sub_lists(A,n)

print(sub_sequence)