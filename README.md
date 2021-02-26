# WebIoT
devote for Hizuki...

## 仕様
- http://127.0.0.1:5000/estimate/<BusID> にアクセスで現在地から先の各バス停への到着予想時刻を表示

## テスト
1. BusDB.py を実行
2. Google API keyをmain.py 17行目に設定
3. main.py を実行
4. http://127.0.0.1:5000/AddDB?BusID=5&AreaID=0&time="2021-02-28 12:10:00"&personNum=10 にアクセス
5. http://127.0.0.1:5000/estimate/5 にアクセス

