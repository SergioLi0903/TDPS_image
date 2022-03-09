# Untitled - By: lenovo - 周一 3月 7 2022

import sensor, image, time
#(37, 55, 0, 18, -12, 34)
kernel_size = 1
kernel = [-3, 5, 3,\
          -10, 0, 10,\
          -3, 5, 3]

kernel2 = [0, -1, 0,\
          -1, 8, -1,\
          0, -1, 0]
sensor.reset() # Initialize the camera sensor.
#sensor.set_vflip(True)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQQVGA)
sensor.skip_frames(10) # 让新的设置生效
#sensor.set_auto_gain(False) # must be turned off for color tracking
#sensor.set_auto_whitebal(False) # must be turned off for color tracking
clock = time.clock() # 跟踪FPS帧率

while(True):
    img = sensor.snapshot().lens_corr(strength = 1.8, zoom = 1.0)
    img.histeq()
    img2=img.copy()
    img2.binary([(40,50,-5,5,-5,5)])
    #img2.binary([(45,60,-20,0,-20,20)])
    img2.invert()
    img.to_grayscale()
    #img.gamma_corr()
    img.gaussian(1)
    img.morph(kernel_size, kernel2)
    #img.morph(kernel_size, kernel)
    x=img.get_statistics()
    max_value=x.max()*1.0
    print(x)
    #print(max_value)
    #for i in range(160):
        #for j in range(120):
            #k=img.get_pixel(i,j)
            #img.set_pixel(i,j,int((k/max_value)*255))

    img.erode(2)

    y=img.get_statistics()
    thresholds = [(y.mean(), 255)]
    img.binary(thresholds)
    img.nor(img2)
    #img.erode(2)
    img.invert()




#可以进行的操作，腐蚀和膨胀的顺序，是否先去翻，腐蚀碰撞和二值化谁先。是否高斯滤波，是否gamma变化
