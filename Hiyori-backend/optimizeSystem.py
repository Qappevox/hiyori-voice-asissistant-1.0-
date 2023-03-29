import os
class Optimizer():
    def optimizeSys(self):
        flag = False
        tmp = os.listdir()
        for i in tmp:
            #check file
            if "audio-" in i and ".mp3" in i:
                flag = True
                os.remove(i)
                print("[-] {0} removed\n".format(i))
                
        if flag == False:
            print("[+] system already optimized...\n from optimizeSystem.py\n")
        else:
            print("[+] system has been optimized...\n from optimizeSystem.py\n")
optimizer = Optimizer()
