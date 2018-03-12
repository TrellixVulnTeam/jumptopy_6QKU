g_student_id_index=0

a = [
        {'a':'a','b':'b'},
        {'c':'c','d':'d'}
    ]

for ele in a:
    if ele.get('a') == 'a':
        del ele
        print("delete")
print(a)

