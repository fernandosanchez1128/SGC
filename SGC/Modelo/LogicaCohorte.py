from ORM.Cohorte import *
from sqlalchemy.orm import sessionmaker


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

    def agregarCohorte(self, cohorte):
        self.session.add(cohorte)
        self.session.commit()
        self.session.close()

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


    def ultimoCohorte(self, id_curso, ano, semestre):
        cohortes= self.session.query(Cohorte).filter_by(id_curso=id_curso, ano=ano, semestre=semestre).all()
        self.session.close()
        if not cohortes == []:
            return cohortes[- 1]
        else:
            return None

    def cohorteN(self, id_curso, ano, semestre, N):
        print "N", N
        print "semest", semestre
        cohortes= self.session.query(Cohorte).filter_by(id_curso=id_curso, ano=ano, semestre=semestre).all()
        self.session.close()
        return cohortes[N]


    def numCohortes(self, id_curso, ano, semestre):
        print "semestre ", semestre
        cohortes= self.session.query(Cohorte).filter_by(id_curso=id_curso, ano=ano, semestre=semestre).count()
        self.session.close()
        return cohortes


'''		
log = LogicaCohorte()
print log.ultimoCohorte(123,3,1)
'''
