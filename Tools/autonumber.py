from Tools.file_path import *

class AutoNumber:
    # 昵称序号
    @staticmethod
    def autonumber():
        with open(test_number_path, 'r')as f:
            i = int(f.readline().strip())
        with open(test_number_path, 'w')as f:
            i+=1
            print(i,file=f)
        return i

    # code序号
    @staticmethod
    def tcode():
        with open(test_tcode_path, 'r')as f:
            i = int(f.readline().strip())
        with open(test_tcode_path, 'w')as f:
            i+=1
            print(i,file=f)
        return i