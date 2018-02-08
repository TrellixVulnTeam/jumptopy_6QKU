from collections import OrderedDict
from Register import Student_Register
from Register import Class_Register
import json
import os
import sys

os_delimeter = "\\"
st_count = "Student_count_number.txt"
json_file_name = "ITT_Student.json"
key_list = ["이름","나이","주소"]
key_list_2 = ["강의코드","강의명","강사"]