# Asana Alart

## 概要
タスク管理ツールAsanaでタスクの進行に遅れが発生したときに、Slackのその人のチャンネルに通知を行うツール。
トヨタのアンドンのような役割を担ってくれることを期待している。


#### 起動方法
  1. sudo sh restart.sh
#### コンテナの中に入る方法
1. docker-compose exec asana bash 

#### 停止方法
- pythonプログラムを停止したいとき
  1. ps -l でpidを取得
  2. kill 取得したpid
   
- コンテナを停止したいとき
  1. exit
  2. docker-compose rm -fsv asana