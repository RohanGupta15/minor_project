import re
from collections import Counter

def apache_log_reader(logfile):
    myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open("/Users/rohangupta/MEGAsync/Python/logfile.log") as f:
        log = f.read()
        my_iplist = re.findall(myregex,log)
        ipcount = Counter(my_iplist)
        for k, v in ipcount.items():
            print("IP Address " + "=> " + str(k) + " " + "Count "  + "=> " + str(v))

# Create entry point of our code
if __name__ == '__main__':
    apache_log_reader("logfile")



    
