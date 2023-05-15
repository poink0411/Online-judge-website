import json
def valid_login(id, pw):
    with open("./data/user_info.json", 'r', encoding='utf-8') as file:
        data=json.load(file)
        try:
            if data[id]['password']==pw:
                return True
            else: return False
        except KeyError:
            return False