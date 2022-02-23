import pymysql

def connectDB():
    db=pymysql.connect(host="127.0.0.1",user="Linux",password="summit",database="StudentSystem",port=3306,charset="utf8")
    return db

def closeDB(db):
    db.close()
    
def find(db,account,password):
    cursor=db.cursor()
    sql="SELECT * FROM IdentityInformation WHERE account='%s' and password='%s'"%(account,password)
    cursor.execute(sql)
    results=cursor.fetchall()
    return results

def getStudent(db,account):
    cursor=db.cursor()
    sql="SELECT * FROM S WHERE SNO='%s'"%(account)
    cursor.execute(sql)
    results=cursor.fetchall()
    return results

def getStudentScore(db,account):
    cursor=db.cursor()
    sql="SELECT * FROM SC WHERE SNO='%s'"%(account)
    cursor.execute(sql)
    results=cursor.fetchall()
    return results

def getCNAME(db,account):
    cursor=db.cursor()
    sql="SELECT CNAME FROM C WHERE CNO in (SELECT CNO FROM SC WHERE SNO='%s')"%(account)
    cursor.execute(sql)
    results=cursor.fetchall()
    return results

def getName(db,account):
    cursor=db.cursor()
    sql="SELECT SNAME FROM S WHERE SNO ='%s'"%(account)
    cursor.execute(sql)
    results=cursor.fetchall()
    return results[0][0]

def getAvg(db,account):
    cursor=db.cursor()
    sql="SELECT AVG(GRADE) FROM SC WHERE SNO ='%s'"%(account)
    cursor.execute(sql)
    results=cursor.fetchall()
    return results[0][0]

def getTNAME(db,account):
    cursor=db.cursor()
    sql="SELECT TNAME FROM T WHERE TNO in(SELECT TNO FROM C WHERE CNO in (SELECT CNO FROM SC WHERE SNO='%s'))"%(account)
    cursor.execute(sql)
    results=cursor.fetchall()
    return results

def getCredit(db,account):
    cursor=db.cursor()
    sql="SELECT CREDIT FROM C WHERE CNO in (SELECT CNO FROM SC WHERE SNO='%s')"%(account)
    cursor.execute(sql)
    results=cursor.fetchall()
    return results

def getScorebyCNAME(db,lesson):
    cursor=db.cursor()
    sql="select sno,grade from sc where cno in (select cno from c where cname='%s')"%(lesson)
    cursor.execute(sql)
    results=cursor.fetchall()
    return results


def getTnamebyCNAME(db,lesson):
    s=db.cursor()
    sql="select tname from t where tno in(SELECT tno FROM c WHERE cno in (select cno from c where cname='%s'))"%(lesson)
    s.execute(sql)
    results=s.fetchall()
    return results[0][0]

def getGrade(db):
    s=db.cursor()
    sql="select (select c.cname from c where c.cno=sc.cno),avg(grade) from sc group by cno"
    s.execute(sql)
    results=s.fetchall()
    return results

def getCnobyCname(db,lesson):
    s=db.cursor()
    sql="select c.cno from c where c.cname='%s'"%(lesson)
    s.execute(sql)
    results=s.fetchall()
    return results[0][0]

def add(db,sno,cno,grade,point):
    s=db.cursor()
    sql="INSERT INTO SC (sno,cno,grade,point) VALUES ('%s','%s','%s','%s')"%(sno,cno,grade,point)
    s.execute(sql)
    db.commit()
    
def Modify(db,sno,cno,grade,point):
    s=db.cursor()
    sql="update sc set grade='%s',point='%s' where sno='%s' and cno='%s'"%(grade,point,sno,cno)
    s.execute(sql)
    db.commit()
    
def Delete(db,sno,cno):
    s=db.cursor()
    sql="delete from sc where sno='%s' and cno='%s'"%(sno,cno)
    s.execute(sql)
    db.commit()
    
def getStudentTable(db):
    s=db.cursor()
    sql="select *,sno,sno from S"
    s.execute(sql)
    results=s.fetchall()
    return results

def getCount(db):
    s=db.cursor()
    sql="select count(*) from S"
    s.execute(sql)
    results=s.fetchall()
    return results[0][0]

def addstudent(db,s1,s2,s3,s4,s5):
    s=db.cursor()
    sql="INSERT INTO S (sno,sname,sex,age,sdept,fees) VALUES ('%s','%s','%s','%s','%s',0)"%(s1,s2,s3,s4,s5)
    s.execute(sql)
    db.commit()
    
def addnewaccount(db,s1,s2,s3,s4):
    s=db.cursor()
    sql="INSERT INTO IdentityInformation  (account,password,iadentity,name) VALUES ('%s','%s','%s','%s')"%(s1,s2,s3,s4)
    s.execute(sql)
    db.commit()

def deletestudent(db,sno):
    s=db.cursor()
    sql="delete from s where sno='%s'"%(sno)
    s.execute(sql)
    db.commit()
    
def deletenewaccount(db,sno):
    s=db.cursor()
    sql="delete from IdentityInformation where account='%s'"%(sno)
    s.execute(sql)
    db.commit()
    
def getTeacherTable(db):
    s=db.cursor()
    sql="select *,tno,tno from T where tdept is not null"
    s.execute(sql)
    results=s.fetchall()
    return results

def getteacherCount(db):
    s=db.cursor()
    sql="select count(*) from T where tdept is not null"
    s.execute(sql)
    results=s.fetchall()
    return results[0][0]

def addteacher(db,s1,s2,s3,s4):
    s=db.cursor()
    sql="INSERT INTO T (tno,tname,tdept,tclass) VALUES ('%s','%s','%s','%s')"%(s1,s2,s3,s4)
    s.execute(sql)
    db.commit()
    
def deleteteacher(db,sno):
    s=db.cursor()
    sql="delete from t where tno='%s'"%(sno)
    s.execute(sql)
    db.commit()
    
def getClassTable(db):
    s=db.cursor()
    sql="select * from c"
    s.execute(sql)
    results=s.fetchall()
    return results

def getclassCount(db):
    s=db.cursor()
    sql="select count(*) from c"
    s.execute(sql)
    results=s.fetchall()
    return results[0][0]

def addclass(db,s1,s2,s3,s4,s5):
    s=db.cursor()
    sql="INSERT INTO c (cno,cname,credit,cdept,tno) VALUES ('%s','%s','%s','%s','%s')"%(s1,s2,s3,s4,s5)
    s.execute(sql)
    db.commit()
    
def deleteclass(db,cno):
    s=db.cursor()
    sql="delete from c where cno='%s'"%(cno)
    s.execute(sql)
    db.commit()
    
def getcanchoosecourse(db,account):
    s=db.cursor()
    sql="select * from c where cno not in(select cno from sc where grade>=60 and sno='%s')"%(account)
    s.execute(sql)
    results=s.fetchall()
    return results

def pd(db,account):
    s=db.cursor()
    sql="select count(*) from t where tno='%s'"%(account)
    s.execute(sql)
    results=s.fetchall()
    return results[0][0]

def getxk(db,sno):
    s=db.cursor()
    sql="select * from c where cno in (select cno from xk where sno='%s')"%(sno)
    s.execute(sql)
    results=s.fetchall()
    return results
    
def addxk(db,sno,cno):
    s=db.cursor()
    sql="INSERT INTO xk (sno,cno) VALUES ('%s','%s')"%(sno,cno)
    s.execute(sql)
    db.commit()

def getxkCount(db):
    s=db.cursor()
    sql="select count(*) from xk"
    s.execute(sql)
    results=s.fetchall()
    return results[0][0]
    
def deletexk(db,sno,cno):
    s=db.cursor()
    sql="delete from xk where sno='%s' and cno='%s'"%(sno,cno)
    s.execute(sql)
    db.commit()
    
def pdd(db,cno):
    s=db.cursor()
    sql="select count(*) from c where cno='%s'"%(cno)
    s.execute(sql)
    results=s.fetchall()
    return results[0][0]