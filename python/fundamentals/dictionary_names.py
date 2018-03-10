students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

def just_students(dict):
    for i in range(0, len(dict)):
        # for key in dict[i]:
        print dict[i]['first_name'] + " " + dict[i]['last_name']

# just_students(students)

def more(dict):
    for key, val in dict.items():
        print key
        for i in range(0, len(val)):
            print str(i+1) + " - " +val[i]['first_name']+" "+val[i]['last_name']+" - " +str(len(val[i]['first_name']+val[i]['last_name']))


more(users)