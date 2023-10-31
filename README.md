# Monster-Strike-Gacha-Notify

怪物彈珠抽卡時機Line通知小幫手，<br/>
根據 http://monst-multi.net/Gacha#reload_view 該網站的預報，<br/>
在超絶大チャンス (過去五分鐘，五星抽中機率>25%)時，給予Line Notify通報

# 必要元件
1. docker

# 使用方法
1. terminal or command line 進到專案目錄下
2. 將gacha腳本中 line_token 變數改為自己的 line notify token 
3. build tag 為"gacha:1.0"的 docker image:
```
docker build -t gacha:1.0 .
```
4. 啟動docker
```
docker run -d gacha:1.0
```