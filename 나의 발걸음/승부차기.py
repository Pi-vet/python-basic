#기본세팅
import random
shooting_location = 0
#shooting_speed = 0
diffence_location = 0
#diffence_speed = 0
shooting_chance = 5
goal = 0

print("승부차기 설명 : 기회는 총 5번으로 공을 찰곳을 선택한다.  \n승부차기 위치 선택\n1 :: 중앙\n2 :: 오른쪽\n3 :: 왼쪽\n 3개의 위치중 공을 찰곳을 선택해 주세요")
while shooting_chance != 0:
    shooting_location = input()
    diffence_location = random.randrange(1, 4)
    if int(shooting_location) == int(diffence_location):
        print("골키퍼가 당신의 공을 훌륭하게 막았습니다.")
        shooting_chance = shooting_chance - 1
    else:
        print("골키퍼가 당신의 공을 막지못하였습니다.")
        goal = goal + 1
        shooting_chance = shooting_chance - 1
print("당신은", goal,"만큼의 공을 넣었습니다.")
    