# Asana Alart

## 操作方法

#### 起動方法
1. このReadmeがあるディレクトリに移動する
2. docker-compose up -d --build

#### コンテナの中に入る方法
1. docker-compose exec asana bash 

#### 停止方法
- pythonプログラムを停止したいとき
  1. ps -l でpidを取得
  2. kill 取得したpid
   
- コンテナを停止したいとき
  1. exit
  2. docker-compose rm -fsv asana