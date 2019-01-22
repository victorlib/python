import json


#  在游戏开始读取最高分，在退出时写入最高分
def get_max_score(filename):
    """如果存储了最大分数， 就获取它"""
    try:
        with open(filename) as file_obj:
            num = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return num


def store_max_score(filename, num):
    with open(filename, 'w') as file_obj:
        json.dump(num, file_obj)
