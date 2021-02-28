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
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 0, '2021-2-28 12:00:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 1, '2021-2-28 12:01:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 2, '2021-2-28 12:02:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 3, '2021-2-28 12:03:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 4, '2021-2-28 12:03:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 5, '2021-2-28 12:04:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 6, '2021-2-28 12:04:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 7, '2021-2-28 12:05:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 8, '2021-2-28 12:06:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 9, '2021-2-28 12:07:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 10, '2021-2-28 12:08:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 11, '2021-2-28 12:09:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 12, '2021-2-28 12:10:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 13, '2021-2-28 12:10:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 14, '2021-2-28 12:12:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 15, '2021-2-28 12:14:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 16, '2021-2-28 12:14:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 17, '2021-2-28 12:16:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 18, '2021-2-28 12:20:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 19, '2021-2-28 12:20:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 20, '2021-2-28 12:21:00')")
c.execute("INSERT INTO ImaginaryBusTimeTable VALUES(5, 21, '2021-2-28 12:24:00')")

#テーブルの作成
c.execute('''CREATE TABLE BusStopTable(areaID INTEGER, name TEXT, lat double, lng double)''')
#データの挿入
c.execute("INSERT INTO BusStopTable VALUES (0, '勝田駅前', 36.39510982068315, 140.5253113218038)")
c.execute("INSERT INTO BusStopTable VALUES (1, '常銀前', 36.39489693896063, 140.5274578302311)")
c.execute("INSERT INTO BusStopTable VALUES (2, 'NTT前', 36.395676456995965, 140.5322422271224)")
c.execute("INSERT INTO BusStopTable VALUES (3, 'ひたちなか市役所', 36.395132146692106, 140.53529854193178)")
c.execute("INSERT INTO BusStopTable VALUES (4, '茨交東石川団地', 36.39547201183516, 140.53849289282854)")
c.execute("INSERT INTO BusStopTable VALUES (5, '笹野アパート前', 36.396181686358574, 140.54206501178194)")
c.execute("INSERT INTO BusStopTable VALUES (6, '松戸体育館', 36.39739720317214, 140.54673775041914)")
c.execute("INSERT INTO BusStopTable VALUES (7, '茨城高専前', 36.39837512140571, 140.5521986737155)")
c.execute("INSERT INTO BusStopTable VALUES (8, '中根郵便局前', 36.3984990563152, 140.55607518110133)")
c.execute("INSERT INTO BusStopTable VALUES (9, '本郷台団地入口', 36.398632027179964, 140.5605568413252)")
c.execute("INSERT INTO BusStopTable VALUES (10, '弥生団地', 36.39896153634087, 140.5628335842829)")
c.execute("INSERT INTO BusStopTable VALUES (11, '馬渡宮前', 36.40080063376988, 140.56958482712457)")
c.execute("INSERT INTO BusStopTable VALUES (12, '中宿西', 36.401163361218465, 140.57202327371687)")
c.execute("INSERT INTO BusStopTable VALUES (13, '馬渡十文字', 36.40080208258307, 140.5743553923603)")
c.execute("INSERT INTO BusStopTable VALUES (14, '市民球場入口', 36.40116773076637, 140.58365580362405)")
c.execute("INSERT INTO BusStopTable VALUES (15, 'ジョイフル本田西', 36.40419431893917, 140.58544942514843)")
c.execute("INSERT INTO BusStopTable VALUES (16, 'ジョイフル本田東', 36.40486569134847, 140.58842415042233)")
c.execute("INSERT INTO BusStopTable VALUES (17, '海浜公園西口', 36.401542058434536, 140.59084150909155)")
c.execute("INSERT INTO BusStopTable VALUES (18, '交通公園', 36.39353349015549, 140.59465346486112)")
c.execute("INSERT INTO BusStopTable VALUES (19, '中央研修所', 36.3931509447394, 140.59555328905415)")
c.execute("INSERT INTO BusStopTable VALUES (20, '中央研修所入口', 36.39658260739551, 140.59533650439653)")
c.execute("INSERT INTO BusStopTable VALUES (21, '海浜公園南口', 36.394218026506095, 140.60312737633956)")


c.execute('''CREATE TABLE RealBusTimetable(BusID INTEGER, areaID INTEGER,time TEXT,PersonNum INTEGER)''')
# 挿入した結果を保存（コミット）する
conn.commit()

# データベースへのアクセスが終わったら close する
conn.close()