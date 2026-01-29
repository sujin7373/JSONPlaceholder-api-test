# Newman 실행 명령어

newman run JSONPlaceholder_API_Test.postman_collection.json \ <br>
  -e JSONPlaceholder_ENV.postman_environment.json \ <br>
  -d post_ids.csv \ <br>
  --reporters cli,htmlextra \ <br>
  --reporter-htmlextra-export report.html <br>