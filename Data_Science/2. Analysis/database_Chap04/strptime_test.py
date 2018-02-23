from datetime import datetime, date
input_date="1/20/14"

convert_date=datetime.strptime(input_date,"%m/%d/%y")

print(convert_date)
# dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")