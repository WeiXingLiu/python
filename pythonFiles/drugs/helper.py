import pymysql
import _thread
import traceback
import time

def removeAdditionString(originString):
    value = ''
    try:
        value = originString.contents[0].strip()
    except Exception:
        return ''
    return value.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')

def connectDB():
    db = pymysql.connect("10.168.3.19","root","Vongi..2017","python" )
    return db

def recordIsExit(id):
    db = connectDB()
    cursor = db.cursor()
    selectSql = 'SELECT * FROM t_test_info WHERE organization_id = "%s"' % id
    try:
        cursor.execute(selectSql)
        results = cursor.fetchall()
    except Exception:
        f = open('error.txt', 'a+')
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        traceback.print_exc(file=f)
        f.flush()
        f.close()
    db.commit()
    cursor.close()
    db.close()
    return len(results) > 0

def deleteTableData():
    db = connectDB()
    cursor = db.cursor()
    baseInfoTable = 'DELETE FROM t_test_info'
    cursor.execute(baseInfoTable)
    organationTable = 'DELETE FROM t_organizations'
    cursor.execute(organationTable)
    enterStandardTable = 'DELETE FROM t_standard_constrain'
    cursor.execute(enterStandardTable)
    refuseStandardTable = 'DELETE FROM t_exclusion_criteria'
    cursor.execute(refuseStandardTable)
    db.commit()
    cursor.close()
    db.close()

def writeDataToDB(detail):
    # 打开数据库连接60.190.233.23 Vongi..2017
    db = connectDB()
    
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    f = open('error.txt', 'a+')

    baseInfoSql = 'INSERT INTO t_test_info (indication, test_popular_title, test_profession_title, scheme_number, drug_name, drug_type, contact, contact_phone, test_end_date, test_status, standard_constrain_id, exclusion_criteria_id, organization_id, search_content_type) VALUES '
    baseInfoData = (detail['indication'], detail['test_popular_title'], detail['test_profession_title'], detail['scheme_number'], detail['drug_name'], detail['drug_type'], detail['contact'], detail['contact_phone'], detail['test_end_date'], detail['test_status'], detail['id'], detail['id'], detail['id'], detail['search_content_type'])  
    # 使用 execute()  方法执行 SQL 查询 

    try:
        baseInfoSqlJoin = '%s%s' % (baseInfoSql, baseInfoData)
        cursor.execute(baseInfoSqlJoin)
        
    except Exception:
        sql = '%s%s' % (baseInfoSql, baseInfoData)
        print(sql)
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        traceback.print_exc(file=f)
        f.flush()

    for index,value in enumerate(detail['organizationLists']):
        sql = 'INSERT INTO t_organizations (organization_id, organization_name, province, city, num) VALUES '
        data = (detail['id'], value['organization_name'], value['province'], value['city'], value['num'])  
        # 使用 execute()  方法执行 SQL 查询 

        try:
            sqlJoin = '%s%s' % (sql, data)
            cursor.execute(sqlJoin)
        except Exception:
            sql = '%s%s' % (sql, data)
            print(sql)
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            traceback.print_exc(file=f)
            f.flush()

    for index,value in enumerate(detail['enterStandrdLists']):

        sql = 'INSERT INTO t_standard_constrain (standard_constrain_id, content, num) VALUES '
        data = (detail['id'], value['content'], value['num'])  

        try:
            sqlJoin = '%s%s' % (sql, data)
            cursor.execute(sqlJoin)
        except Exception:
            sql = '%s%s' % (sql, data)
            print(sql)   
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            traceback.print_exc(file=f)
            f.flush()

    for index,value in enumerate(detail['defuseStandardLists']):
        sql = 'INSERT INTO t_exclusion_criteria (exclusion_criteria_id, content, num) VALUES '
        data = (detail['id'], value['content'], value['num'])  

        try:
            sqlJoin = '%s%s' % (sql, data)
            cursor.execute(sqlJoin)
        except Exception:
            sql = '%s%s' % (baseInfoSql, baseInfoData)
            print(sql)
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            traceback.print_exc(file=f)
            f.flush()

    # 关闭数据库连接
    f.close()
    db.commit()
    cursor.close()
    db.close()