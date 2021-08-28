from app import db

class Aritmetika_db(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nilai_1=db.Column(db.Integer)
    nilai_2=db.Column(db.Integer)
    operator=db.Column(db.String(5))
    hasil=db.Column(db.Integer)
    ket=db.Column(db.String(20)) 
    
    def __repr__(self):
        return '<Aritmetika_db {}>'.format(self.nilai_1,self.nilai_2)

    