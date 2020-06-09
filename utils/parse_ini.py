import configparser
import os

# current_path = os.path.dirname(os.path.realpath(__file__))
# print(current_path)
#
# ini_file = os.path.join(current_path, "test.ini")
# print(ini_file)
#
# conf = configparser.ConfigParser() # 生成对象
# conf.read(ini_file, encoding="utf-8") # read读取文件
# ipaddress = conf.get("ip_address", "ip") # get读取section中的option对应的值
# print(ipaddress)

# 封装成类
class ParseINI():
    def parse_ini(self,file, section, option):
        conf = configparser.ConfigParser()
        conf.read(file, encoding="utf-8")
        return conf.get(section, option)

if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_path, "test.ini")
    print(ParseINI.parse_ini(file_path, "ip_address", "ip"))
