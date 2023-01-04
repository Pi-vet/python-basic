import random
print("플레이어를 설정해주세요.")
player_Count = input(int())
list_player = []
list_player_01 = []
player_Count_01 = player_Count
player_Count_02 = int(player_Count) - 1
player_Count_03 = int(player_Count) - 1
print("플레이어 수만큼의 이름을 정해주세요\n")#(참고 :: 원활한 게임 플레이를 위해 이름을 두번씩 입력해주십시오.")
for I in range(int(player_Count)):
    l = input(str())
    list_player.append(l)
    list_player_01.append(l)
    #print(list_player)
    player_Count = int(player_Count) - 1
c = random.randrange(0, int(player_Count_01))
seeker = list_player[c]
print("플레이어 설정이 끝났습니다.\n각각의 플레이어가 랜덤으로 숨었습니다.\n술래는", seeker, "입니다.")
Hide_player_place = ['침대', '화장실', '커튼', '에어컨' , '화분']
list_player.remove(seeker)
list_player_01.remove(seeker)
list_player_file = list_player

print(list_player_file)
print("숨을 장소를 고를 기회를 입력하세요.")
player_hide_count = input(int())*2#int(player_Count_03)
#player_hide_count = int(player_hide_count) - 1
a = 0
for I in range(int(player_hide_count)):
    if  a == int(player_Count_01) - 1:
        a = 0
    b = random.randrange(0,4)
    list_player_file[a] = Hide_player_place[b]
    player_hide_count = int(player_hide_count) - 1
    a = int(a) + 1
    #print(list_player)
print("술래는 플레이어가 숨은곳을 골라주세요.\n3 번의 기회가 있습니다.")
print("침대, 화장실, 커튼, 화분, 에어컨")
N = random.randrange(1, 10)
play_Count_1 = 3
hide_grab = player_Count_03
e = 0
print("주의 :: 첫번째 줄에 첫번째 플레이어, 두번째 줄에는 두번째 플레이어입니다.")
while play_Count_1 != 0:
    print("기회가", play_Count_1, "만큼 남아있습니다.")
    if play_Count_1 == 0:
        print("플레이어를 다 잡지 못했습니다.")
        break
    if hide_grab == 0:
        print("플레이어를 다 잡았습니다.")
        break
    seeker_search = input()
    for H in range(player_Count_03):
        if e == player_Count_03:
            e = 0
        if str(seeker_search) == list_player_file[e]:
            print(list_player_01[e], "을/를 잡았습니다.")
            hide_grab = hide_grab - 1
        else:
            print("플레이어를 잡지 못했습니다.")
        e = e + 1
    play_Count_1 = play_Count_1 - 1
#print(list_player_01)