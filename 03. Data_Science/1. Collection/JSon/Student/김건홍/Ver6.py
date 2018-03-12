student_ITT_list = [
    {
        'student_id': 'ITT001',
        'student_name': "홍길동 ",
        'student_age': "30",
        'student_address': "주소",
        'total_course_info':{
            'num_of_course_learned': "빵",
            'learning_course_info':[
                {
                    'course_code': "IB171106",
                    'course_name': "IoT 빅데이터 실무반",
                    'teacher': "이현구",
                    'start_date': "2017-11-06",
                    'finish_date': "2018-09-05"
                }
            ]
        }
    },{
        'student_id': 'ITT002',
        'student_name': "홍길동2 ",
        'student_age': "302",
        'student_address': "주소2",
        'total_course_info':{
            'num_of_course_learned': "빵2",
            'learning_course_info':[
                {
                    'course_code': "IB1711062",
                    'course_name': "IoT 빅데이터 실무반2",
                    'teacher': "이현구2",
                    'start_date': "2017-11-062",
                    'finish_date': "2018-09-052"
                }
            ]
        }
    }
]

print("<학생정보조회>")
for student_data in student_ITT_list:
    print("아이디 : "+student_data['student_id'])
    print("이름 : "+ student_data['student_name'])
    print("나이 : "+ student_data['student_age'])
    print("주소 : "+ student_data['student_address'])
    print("횟수 : "+ student_data['total_course_info']['num_of_course_learned'])
    print("강의코드 : "+ student_data['total_course_info']['learning_course_info'][0]['course_code'])
    print("강의명 : "+ student_data['total_course_info']['learning_course_info'][0]['course_name'])
    print("강사명 : "+ student_data['total_course_info']['learning_course_info'][0]['teacher'])
    print("개강일 : "+ student_data['total_course_info']['learning_course_info'][0]['start_date'])
    print("종료일 : "+ student_data['total_course_info']['learning_course_info'][0]['finish_date'])
    print("=" *50)