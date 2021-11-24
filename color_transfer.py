import numpy as np
import cv2
import os

def read_file(sn,tn):
	s = cv2.imread('source/'+sn+'.bmp')
	s = cv2.cvtColor(s,cv2.COLOR_BGR2LAB)
	t = cv2.imread('target/'+tn+'.bmp')
	t = cv2.cvtColor(t,cv2.COLOR_BGR2LAB)
	return s, t

def get_mean_and_std(x):
	x_mean, x_std = cv2.meanStdDev(x)
	x_mean = np.hstack(np.around(x_mean,2))
	x_std = np.hstack(np.around(x_std,2))
	return x_mean, x_std

# def color_transfer():
# 	sources = ['s1','s2','s3','s4','s5','s6']
# 	targets = ['t1','t2','t3','t4','t5','t6']

# 	for n in range(len(sources)):
# 		print("Converting picture"+str(n+1)+"...")
# 		s, t = read_file(sources[n],targets[n])
# 		s_mean, s_std = get_mean_and_std(s)
# 		t_mean, t_std = get_mean_and_std(t)

# 		height, width, channel = s.shape
# 		for i in range(0,height):
# 			for j in range(0,width):
# 				for k in range(0,channel):
# 					x = s[i,j,k]
# 					x = ((x-s_mean[k])*(t_std[k]/s_std[k]))+t_mean[k]
# 					# round or +0.5
# 					x = round(x)
# 					# boundary check
# 					x = 0 if x<0 else x
# 					x = 255 if x>255 else x
# 					s[i,j,k] = x

# 		s = cv2.cvtColor(s,cv2.COLOR_LAB2BGR)
# 		cv2.imwrite('result/r'+str(n+1)+'.bmp',s)

# color_transfer()
# os.system("pause")


def color_transfer(c_path, s_path):
	c_img = cv2.imread(c_path)
	s_img = cv2.imread(s_path)
	c_img = cv2.cvtColor(c_img, cv2.COLOR_BGR2LAB)
	s_img = cv2.cvtColor(s_img, cv2.COLOR_BGR2LAB)
	c_mean, c_std = get_mean_and_std(c_img)
	s_mean, s_std = get_mean_and_std(s_img)

	c_mean = np.expand_dims(np.expand_dims(c_mean, axis=0), axis=0)
	c_std = np.expand_dims(np.expand_dims(c_std, axis=0), axis=0)
	s_mean = np.expand_dims(np.expand_dims(s_mean, axis=0), axis=0)
	s_std = np.expand_dims(np.expand_dims(s_std, axis=0), axis=0)
	# print(f'c_mean={c_mean.shape}, c_std={c_std.shape}')
	# print(f's_mean={s_mean.shape}, s_std={s_std.shape}')
	out = (c_img - c_mean) *(s_std / c_std) + s_mean
	out = np.rint(out)
	out = np.clip(out, 0, 255)
	out = out.astype(np.uint8)
	out = cv2.cvtColor(out, cv2.COLOR_LAB2BGR)
	return out

	# height, width, channel = c_img.shape
	# for i in range(0,height):
	# 	for j in range(0,width):
	# 		for k in range(0,channel):
	# 			x = c_img[i,j,k]
	# 			x = ((x-c_mean[k])*(s_std[k]/c_std[k]))+s_mean[k]
	# 			# round or +0.5
	# 			x = round(x)
	# 			# boundary check
	# 			x = 0 if x<0 else x
	# 			x = 255 if x>255 else x
	# 			c_img[i,j,k] = x
	# c_img = cv2.cvtColor(c_img,cv2.COLOR_LAB2BGR)
	# return c_img
