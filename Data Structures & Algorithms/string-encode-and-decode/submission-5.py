class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = ''
        for s in strs:
            res = res + ','.join(str(ord(ch)) for ch in s) 
            res = res + '*' 

        #print(res)
        return res

    def decode(self, st: str) -> List[str]:
        #print("decode input is " + st)
        if(st == ''): 
            #print("at initial empty" + st)
            return []
        if (st == "" or st == '*'):
            return [""]
        res = []
        word = ''
        wd = ''
        for s in st:
            if s == ',':
                word = word + chr(int(wd))
                #print(wd)
                #print(word)
                wd = ''
                continue
            if s == '*':
                #print("at *" + wd)
                if(wd == ""):
                    #print("at none case" + wd)
                    word = ""
                else:
                    #print ("at generice case" + wd)
                    word = word + chr(int(wd))
                res.append(word)
                #print(word)
                word = ''
                wd = ''
                continue
            wd = wd + s


        #print(res)
        return res

            



