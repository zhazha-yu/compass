import cv2
import os
import time

p = 1
#点击函数,screen为模板
def touch(screen,template):
	global p
	img_x, img_y = template.shape[:2]#模板匹配
	result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	# print("prob:", max_val)#输出匹配度
	if max_val > 0.98:
	    x = max_loc[0] + img_y / 2
	    y = max_loc[1] + img_x / 2
	    # print(x,y)#期望坐标点
	    os.system('adb shell input tap %d %d'%(x,y))#点击坐标点
	    p = 0
	else:
	    p = 1 

#点击开始
def open():
	os.system('adb shell screencap -p /data/compass.png')#截取当前屏幕到设备
	os.system('adb pull /data/compass.png ./now.png')#截图推到主机
	time.sleep(1)
	scr = cv2.imread('now.png')
	tmp = cv2.imread('open.png')
	touch(scr,tmp)
	if(p == 1):
		# print("Open Match Error")
		return True
	else:
		print('Open OK')
		return False

#点击rank
def rank():
	time.sleep(1.5)
	os.system('adb shell screencap -p /data/compass.png')#截取当前屏幕到设备
	os.system('adb pull /data/compass.png ./now.png')#截图推到主机
	time.sleep(1)
	scr = cv2.imread('now.png')
	tmp = cv2.imread('rank.png')
	touch(scr,tmp)
	if(p == 1):
		# print("Rank Match Error")
		return True
	else:
		print('Rank OK')
		return False

#晶满了
def step():
	time.sleep(1.5)
	os.system('adb shell screencap -p /data/compass.png')#截取当前屏幕到设备
	os.system('adb pull /data/compass.png ./now.png')#截图推到主机
	time.sleep(1)
	scr = cv2.imread('now.png')
	tmp = cv2.imread('step.png')
	touch(scr,tmp)
	if(p == 1):
		# print("Step Match Error")
		return True
	else:
		print('Step OK')
		return False

#点击auto
def auto():
	time.sleep(1)
	os.system('adb shell screencap -p /data/compass.png')#截取当前屏幕到设备
	os.system('adb pull /data/compass.png ./now.png')#截图推到主机
	time.sleep(1)
	scr = cv2.imread('now.png')
	tmp = cv2.imread('auto.png')
	touch(scr,tmp)
	if(p == 1):
		# print("Auto Match Error")
		return True
	else:
		print('Auto OK')
		return False

#点击结束1
def over1():
	time.sleep(2)
	os.system('adb shell screencap -p /data/compass.png')#截取当前屏幕到设备
	os.system('adb pull /data/compass.png ./now.png')#截图推到主机
	time.sleep(2)
	scr = cv2.imread('now.png')
	tmp = cv2.imread('over1.png')
	touch(scr,tmp)
	if(p == 1):
		# print("Over1 Match Error")
		return True
	else:
		print('Over1 OK')
		return False

#点击结束2
def over2():
	time.sleep(1)
	os.system('adb shell screencap -p /data/compass.png')#截取当前屏幕到设备
	os.system('adb pull /data/compass.png ./now.png')#截图推到主机
	time.sleep(1)
	scr = cv2.imread('now.png')
	tmp = cv2.imread('over2.png')
	touch(scr,tmp)
	if(p == 1):
		# print("Over2 Match Error")
		return True
	else:
		print('Over2 OK')
		return False

print('请输入代刷次数：')
num = int(input())
for i in range(0,num):
	while(open()):
		pass
	while(rank()):
		pass
	while(step()):
		pass
	time.sleep(40)#等待进入游戏,预设40s
	while(auto()):
		pass
	time.sleep(120)#等待结束,固定时长3min,挂机大概率提前结束
	for j in range(0,4):
		while(over1()):
			pass
	while(over2()):
		pass
	time.sleep(10)#返回主界面
print('All Over')