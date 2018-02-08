import re

def check_match(p,file_name):
    m = p.match(file_name)
    if m:
        print(m)

# Step1] 파일명.확장자를 나타내는 정규식
file_name_candidates=["foo.bar","autoexec.bat","sendmail.cf"]

p = re.compile(".*[.].*$")

print("첫번째 정규식 테스트: .*[.].*$")
for file_name in file_name_candidates:
    check_match(p,file_name)

# Step2] 확장자가 bat 파일 제외
p = re.compile(".*[.][^b].*$")
print("\n두번째 정규식 테스트: .*[.][^b].*$")
for file_name in file_name_candidates:
    check_match(p,file_name)

# Step3] 확장자가 bat 파일 제외 두번쨰 시도
p = re.compile(".*[.]([^b]..|.[^a].|..[^t])")
print("\n세번째 정규식 테스트: .*[.]([^b]..|.[^a].|..[^t]")
for file_name in file_name_candidates:
    check_match(p,file_name)

# Step4] 확장자가 bat 파일 제외 세번쨰 시도
p = re.compile(".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)")
print("\n네번째 정규식 테스트: .*[.]([^b]..|.[^a].|..[^t]")
for file_name in file_name_candidates:
    check_match(p,file_name)
