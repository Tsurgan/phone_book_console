import os

def edit_entry(m,f,file_length):
    n=int(m)
    print (n,f[n].replace(';',' '))
    fio,cmp,cmp_nmb,prsn_nmb = f[n].split(';')
    print (fio,cmp,cmp_nmb,prsn_nmb)
    choice=''
    while (choice != 'q')&(choice != 's'):
        choice=input("Выберите часть записи для редактирования:\n 1 - ФИО\n 2 - название компании\n 3 - контактный номер компании\n 4 - личный контактный номер\n s - сохранить\n q - отменить\n  ")
        
        if choice == '1':
            fio = input("Введите ФИО:\n")
            
        elif choice == '2':
            cmp=input("Введите название компании:\n")
            
        elif choice == '3':
            cmp_nmb = input("Введите контактный номер компании:\n")
            while not (cmp_nmb.isdigit()):
                cmp_nmb = input("В номере должны быть только цифры!\nВведите контактный номер компании:\n")
        
        elif choice == '4':
            prsn_nmb = input("Введите личный контактный номер:\n")
            while not (prsn_nmb.isdigit()):
                prsn_nmb = input("В номере должны быть только цифры!\nВведите личный контактный номер:\n")
            
        elif choice == 'q':
            print()
            return
        
        elif choice == 's':
            print()
            
        else:
            print("Некорректный ввод.\n")

    edited_entry = '\n'+fio+';'+cmp+';'+cmp_nmb+';'+prsn_nmb+'\n'     
    temp_file = '\n'.join(f[0:n])+edited_entry+'\n'.join(f[n+1:file_length])
    temp_file=temp_file.strip()
    file = open("tmp_phone_book.csv", "w")
    file.write(temp_file)
    file.close()
    os.remove('phone_book.csv')
    os.rename('tmp_phone_book.csv', 'phone_book.csv')
    print("Изменения сохранены успешно!\n")
    return

def print_page(page_start,p,f,file_length):
    page_end = 0
    if file_length >= page_start+p:
        page_end = page_start+p
    else:
        page_end = file_length
        

    for i in range (page_start,page_end):
        print (i,f[i].replace(';',' '))

    if page_start == 0:
        choice = input("Выберите дальнейшие действия: \n 6 - следующая страница \n 7 - редактировать запись \n q - выход \n")
        if choice == '6':
            print_page(page_start+p,p,f,file_length)
        elif choice == '7':
            id = input("Введите номер записи:\n")
            while (not id.isdigit()):
                id = input("Некорректный номер!\n Введите номер записи:\n")
                
            while (not int(id) in range(0,file_length)):
                id = input("Некорректный номер!\n Введите номер записи:\n")
                
            edit_entry(id,f,file_length)
            
        elif choice == 'q':
            return
        else:
            print("Некорректный ввод.\n")
            print_page(page_start,p,f,file_length)
    elif page_start == (file_length-(file_length%p)):        
        choice=input("Выберите дальнейшие действия: \n 5 - предыдущая страница \n 7 - редактировать запись \n q - выход \n")
        if choice == '5':
            print_page(page_start-p,p,f,file_length)
        elif choice == '7':
            id = input("Введите номер записи:\n")
            while (not id.isdigit()):
                id = input("Некорректный номер!\n Введите номер записи:\n")
                
            while (not int(id) in range(0,file_length)):
                id = input("Некорректный номер!\n Введите номер записи:\n")
                
            edit_entry(id,f,file_length)
            
        elif choice == 'q':
            return
        else:
            print("Некорректный ввод.\n")
            print_page(page_start,p,f,file_length)
    elif page_start == (file_length-p):
        choice=input("Выберите дальнейшие действия: \n 5 - предыдущая страница \n 7 - редактировать запись \n q - выход \n")
        if choice == '5':
            print_page(page_start-p,p,f,file_length)
        elif choice == '7':
            id = input("Введите номер записи:\n")
            while (not id.isdigit()):
                id = input("Некорректный номер!\n Введите номер записи:\n")
                
            while (not int(id) in range(0,file_length)):
                id = input("Некорректный номер!\n Введите номер записи:\n")
                
            edit_entry(id,f,file_length)
            
        elif choice == 'q':
            return
        else:
            print("Некорректный ввод.\n")
            print_page(page_start,p,f,file_length)
    else:
        choice=input("Выберите дальнейшие действия: \n 5 - предыдущая страница \n 6 - следующая страница \n 7 - редактировать запись \n q - выход \n")
        
        if choice == '5':
            print_page(page_start-p,p,f,file_length)
        elif choice == '6':
            print_page(page_start+p,p,f,file_length)
        elif choice == '7':
            id = input("Введите номер записи:\n")
            while (not id.isdigit()):
                id = input("Некорректный номер!\n Введите номер записи:\n")
                
            while (not int(id) in range(0,file_length)):
                id = input("Некорректный номер!\n Введите номер записи:\n")
                
            edit_entry(id,f,file_length)
            
        elif choice == 'q':
            return
        else:
            print("Некорректный ввод.\n")
            print_page(page_start,p,f,file_length)


def print_phone_book(filename,p):
    file=open(filename, "r")
    f = file.read().split('\n')
    file.close()
    file_length = len(f)
    if f[file_length-1] == '':
        f.pop(file_length-1)
        file_length -= 1
    #print(f)
    page_amount=(file_length//p)+1
    page_start=0
    print_page(page_start,p,f,file_length)
    
    return

def add_entry(filename):
    fio = input("Введите ФИО:\n")
    cmp = input("Введите название компании:\n")
    
    cmp_nmb = input("Введите контактный номер компании:\n")
    while not (cmp_nmb.isdigit()):
        cmp_nmb = input("В номере должны быть только цифры!\nВведите контактный номер компании:\n")
        
    prsn_nmb = input("Введите личный контактный номер:\n")
    while not (prsn_nmb.isdigit()):
        prsn_nmb = input("В номере должны быть только цифры!\nВведите личный контактный номер:\n")

    print(fio,cmp,cmp_nmb,prsn_nmb)
    record = fio+';'+cmp+';'+cmp_nmb+';'+prsn_nmb
    file = open(filename, "a")
    file.write(record)
    file.close()
    print("Запись добавлена успешно!\n")
    return

def search(a):
    key_length=len(a)

    file=open(filename, "r")
    f = file.read().split('\n')
    file.close()
    file_length = len(f)
    if f[file_length-1] == '':
        f.pop(file_length-1)
        file_length -= 1

    fio_list = []
    cmp_list = []
    cmp_nmb_list = []
    prsn_nmb_list = []

    f_list=[x.split(';') for x in f]
    f_list_len=len(f_list)
    
    for x in f_list:
        
        fio,cmp,cmp_nmb,prsn_nmb = x
        fio_list.append(fio)
        cmp_list.append(cmp)
        cmp_nmb_list.append(cmp_nmb)
        prsn_nmb_list.append(prsn_nmb)

    search_res=[]
    for i in range (key_length):
        if a[i][0] == 1:
            for j in range(f_list_len):
                if a[i][1] in fio_list[j]:
                    search_res.append(j)

        elif a[i][0] == 2:
            for j in range(f_list_len):
                if a[i][1] in cmp_list[j]:
                    search_res.append(j)

        elif a[i][0] == 3:
            for j in range(f_list_len):
                if a[i][1] in cmp_nmb_list[j]:
                    search_res.append(j)

        elif a[i][0] == 4:
            for j in range(f_list_len):
                if a[i][1] in prsn_nmb_list[j]:
                    search_res.append(j)
            
    
    true_res=[x for x in search_res if search_res.count(x)>=key_length]
    true_res_set=set(true_res)
    true_res=list(true_res_set)
    for i in range(len(true_res)):
        print (true_res[i],f[true_res[i]].replace(';',' '))
    if len(true_res)==0:
        print("Нет результатов\n")

filename = "phone_book.csv"    
choice = ""
while choice != "q":
    choice = input("Выберите дальнейшие действия: \n 1 - просмотреть телефонную книгу \n 2 - добавить запись \n 3 - поиск \n q - выйти\n")
    if choice == '1':
        p = 7
        print_phone_book(filename,p)
    elif choice == '2':
        add_entry(filename)
    elif choice == '3':
        keywords = []
        key = ''
        while key != 'q':
            field = input("Выберите поле для поискового запроса:\n 1 - ФИО\n 2 - название компании\n 3 - контактный номер компании\n 4 - личный контактный номер \n или закончите, нажав q:\n")
            if field == 'q':
                break
            if not field.isdigit():
                print("Некорректное значение!\n")
                continue
            if not int(field) in range (1,5):
                print("Некорректное значение!\n")
                continue
            
            key = input("Введите поисковой запрос или закончите, нажав q:\n")
            if key != 'q':
                keywords.append([int(field),key])
        if len(keywords)>=1:
            search(keywords)
        else:
            print("Нет запроса!\n")
    elif choice == 'q':
        print()
    else:
        print("Некорректный ввод.\n")
