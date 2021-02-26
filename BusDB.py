import sqlite3

# データベースに接続する
conn = sqlite3.connect('Bus.db')
c = conn.cursor()

c.execute("drop table if exists UniqueBusDB")
c.execute("drop table if exists ImaginaryBusTimetable")
c.execute("drop table if exists BusStopTable")
c.execute("drop table if exists RealBusTimetable")
# テーブルの作成
c.execute('''CREATE TABLE UniqueBusDB(Busid INTEGER, area_SquareM REAL,owner TEXT)''')
# データの挿入
c.execute("INSERT INTO UniqueBusDB VALUES (1 ,30, 'owner1')")
c.execute("INSERT INTO UniqueBusDB VALUES (2 ,22.5, 'owner2')")
c.execute("INSERT INTO UniqueBusDB VALUES (3 ,16.8, 'owner3')")


# テーブルの作成
c.execute('''CREATE TABLE ImaginaryBusTimetable(BusID INTEGER, areaID INTEGER,time TEXT)''')
# データの挿入
areaNum=10
BusNum =5
startTime = "2021-2-28 12:"
for Bus in range(BusNum):
    for area in range(areaNum):
        time = 5* area #分のデータ
        Str = "INSERT INTO ImaginaryBusTimetable VALUES(" + str(Bus) + "," + str(area) + ",\"" + startTime +str(time) +":00"+"\")"
        c.execute(Str)
#テスト
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 0, '2021-2-28 12:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 1, '2021-2-28 12:01')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 2, '2021-2-28 12:02')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 3, '2021-2-28 12:03')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 4, '2021-2-28 12:03')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 5, '2021-2-28 12:04')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 6, '2021-2-28 12:04')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 7, '2021-2-28 12:05')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 8, '2021-2-28 12:06')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 9, '2021-2-28 12:07')")

#テーブルの作成
c.execute('''CREATE TABLE BusStopTable(areaID INTEGER, name TEXT)''')
#データの挿入
c.execute("INSERT INTO BusStopTable VALUES (0, '勝田駅前')")
c.execute("INSERT INTO BusStopTable VALUES (1, '常銀前')")
c.execute("INSERT INTO BusStopTable VALUES (2, 'NTT前')")
c.execute("INSERT INTO BusStopTable VALUES (3, 'ひたちなか市役所')")
c.execute("INSERT INTO BusStopTable VALUES (4, '茨交東石川団地')")
c.execute("INSERT INTO BusStopTable VALUES (5, '笹野アパート前')")
c.execute("INSERT INTO BusStopTable VALUES (6, '松戸体育館')")
c.execute("INSERT INTO BusStopTable VALUES (7, '茨城高専前')")
c.execute("INSERT INTO BusStopTable VALUES (8, '中根郵便局前')")
c.execute("INSERT INTO BusStopTable VALUES (9, '本郷台団地入口')")




c.execute('''CREATE TABLE RealBusTimetable(BusID INTEGER, areaID INTEGER,time TEXT,PersonNum INTEGER)''')
# 挿入した結果を保存（コミット）する
conn.commit()

# データベースへのアクセスが終わったら close する
conn.close()