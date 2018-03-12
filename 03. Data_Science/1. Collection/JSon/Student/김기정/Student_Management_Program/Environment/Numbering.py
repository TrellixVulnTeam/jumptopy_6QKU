import os
def id_generator():
    if not os.path.isfile(os.getcwd() + os_delimeter + count_file):
        with open(os.getcwd() + os_delimeter + count_file, "w") as count:
            count.write("001")

def id_check():
    with open(os.getcwd() + os_delimeter + count_file, "r") as data:
        count_n = data.readline()
        st_ID = "ITT" + count_n
        int_count_n = int("%01d" % int(count_n))
        int_count_n += 1
    with open(os.getcwd() + os_delimeter + count_file, "w") as count:
        three_digit_n = "%03d" % int_count_n
        count.write(three_digit_n)
        return st_ID




now_cwd = os.getcwd()
os_delimeter = "\\"
count_file = "Student_count_number.txt"
json_file_name = "ITT_Student.json"
json_default = {}