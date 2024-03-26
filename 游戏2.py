import pygame
import random
import math

pygame.init()
# print()
img_fish = pygame.image.load("ima\小书1.png")
img_small = pygame.image.load("ima\小书2.png")
img_middle1 = pygame.image.load("ima\中书1.png")
img_middle2 = pygame.image.load("ima\中书2.png")
img_big1 = pygame.image.load("ima\大书1.png")
img_big2 = pygame.image.load("ima\大书2.png")
img_shark = pygame.image.load("ima\Boss书.png")
img_fight = pygame.image.load("ima\医生.png")

img_yinger = pygame.image.load("ima\婴儿.png")
img_xiaoxue = pygame.image.load("ima\小学生.png")
img_zhongxue = pygame.image.load("ima\高中生.png")
img_daxue = pygame.image.load("ima\大学生.png")

img_red1 = pygame.image.load("ima\红怪1.png")
img_red2 = pygame.image.load("ima\红怪2.png")
img_yellow1 = pygame.image.load("ima\黄怪1.png")
img_yellow2 = pygame.image.load("ima\黄怪2.png")
img_green1 = pygame.image.load("ima\绿怪1.png")
img_green2 = pygame.image.load("ima\绿怪2.png")

img_boss = pygame.image.load("ima\Boss.png")
# 载入所需图片

new_boss = pygame.transform.rotozoom(img_boss, 0, 0.3)

new_red11 = pygame.transform.rotozoom(img_red1, 0, 0.5)
new_red12 = pygame.transform.flip(new_red11, 1,0)
new_red21 = pygame.transform.rotozoom(img_red2, 0, 0.5)
new_red22 = pygame.transform.flip(new_red21, 1,0)

new_yellow11 = pygame.transform.rotozoom(img_yellow1, 0, 0.5)
new_yellow12 = pygame.transform.flip(new_yellow11, 1,0)
new_yellow21 = pygame.transform.rotozoom(img_yellow2, 0, 0.5)
new_yellow22 = pygame.transform.flip(new_yellow21, 1,0)

new_green11 = pygame.transform.rotozoom(img_green1, 0, 0.5)
new_green12 = pygame.transform.flip(new_green11, 1,0)
new_green21 = pygame.transform.rotozoom(img_green1, 0, 0.5)
new_green22 = pygame.transform.flip(new_green21, 1,0)

new_yinger1 = pygame.transform.rotozoom(img_yinger, 0, 0.3)
new_yinger2 = pygame.transform.flip(new_yinger1, 1,0)

new_xiaoxue1 = pygame.transform.rotozoom(img_xiaoxue, 0, 0.3)
new_xiaoxue2 = pygame.transform.flip(new_xiaoxue1, 1,0)

new_zhongxue1 = pygame.transform.rotozoom(img_zhongxue, 0, 0.3)
new_zhongxue2= pygame.transform.flip(new_zhongxue1, 1,0)

new_daxue1 = pygame.transform.rotozoom(img_daxue, 0, 0.3)
new_daxue2 = pygame.transform.flip(new_daxue1, 1,0)

new_yishen1 = pygame.transform.rotozoom(img_fight, 0, 0.3)
new_yishen2 = pygame.transform.flip(new_yishen1, 1,0)
new_small1 = pygame.transform.rotozoom(img_small, 0, 0.18)
new_small2 = pygame.transform.rotozoom(img_small, 0,0.18)

new_middle11 = pygame.transform.rotozoom(img_middle1, 0, 0.15)
new_middle12 = pygame.transform.flip(new_middle11, 1,0)


new_middle21 = pygame.transform.rotozoom(img_middle2, 0, 0.15)
new_middle22 = pygame.transform.flip(new_middle21, 1, 0)

new_big11 = pygame.transform.rotozoom(img_big1, 0, 0.3)
new_big12 = pygame.transform.flip(new_big11, 1, 0)

new_big21 = pygame.transform.rotozoom(img_big2, 0, 0.3)
new_big22 = pygame.transform.flip(new_big21, 1, 0)

new_shark1 = pygame.transform.rotozoom(img_shark, 0, 0.4)
new_shark2 = pygame.transform.flip(new_shark1, 1, 0)

# 转换图片大小方向，1是向左，2是向右边


background1 = pygame.image.load("ima\学习背景5.jpeg")
background1 = pygame.transform.rotozoom(background1, 0, 2)
background2 = pygame.image.load("ima\病毒环境2.jpeg")
background2 = pygame.transform.rotozoom(background2, 0, 2)
# 背景图片放缩

win_music = pygame.mixer.Sound("ima\胜利音乐.wav")
eat_music = pygame.mixer.Sound('ima\吃书1.wav')
up_music = pygame.mixer.Sound('ima\升级2.wav')
over_music = pygame.mixer.Sound('ima\游戏结束音乐.wav')
shot_music = pygame.mixer.Sound('ima\射击声音.wav')
enemies_die = pygame.mixer.Sound('ima\小怪死亡.wav')
boss_die_music = pygame.mixer.Sound("ima\Boss死亡.wav")
# 载入音乐

screen = pygame.display.set_mode((1600, 900), flags=pygame.RESIZABLE)
pygame.display.set_caption("game")
clock = pygame.time.Clock()
time_i = 0
time_d = 0

red_bullet = 0
green_bullet = 0
fish_list = []
npc_fish = []
virus_list = []
npc_virus =[]
angle_move = 300
v_boss_x = -2
v_boss_y = -2


player_x = 300
player_y = 200
sp = (player_x,player_y)
eat_number = 0
change = 0
green_number = 0
yellow_number = 0
red_number = 0
virus_life = 2
boss_life = 10
boss_life1 = 10
v_boss = 10
boss_x = 1000
boss_y = 800

v_small = 5
v_middle = 4
v_big = 3
v_shark = 2
v_playerx = 0
v_playery = 0
n = 0
level = 0
# pai =3.1415

bullets = []
bullets1 = []
is_over = False
is_win = False
boss_show = False
overtime = 0
musictime = 0
pygame.mixer.music.load('ima\学习音乐.mp3')
pygame.mixer.music.play(-1)
# 游戏基本参数设置

class Bullet():
    def __init__(self):
        # 以 类.img表示插入敌人图片
        self.img = pygame.image.load('ima\子弹.png')
        self.img = pygame.transform.rotozoom(self.img, 0, 0.5)
        # 定义子弹的坐标，以玩家坐标为基准，使得子弹x坐标与其一样，y坐标比他高一点
        self.x = player_x + 30
        self.y = player_y + 25
        # 子弹移动的速度
        self.step = 15
# 创建第一种子弹类
class Bullet1():
    def __init__(self):
        # 以 类.img表示插入敌人图片
        self.img = pygame.image.load('ima\子弹1.png')
        self.img = pygame.transform.rotozoom(self.img, 0, 0.5)
        # 定义子弹的坐标，以玩家坐标为基准，使得子弹x坐标与其一样，y坐标比他高一点
        self.x = player_x + 30
        self.y = player_y + 25
        # 子弹移动的速度
        self.step = 15
# 创建第二种子弹类
fonts = pygame.font.Font('freesansbold.ttf',150)
# 字体
def check_is_over():
    global is_over
    if is_over:
        text = "Game Over"
        # 用该函数给某一变量赋一个渲染值，fonts(之前定义的字体类型).render(渲染文本 ，True(表示用三色法表示颜色)，(x,y,z)(添加颜色值))
        render = fonts.render(text, True, (255, 0, 0))
        # 此时上述render表示可看作一个可变的图像，可由如下函数插入，当作为背景图片
        screen.blit(render, (400, 400))
        pygame.mixer.music.stop()
# 检查游戏是否结束（角色是否死亡的函数）

def check_is_win():
    global is_win
    if is_win:
        text = "victory!"
        # 用该函数给某一变量赋一个渲染值，fonts(之前定义的字体类型).render(渲染文本 ，True(表示用三色法表示颜色)，(x,y,z)(添加颜色值))
        render = fonts.render(text, True, (255, 240, 27))
        # 此时上述render表示可看作一个可变的图像，可由如下函数插入，当作为背景图片
        screen.blit(render, (400, 400))
        pygame.mixer.music.stop()
# 检查是否胜利的函数

font = pygame.font.Font('freesansbold.ttf', 20)
def show_bullet_number():
    global red_bullet
    global green_bullet
    # 在字符串前加f表示字符串可放入变量，在变量外需加{}来表示其是嵌入变量
    text = f"bullet red:{red_bullet}"
    text1 = f"bullet green:{green_bullet}"
    # 用该函数给某一变量赋一个渲染值，font(之前定义的字体类型).render(渲染文本 ，True(表示用三色法表示颜色)，(x,y,z)(添加颜色值))
    score_render = font.render(text, True, (255 , 0 , 0))
    score_render1 = font.render(text1, True, (255, 255, 0))
    # 此时上述score_render表示可看作一个可变的图像，可由如下函数插入，当作为背景图片
    screen.blit(score_render, (10, 10))
    screen.blit(score_render1,(10, 30))

def show_bullets():
    # 循环全部列表中子弹
    for b in bullets:
        # 第n词循环中子弹的位置
        angle = math.atan(b[1]/b[2])*180/math.pi
        bullet_img = pygame.transform.rotozoom(b[0].img, angle + 180, 1)
        screen.blit(bullet_img, (b[0].x, b[0].y))
        b[0].y = b[0].y + 10*b[2]
        b[0].x = b[0].x + 10*b[1]
        # 如果子弹抛出屏幕，则将该子弹从子弹列表中移除
        if b[0].y < 0 or b[0].x < 0 or b[0].y > 2000 or b[0].x > 2000:
            try:
                bullets.remove(b)
            except:
                continue
# 将子弹展示在屏幕上的函数
def show_bullets1():
    # 循环全部列表中子弹
    for b in bullets1:
        # 第n词循环中子弹的位置
        angle = math.atan(b[1]/b[2])*180/math.pi
        bullet_img = pygame.transform.rotozoom(b[0].img, angle + 180, 1)
        screen.blit(bullet_img, (b[0].x, b[0].y))
        b[0].y = b[0].y + 10*b[2]
        b[0].x = b[0].x + 10*b[1]
        # 如果子弹抛出屏幕，则将该子弹从子弹列表中移除
        if b[0].y < 0 or b[0].x < 0 or b[0].y > 2000 or b[0].x > 2000:
            try:
                bullets1.remove(b)
            except:
                continue
# 第二种子弹，同上


# 下面是游戏主循环，这个循环会一直持续直到游戏结束，每1毫秒循环一次
while True:
    if is_over:
        v_small = 5
        v_middle = 4
        v_big = 3
        v_shark = 2
    # 各种大小书的速度

    if eat_number <= 4:
        if change == 0:
            new_fish = new_yinger1
        else:
            new_fish = new_yinger2
    elif eat_number <= 20:
        if change == 0:
            new_fish = new_xiaoxue1
        else:
            new_fish = new_xiaoxue2
    elif eat_number <= 84:
        if change == 0:
            new_fish = new_zhongxue1
        else:
            new_fish = new_zhongxue2
    elif eat_number <= 148:
        if change == 0:
            new_fish = new_daxue1
        else:
            new_fish = new_daxue2
    elif eat_number <= 212:
        level = 1
        if level == 1 and musictime == 0:
            pygame.mixer.music.load('战斗音乐.mp3')
            pygame.mixer.music.play(-1)
            musictime = 1
        if change == 0:
            new_fish = new_yishen1
        else:
            new_fish = new_yishen2
    # 通过吃书获得的经验值，来改变角色的样貌

    keys = pygame.key.get_pressed()
    clock.tick_busy_loop(60)
    time_i = time_i + 1
    if level == 0:
        screen.blit(background1, (0, 0))
    else:
        screen.blit(background2, (0, 0))
    # 画上背景图片，第一关和第二关




    v1 = 0
    v2 = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
        if event.type == pygame.KEYDOWN:

            # if event.key == pygame.K_w:
            #     bullets.append(Bullet())
            if event.key == pygame.K_c:
                pygame.display.quit()
            if event.key == pygame.K_w:
                v_playery = -11
            if event.key == pygame.K_s:
                v_playery = 11
            if event.key == pygame.K_a:
                change = 0
                v_playerx = -11
            if event.key == pygame.K_d:
                change =1
                v_playerx = 11
    # 按wasd改变人物速度 change表示朝向
        # 转头
        if event.type == pygame.MOUSEMOTION:
            distance1 = math.sqrt((event.pos[0]-player_x) * (event.pos[0]-player_x) + (event.pos[1]-player_y) * (event.pos[1]-player_y))
            sin = (event.pos[0]-player_x)/distance1
            cos = (event.pos[1]-player_y)/distance1
        # 鼠标事件，算出鼠标和人的距离从而算出与水平方向夹角

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and level == 1 and red_bullet > 0:
                shot_music.play()
                bullets.append([Bullet(), sin, cos])
                red_bullet = red_bullet - 1
            # 当在第二关时 红子弹数大于0 鼠标左键会像子弹列表中添加一子弹，并减少一子弹数量
            if event.button == 3 and level == 1 and green_bullet > 0:
                shot_music.play()
                bullets1.append([Bullet1(), sin, cos])
                green_bullet = green_bullet - 1
            # 同上只不过是绿色

    if level == 1:
        show_bullets1()
        show_bullets()
        n = 1
    # 如果是第二关，调用函数显示子弹

    if is_over == False and is_win == False and player_x <= 1600 and player_x >= 0 and player_y >= 0and player_y <= 900:
        player_x = player_x + v_playerx
        player_y = player_y + v_playery
    if player_x <=0:
        player_x =0
    if player_x >=1600:
        player_x =1600
    if player_y <= 0:
        player_y = 0
    if player_y >= 900:
        player_y = 900
    # 防止人物超出地图
    # 下面是生成怪
    if time_i % 100 == 0 and level == 0:
        ram_num1 = random.randint(0, 1)
        ram_num2 = random.randint(1, 20)
        if ram_num1 == 1:
            # 随机方向出现 1
            npc_fish.append("left")
        else:
            npc_fish.append("right")
        if ram_num2 == 1:
            # 品种 2
            npc_fish.append("shark")
        elif ram_num2 >= 2 and ram_num2 <= 3:
            npc_fish.append("big1")
        elif ram_num2 >= 4 and ram_num2 <= 5:
            npc_fish.append("big2")
        elif ram_num2 >= 6 and ram_num2 <= 8:
            npc_fish.append("middle1")
        elif ram_num2 >= 9 and ram_num2 <= 11:
            npc_fish.append("middle2")
        else:
            npc_fish.append("small")
        if npc_fish[0] == "left":
            npc_fish.append(random.randint(800, 1600))
        else:
            npc_fish.append(random.randint(0, 800))
        npc_fish.append(random.randint(0, 800))
        fish_list.append(npc_fish)
        # print(npc_fish)
        npc_fish = []
    # fish_list的每一个元素中载入了鱼各种属性，朝向，生成位置

    if is_over == False and level == 0:
        for fish in fish_list:
            player_rect = new_fish.get_rect()
            player_rect.x = player_x
            player_rect.y = player_y
            if fish[1] == "small":
                # 怪的种类
                v_e = 8
                # 怪的速度
                if fish[0] == "left":
                    rect = new_small1.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    # 怪的半径
                    screen.blit(new_small1, (fish[2], fish[3]))
                    # 画出怪
                else:
                    rect = new_small2.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_small2, (fish[2], fish[3]))
                # 同上
                juli = math.sqrt(
                    (rect.centerx - player_rect.centerx) * (rect.centerx - player_rect.centerx) + (
                            rect.centery - player_rect.centery) * (
                            rect.centery - player_rect.centery))
                # 算出角色与怪的距离
                if juli <= min_distance * 0.3 and level == 0:
                    # 如果距离小于0.4倍的鱼的半径，且在第一关
                    if eat_number == 4 or eat_number == 8 or eat_number == 12 or eat_number == 16:
                        # 如果经验值等于升级的挡位，发出一下升级的声音
                        up_music.play()
                    eat_music.play()
                    # 吃怪声音
                    fish_list.remove(fish)
                    # 然后吃掉怪，把怪从列表中移除
                    eat_number = eat_number + 1
                    # 吃怪经验增加，每种怪不一样
                    red_bullet= red_bullet + 2
                    # 子弹增加
            if fish[1] == "middle1":
                v_e = 3
                if fish[0] == "left":
                    rect = new_middle11.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_middle11, (fish[2], fish[3]))
                else:
                    rect = new_middle12.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_middle12, (fish[2], fish[3]))
                juli = math.sqrt(
                    (rect.centerx - player_rect.centerx) * (rect.centerx - player_rect.centerx) + (
                                rect.centery - player_rect.centery) * (
                            rect.centery - player_rect.centery))
                if juli <= min_distance * 0.4 and eat_number > 4 and level == 0:
                    if eat_number == 4 or eat_number == 20 or eat_number == 84 or eat_number == 148:
                        up_music.play()
                    eat_music.play()
                    fish_list.remove(fish)
                    eat_number = eat_number + 4
                    red_bullet = red_bullet + 5
                elif juli <= min_distance * 0.4 and eat_number < 4 and level == 0:
                    # 如果经验值不够，即等级不够，被大的怪碰到，就直接game over！
                    is_over = True
            if fish[1] == "middle2":
                v_e = 3
                if fish[0] == "left":
                    rect = new_middle21.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_middle21, (fish[2], fish[3]))
                else:
                    rect = new_middle22.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_middle22, (fish[2], fish[3]))
                juli = math.sqrt(
                    (rect.centerx - player_rect.centerx) * (rect.centerx - player_rect.centerx) + (
                                rect.centery - player_rect.centery) * (
                            rect.centery - player_rect.centery))
                if juli <= min_distance * 0.4 and eat_number > 4 and level == 0:
                    if eat_number == 4 or eat_number == 20 or eat_number == 84 or eat_number == 148:
                        up_music.play()
                    eat_music.play()
                    fish_list.remove(fish)
                    eat_number = eat_number + 4
                    green_bullet = green_bullet
                elif juli <= min_distance * 0.4 and eat_number < 4 and level == 0:
                    is_over = True
            if fish[1] == "big1":
                v_e = 2
                if fish[0] == "left":
                    rect = new_big11.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_big11, (fish[2], fish[3]))
                else:
                    rect = new_big12.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_big12, (fish[2], fish[3]))
                juli = math.sqrt(
                    (rect.centerx - player_rect.centerx) * (rect.centerx - player_rect.centerx) + (
                                rect.centery - player_rect.centery) * (
                            rect.centery - player_rect.centery))
                if juli <= min_distance * 0.4 and eat_number > 8 and level == 0:
                    if eat_number == 4 or eat_number == 20 or eat_number == 84 or eat_number == 148:
                        up_music.play()
                    eat_music.play()
                    fish_list.remove(fish)
                    eat_number = eat_number + 16
                    red_bullet = red_bullet + 10
                elif juli <= min_distance * 0.4 and eat_number < 8 and level == 0:
                    is_over = True
            if fish[1] == "big2":
                v_e = 2
                if fish[0] == "left":
                    rect = new_big21.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_big21, (fish[2], fish[3]))
                else:
                    rect = new_big22.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_big22, (fish[2], fish[3]))
                juli = math.sqrt(
                    (rect.centerx - player_rect.centerx) * (rect.centerx - player_rect.centerx) + (
                                rect.centery - player_rect.centery) * (
                            rect.centery - player_rect.centery))
                if juli <= min_distance * 0.4 and eat_number > 8 and level == 0:
                    if eat_number == 4 or eat_number == 20 or eat_number == 84 or eat_number == 148:
                        up_music.play()
                    eat_music.play()
                    fish_list.remove(fish)
                    eat_number = eat_number + 16
                    green_bullet = green_bullet + 10
                elif juli <= min_distance * 0.4 and eat_number < 8 and level == 0:
                    is_over = True
            if fish[1] == "shark":
                v_e = 1
                if fish[0] == "left":
                    rect = new_shark1.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_shark1, (fish[2], fish[3]))
                else:
                    rect = new_shark2.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_shark2, (fish[2], fish[3]))
                juli = math.sqrt(
                    (rect.centerx - player_rect.centerx) * (rect.centerx - player_rect.centerx) + (
                                rect.centery - player_rect.centery) * (
                            rect.centery - player_rect.centery))
                if juli <= min_distance * 0.4 and eat_number > 12 and level == 0:
                    if eat_number == 4 or eat_number == 20 or eat_number == 84 or eat_number == 148:
                        up_music.play()
                    eat_music.play()
                    fish_list.remove(fish)
                    eat_number = eat_number + 64
                    green_bullet = green_bullet +20
                elif juli <= min_distance * 0.4 and eat_number < 12 and level == 0:
                    is_over = True

            if fish[0] == "left":
                fish[2] = fish[2] - v_e
                if fish[2] == 1600:
                    fish_list.remove(fish)
            # 使得怪动起来，让怪以v_e速度移动
            else:
                fish[2] = fish[2] + v_e
                if fish[2] == -200:
                    fish_list.remove(fish)


    # 同上的操作，只不过是刷新病毒，且取消了碰到就会吃怪的代码，也就是碰到直接gg
    if time_i % 50 == 0 and level == 1:
        ram_num1 = random.randint(0, 1)
        ram_num2 = random.randint(1, 24)
        if ram_num1 == 1:
            # 随机方向出现 1
            npc_virus.append("left")
        else:
            npc_virus.append("right")
        if ram_num2 >=1 and ram_num2 <= 4:
            # 品种 2
            npc_virus.append("red1")
        elif ram_num2 >= 5 and ram_num2 <= 8:
            npc_virus.append("red2")
        elif ram_num2 >= 9 and ram_num2 <= 12:
            npc_virus.append("yellow1")
        elif ram_num2 >= 13 and ram_num2 <= 16:
            npc_virus.append("yellow2")
        elif ram_num2 >= 17 and ram_num2 <= 20:
            npc_virus.append("green1")
        elif ram_num2 >= 21 and ram_num2 <= 24:
            npc_virus.append("green2")
        if npc_virus[0] == "left":
            npc_virus.append(random.randint(800, 1600))
        else:
            npc_virus.append(random.randint(0, 800))
        npc_virus.append(random.randint(0, 800))
        npc_virus.append(virus_life)
        virus_list.append(npc_virus)
        # print(npc_fish)
        npc_virus = []
    if is_over == False and level == 1 and is_win == False:
        player_rect = new_fish.get_rect()
        player_rect.x = player_x
        player_rect.y = player_y
        for fish in virus_list:
            appear_d = math.sqrt((player_rect.centerx - fish[2])*(player_rect.centerx - fish[2]) + (player_rect.centery - fish[3])*(player_rect.centery - fish[3]))
            if appear_d <= 50:
                continue
            if fish[1] == "red1":
                v_e = 4
                if fish[0] == "left":
                    rect = new_red11.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_red11, (fish[2], fish[3]))
                else:
                    rect = new_red12.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_red12, (fish[2], fish[3]))
                juli = math.sqrt(
                    (rect.centerx - player_rect.centerx) * (rect.centerx - player_rect.centerx) + (
                            rect.centery - player_rect.centery) * (
                            rect.centery - player_rect.centery))
                if juli <= min_distance * 0.4:
                    is_over = True

            if fish[1] == "red2":
                v_e = 3
                if fish[0] == "left":
                    rect = new_red21.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_red21, (fish[2], fish[3]))
                else:
                    rect = new_red22.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_red22, (fish[2], fish[3]))
                juli = math.sqrt(
                    (rect.centerx - player_rect.centerx) * (rect.centerx - player_rect.centerx) + (
                            rect.centery - player_rect.centery) * (
                            rect.centery - player_rect.centery))

                if juli <= min_distance * 0.4:
                    is_over = True
            if fish[1] == "yellow1":
                v_e = 3
                if fish[0] == "left":
                    rect = new_yellow11.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_yellow11, (fish[2], fish[3]))
                else:
                    rect = new_yellow12.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_yellow12, (fish[2], fish[3]))
                juli = math.sqrt(
                    (rect.centerx - player_rect.centerx) * (rect.centerx - player_rect.centerx) + (
                            rect.centery - player_rect.centery) * (
                            rect.centery - player_rect.centery))
                if juli <= min_distance * 0.4:
                    is_over = True
            if fish[1] == "yellow2":
                v_e = 2
                if fish[0] == "left":
                    rect = new_yellow21.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_yellow21, (fish[2], fish[3]))
                else:
                    rect = new_yellow22.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_yellow22, (fish[2], fish[3]))
                juli = math.sqrt(
                    (rect.centerx - player_rect.centerx) * (rect.centerx - player_rect.centerx) + (
                            rect.centery - player_rect.centery) * (
                            rect.centery - player_rect.centery))
                if juli <= min_distance * 0.4:
                    is_over = True
            if fish[1] == "green1":
                v_e = 2
                if fish[0] == "left":
                    rect = new_green11.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_green11, (fish[2], fish[3]))
                else:
                    rect = new_green12.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_green12, (fish[2], fish[3]))
                juli = math.sqrt(
                    (rect.centerx - player_rect.centerx) * (rect.centerx - player_rect.centerx) + (
                            rect.centery - player_rect.centery) * (
                            rect.centery - player_rect.centery))
                if juli <= min_distance * 0.4:
                    is_over = True
            if fish[1] == "green2":
                v_e = 1
                if fish[0] == "left":
                    rect = new_green21.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_green21, (fish[2], fish[3]))
                else:
                    rect = new_green22.get_rect()
                    rect.x = fish[2]
                    rect.y = fish[3]
                    min_distance = math.sqrt(rect.w * rect.w + rect.h * rect.h)
                    screen.blit(new_green22, (fish[2], fish[3]))
                juli = math.sqrt(
                    (rect.centerx - player_rect.centerx) * (rect.centerx - player_rect.centerx) + (
                            rect.centery - player_rect.centery) * (
                            rect.centery - player_rect.centery))
                if juli <= min_distance * 0.4:
                    is_over = True

            # 循环所有的第一种子弹
            for b in bullets:
                distance3 = math.sqrt((b[0].x - rect.centerx) * (b[0].x - rect.centerx) + (b[0].y - rect.centery) * (
                        b[0].y - rect.centery))
                # print(distance3)
                if distance3 <= min_distance * 0.4:
                    # 如果距离小于0.4怪的半径，怪将受到伤害
                    if fish[1] == "yellow1" or fish[1] == "yellow2":
                        fish[4] = fish[4] - 0.5
                        # 黄怪减去0.5
                    if fish[1] == "red1" or fish[1] == "red2":
                        # 红怪减去伤害
                        fish[4] = fish[4] - 1
                    try:
                        enemies_die.play()
                        if fish[4] == 0:
                            # 如果怪的生命等于0则移除怪
                            if fish[1] == "green1" or fish[1] == "green2":
                                green_number = green_number + 1
                            if fish[1] == "yellow1" or fish[1] == "yellow2":
                                yellow_number = yellow_number + 1
                            if fish[1] == "red1" or fish[1] == "red2":
                                red_number = red_number + 1
                                fish[4] = fish[4] - 1
                            virus_list.remove(fish)
                        bullets.remove(b)
                    except:
                        break
                    # try，except结构，防止某一次循环运行报错后直接推出程序

                if red_number>=2 and yellow_number>=2 and green_number >=2:
                    # 需要打 红绿黄 每种怪两种boss才会出现哦
                    boss_show = True
            # 第二种子弹和上面差不多
            for b in bullets1:
                distance3 = math.sqrt((b[0].x - rect.centerx) * (b[0].x - rect.centerx) + (b[0].y - rect.centery) * (
                        b[0].y - rect.centery))
                if distance3 <= min_distance * 0.4:
                    if fish[1] == "green1" or fish[1] == "green2":
                        fish[4] = fish[4] - 1
                    if fish[1] == "yellow1" or fish[1] == "yellow2":
                        fish[4] = fish[4] - 0.5
                    try:
                        enemies_die.play()
                        if fish[4] == 0:
                            if fish[1] == "green1" or fish[1] == "green2":
                                green_number = green_number + 1
                            if fish[1] == "yellow1" or fish[1] == "yellow2":
                                yellow_number = yellow_number + 1
                            if fish[1] == "red1" or fish[1] == "red2":
                                red_number = red_number + 1
                            virus_list.remove(fish)
                        bullets1.remove(b)
                    except:
                        break
                if red_number >= 2 and yellow_number >= 2 and green_number >= 2:
                    boss_show = True

            # 怪的移动上面讲过
            if fish[0] == "left":
                fish[2] = fish[2] - v_e
                if fish[2] == 1600:
                    fish_list.remove(fish)
            else:
                fish[2] = fish[2] + v_e
                if fish[2] == -200:
                    fish_list.remove(fish)
        # 让boss出现，并且设定当生命值为零时不执行代码
        if boss_show and (boss_life >= 0 or boss_life1 >= 0):
            time_d = time_d +1
            boss_rect = new_boss.get_rect()
            boss_rect.x = boss_x
            boss_rect.y = boss_y
            if time_d % 2000 == 0:
                v_boss_x = random.randint(-3, 3)
                v_boss_y = random.randint(-3, 3)
            # 随机速度2000毫秒换一次
            screen.blit(new_boss, (boss_x, boss_y))
            # 画出boss
            boss_x = boss_x + v_boss_x
            boss_y = boss_y + v_boss_y
            min_distance = math.sqrt(boss_rect.w * boss_rect.w + boss_rect.h * boss_rect.h)
            if boss_rect.left <= 0 and v_boss_x <= 0:
                v_boss_x = -v_boss_x
            elif boss_rect.right >= 1600 and v_boss_x >= 0:
                v_boss_x = -v_boss_x
            elif boss_rect.top <= 0 and v_boss_y <= 0:
                v_boss_y = -v_boss_y
            elif boss_rect.bottom >= 900 and v_boss_y >= 0:
                v_boss_y = -v_boss_y
            # 让怪碰壁反弹
            juli = math.sqrt(
                (boss_rect.centerx - player_rect.centerx) * (boss_rect.centerx - player_rect.centerx) + (
                        boss_rect.centery - player_rect.centery) * (
                        boss_rect.centery - player_rect.centery))
            # 和上面一样的子弹操作
            for b in bullets:
                distance4 = math.sqrt((b[0].x - boss_rect.centerx) * (b[0].x - boss_rect.centerx) + (b[0].y - boss_rect.centery) * (
                        b[0].y - boss_rect.centery))
                if distance4 <= min_distance * 0.4:
                    boss_life = boss_life - 1
                    try:
                        enemies_die.play()
                        bullets.remove(b)
                    except:
                        break
            for b in bullets1:
                distance4 = math.sqrt(
                    (b[0].x - boss_rect.centerx) * (b[0].x - boss_rect.centerx) + (b[0].y - boss_rect.centery) * (
                            b[0].y - boss_rect.centery))
                if distance4 <= min_distance * 0.6:
                    boss_life1 = boss_life1 - 1
                    try:
                        enemies_die.play()
                        bullets1.remove(b)
                    except:
                        break
            if juli <= min_distance * 0.4 and eat_number < 4:
                is_over = True
    # boss生命等于零时，就胜利了！
    if boss_life <=0 and boss_life1 <=0:
        is_win = True



    # 画出主角位置
    screen.blit(new_fish, (player_x, player_y))
    
    if is_over and overtime == 0:
        over_music.play()
        # 游戏结束音乐
        overtime = 1
    # 这个算法当时想了半天。。。怎么让音乐在无限循环中只放一次

    if is_win and overtime == 0:
        boss_die_music.play()
        # boss死亡音
        win_music.play()
        # 胜利音乐
        overtime = 1

    show_bullet_number()
    # 调用子弹出现函数
    check_is_over()
    # 检查游戏是否结束函数
    check_is_win()
    # 检查是否胜利函数
    pygame.display.update()
    # 最终要每次循环更新画面
