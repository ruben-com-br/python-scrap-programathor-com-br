class Vaga:
    def __init__( self, id, nome, url,skills,infos):
        self.id = id
        self.nome = nome
        self.url = url
        self.skills = skills
        self.infos = infos


    def setId(self, id):
        self.id = id

    def setNome(self,nome):
        self.nome = nome

    def setUrl(self, url):
        self.url = url

    def setSkills(self, skills):
        self.skills = skills

    def setInfos(self,infos):
        self.info = infos

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getUrl(self):
        return self.url

    def getSkills(self):
        return self.skills

    def getInfos(self):
        return self.infos
