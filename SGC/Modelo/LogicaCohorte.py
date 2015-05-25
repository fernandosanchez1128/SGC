from ORM.Cohorte import *
from ORM.basetest import *

class LogicaCohorte():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        print ("contructorc")

    def agregarCohorte(self, id_curso, ano, semestre):
        coh = Cohorte(id_curso = id_curso, ano = ano, semestre = semestre)
        self.session.add(coh)
        self.session.commit()
        self.session.close()

<<<<<<< .merge_file_SGzaGm
=======
    def consulta_cohorte (self,id_curso,id_cohorte):
        cohorte = self.session.query(Cohorte).filter_by(id_curso=id_curso,id_cohorte = id_cohorte).first()
        self.session.close()
        return cohorte

    def modificar_cohorte(self, id_curso,id_cohorte,fecha_inicio,fecha_fin):
        exito = 1
        try:
            cohorte= self.session.query(Cohorte).filter_by(id_curso=id_curso,id_cohorte=id_cohorte).first()
            cohorte.fecha_inicio = fecha_inicio
            cohorte.fecha_fin = fecha_fin
            self.session.commit()
            self.session.close()
        except Exception:
            exito = 0
        return exito


>>>>>>> .merge_file_iItRPm
    def ultimoCohorte(self, id_curso, ano, semestre):
        cohortes= self.session.query(Cohorte).filter_by(id_curso=id_curso, ano=ano, semestre=semestre).all()
        self.session.close()
        if not cohortes == []:
            return cohortes[- 1]
        else:
            return None

    def cohorteN(self, id_curso, ano, semestre, N):
        print "N", N
        cohortes= self.session.query(Cohorte).filter_by(id_curso=id_curso, ano=ano, semestre=semestre).all()
        self.session.close()
        return cohortes[N]

    def numCohortes(self, id_curso, ano, semestre):
        cohortes= self.session.query(Cohorte).filter_by(id_curso=id_curso, ano=ano, semestre=semestre).count()
        self.session.close()
        return cohortes

'''
coh = Cohorte(id_curso = 4, ano = 2015, semestre = 2)
lc= LogicaCohorte()
lc.agregarCohorte(coh )
'''
