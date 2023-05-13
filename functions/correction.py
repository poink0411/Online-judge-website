import subprocess
import sys
import time
import json
def check_correct(prob_number, id):
    flag = 1
    prob_number="1001"
    id="21053"
    with open('./problems/'+prob_number+'/test_case', 'r') as tc:
        with open('./problems/'+prob_number+'/test_case_ans', 'r') as tca:
            ans = tca.read().split('\n\n')
            loc = 0
            for i in tc.read().split('\n\n'):
                p = subprocess.Popen(args=[sys.executable, "./data/"+id+"/ans_code_"+prob_number+".py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                     text=True)
                start=time.time()
                if p.communicate(input=i)[0] == ans[loc]:
                    print(str(loc)+"번째 테스트 케이스에 대해 맞았습니다!")
                else:
                    print(str(loc)+"번째 테스트 케이스에 대해 틀렸습니다!")
                    flag = 0
                end = time.time()
                loc += 1
                p.stdin.close()
    return flag == 1

def add_correct(user, prob_number, correct):
    json_data = {}
    with open('./data/user_info.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    flag = 0
    if correct:
        if int(prob_number) not in json_data[str(user)]['problems_solved']:
            json_data[str(user)]['problems_solved'].append(int(prob_number))
            flag = 1
    else:
        if int(prob_number) not in json_data[str(user)]['problems_failed']:
            json_data[str(user)]['problems_failed'].append(int(prob_number))
            flag = 1
    if flag:
        with open('./data/user_info.json', 'w', encoding='utf-8') as file:
            json.dump(json_data, file, indent=4)
