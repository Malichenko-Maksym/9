class Phone():
    def __init__(self,number,num_cont):
        self.number=int(number)
        self.num_cont=int(num_cont)
        self.act_cont=1
    def __str__(self):
        return "phone number: "+str(self.number)+"\nselected contact:"+str(self.act_cont)+"\n"
    def nextt(self):
        if self.act_cont<self.num_cont: self.act_cont+=1
        else: print("no numbers no more(up)")
    def previous(self):
        if self.act_cont>1: self.act_cont-=1
        else: print("no numbers no more(down)")
q=Phone(66456,6)
q.nextt()
q.nextt()
print(q)
q.previous()
print(q)
w=Phone(76866,10)
w.previous()
print(w)