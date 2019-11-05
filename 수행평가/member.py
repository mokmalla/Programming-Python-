class member:
    def __init__(self):
        self.id = ""
        self.pwd = ""
        self.name = ""

    def setId(self, id):
        print(id)
        if id =="":
            print("tq")
        self.id=id

    def getId(self):
        return self.id

    def setPwd(self, pwd):
        self.pwd= pwd

    def getPwd(self):
        return self.pwd

    def setName(self, name):
        self.id = name

    def getName(self):
        return self.name