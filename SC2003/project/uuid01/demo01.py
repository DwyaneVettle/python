# author by Michealzou@126.com
# 2022/5/22 10:33
# 生成uuid
import uuid
def get_uuid():
    get_timestamp_uuid = uuid.uuid1()
    return get_timestamp_uuid

print(get_uuid())
