class Book():
    def __init__(self,page,name):
        self.name=name
        self.page=int(page)
    def __str__(self):
        return self.name+",active page: "+str(self.page)
    def nextt(self):
        self.page+=1
class Paper(Book):
    def __init__(self,page,name,pages):
        super().__init__(page,name)
        self.pages=int(pages)
    def __str__(self):
        return self.name+",active page: "+str(self.page)+' all pages:'+str(self.pages)
class Ebook(Book):
    def __init__(self,page,name,file):
        super().__init__(page,name)
        self.file=file
    def __str__(self):
        return self.name+",active page: "+str(self.page)+' file:'+self.file

q=Paper(4,"fer",666)
q.nextt()
print(q)
w=Ebook(54,"fgfn er","texr.txt")
w.nextt()
w.nextt()
w.nextt()
print(w)