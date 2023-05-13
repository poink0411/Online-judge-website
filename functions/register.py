import os
import shutil
def register_year(year):
    dirs=['./data/']*100
    for i in range(1, 101):
        dirs[i-1] += str(year) + str(i).zfill(3)
        os.mkdir(dirs[i-1])
    print("성공적으로"+str(year)+"학번에 대한 디렉토리를 만들었습니다")
def delete_year(year):
    dirs=['./data/']*100
    for i in range(1, 101):
        dirs[i-1] += str(year) + str(i).zfill(3)
        try:
            shutil.rmtree(dirs[i-1])
        except FileNotFoundError:
            continue
    print("성공적으로"+str(year)+"학번에 대한 디렉토리를 삭제하였습니다")
