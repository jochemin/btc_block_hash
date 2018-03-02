import subprocess
import time

def blocktime(blockhash):
    block_info = subprocess.check_output(['bitcoin-cli','getblock',blockhash])
    for line in block_info.splitlines():
        if "time" in line:
            epoch  = line.split(':',2)
            epoch  = epoch[1].strip()
            epoch  = float(epoch[:-1])
            date = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(epoch))
            return date

def composeline(date,i,block_hash):
    i = str(i)
    line = date+";"+i+";"+block_hash+"\n"
    return line

def to_csv(line):
    f = open("BTC_Blockhash.csv","a")
    f.write(line)
    f.close()

f = open("BTC_Blockhash.csv","w")
f.write("date;number;hash\n")

for i in range(0 , 511591):
    block = str(i)
    block_hash = subprocess.check_output(['bitcoin-cli','getblockhash',block])
    block_hash = block_hash.rstrip()
    date = blocktime(block_hash)
    line = composeline(date, i, block_hash)
    to_csv(line)
