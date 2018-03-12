def print_device_status(device_name,devcie_status):
    print("%s 상태: "%device_name, end="")
    if devcie_status == True : print("작동")
    elif devcie_status == False : print("정지")

def print_window_status(device_name,devcie_status):
    print("%s 상태: "%device_name, end="")
    if devcie_status == True : print("열림")
    elif devcie_status == False : print("닫힘")

