from ORM.Cohorte import *


class LogicaCohorte():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        print ("contructorc")

    def agregarCohorte(self, cohorte):
        self.session.add(cohorte)
        self.session.commit()
        self.session.close()

    def ultimoCohorte(self, id_curso, ano, semestre):
        cohorte = self.session.query(Cohorte).filter_by(id_curso=id_curso, ano=ano, semestre=semestre).all()
        self.session.close()
        return cohorte[len(cohorte) - 1].id_cohorte


'''		
log = LogicaCohorte()
print log.ultimoCohorte(123,3,1)
'''
