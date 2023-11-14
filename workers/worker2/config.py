# Broker 與 Backend 設定
broker_url = 'redis://redis:6379/0'
result_backend = 'redis://redis:6379/1'

# 其他設定
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Taipei'
enable_utc = False