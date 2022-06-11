# トラブルが起きたときに確認する方法

- dockerが正しく起動しているかどうかを確認
  - sudo docker
- dockerが正しく起動できていなかった場合に、ログをチェックする方法
  - sudo docker logs --tail 50 --follow --timestamps asana