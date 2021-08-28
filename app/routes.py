import matplotlib.pyplot as plt
from flask import render_template,request, url_for,flash, redirect
from app import app
from app.frm_entry import EntryForm, EditForm
from app import db
from app.models import Aritmetika_db
from werkzeug.urls import url_parse

@app.route("/")
@app.route("/index")
def index():
    x=[17,16,7,8,9]
    plt.plot(x)
    plt.savefig("app/static/new_plot.png")
    return render_template("index.html",title="Aritmetika",nama_file="new_plot.png")

@app.route("/frm_entry", methods=["GET","POST"])
def frm_entry():
    form=EntryForm()
    xhasil=0
    ket=""
    
    if form.validate_on_submit():
        # Ambil data dari form
        xnilai_1=form.nilai_1.data
        xnilai_2=form.nilai_2.data        
        xoperator=form.operatornya.data        
        
        # Proses perhitungan        
        if xoperator=="+":
            xhasil=int(xnilai_1)+int(xnilai_2)
        elif xoperator=="-":
            xhasil=int(xnilai_1)-int(xnilai_2)
        elif xoperator=="/":
            xhasil=int(xnilai_1)/int(xnilai_2)
        elif xoperator=="*":
            xhasil=int(xnilai_1)*int(xnilai_2)
        else:
            xhasil=0
       
        # Menentukan Ganjil atau Genap
        if xhasil % 2 ==0:
            ket="Genap"
        elif xhasil % 2==1:
            ket="Ganjil"
        else:
            ket="Nol"           
       
        # Simpan ke Database
        simpan=Aritmetika_db(nilai_1=xnilai_1,nilai_2=xnilai_2,operator=xoperator,hasil=xhasil,
                             ket=ket)
        db.session.add(simpan)
        db.session.commit()
        
    return render_template("frm_entry.html",title="Operasi Aritmetika",form=form,xhasil=xhasil,ket=ket)

@app.route("/tampil_data")
def tampil_data():
    hasilnya=Aritmetika_db.query.all()
    return render_template("tampil_data.html",title="Data Operasi Aritmetika",hasilnya=hasilnya,no=1)

@app.route("/edit_data/<id>", methods=["GET","POST"])
def edit_data(id):
    form_edit=Aritmetika_db.query.filter_by(id=id).first()
    znilai_1=form_edit.nilai_1
    znilai_2=form_edit.nilai_2
    zoperator=form_edit.operator
    
    form_editnya=EditForm()    
    
    if form_editnya.validate_on_submit():              
       xoperator=form_editnya.operatornya.data
       xnilai_1=form_editnya.nilai_1.data
       xnilai_2=form_editnya.nilai_2.data
       
       # Proses perhitungan        
       if xoperator=="+":
          xhasil=int (xnilai_1)+int (xnilai_2)
       elif xoperator=="-":
          xhasil=int (xnilai_1)-int (xnilai_2)
       elif xoperator=="/":
          xhasil=int(xnilai_1)/int (xnilai_2)
       elif xoperator=="*":
          xhasil=int (xnilai_1)*int (xnilai_2)
       else:
          xhasil=0
       
       # Menentukan Ganjil atau Genap
       if xhasil % 2 ==0:
          xket="Genap"
       elif xhasil % 2==1:
          xket="Ganjil"
       else:
          xket="Nol"                  
       
       form_edit.nilai_1=form_editnya.nilai_1.data
       form_edit.nilai_2=form_editnya.nilai_2.data
       form_edit.operator=form_editnya.operatornya.data
       form_edit.hasil=xhasil
       form_edit.ket=xket
       db.session.commit()       
       flash("Data berhasil diedit")       
       return redirect(url_for("tampil_data")) 
    elif request.method=="GET":
       form_editnya.nilai_1.data=znilai_1
       form_editnya.nilai_2.data=znilai_2
       form_editnya.operatornya.data=zoperator
    return render_template("frm_edit.html",title="Edit Data",form_edit=form_edit,form_editnya=form_editnya)    

@app.route("/hapus_data/<id>", methods=["GET","POST"])
def hapus_data(id):
    Aritmetika_db.query.filter_by(id=id).delete()    
    db.session.commit()
    flash("Data berhasil diedit")       
    return redirect(url_for("tampil_data")) 