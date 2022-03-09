# TDPS notes from Image Processing Segment
## Date 3.7
### First Attempt
- Process 
	- Convert the image into grayscale
	- Do the Gaussian blur with radius 2
 	- Edge detection with operator 
$$
\nabla=\begin{bmatrix}
-2 & -1 & 2\\
-6 & 0 & 6 \\
-2 & -1 &2
\end{bmatrix}
$$
- Image binary processing 
### Result
- Could turn the route into white points with black background, which could manifest the route 
- However, working effectively for every segments of the route
### Some optimizations
- Change the operator for edge detection as
$$
	\nabla=\begin{bmatrix} -3 & 5 & 3\\-10 & 0 & 10 \\-3 & 5 & 3 \end{bmatrix}
$$
- Abandon the Gaussian blur operation
- Add the image erosion operation
```python
image3 = (image2 / float(image2.max())) * 255
kernel = np.ones((5, 5), np.uint8)
image3 = cv2.erode(image3, kernel)
```
### Further plan
- Try to integrate the process with OpenMV micro python codes
- To check whether the weather and time of the day would influence the route detection hugely

## Date 3.8

### Outcomes of OpenMV with previous plan
- Detections of turnings are poor when the color outside of the route is similar to that of the route
- However, OpenMV succeeds in detecting direct or bending route when the color itself is easily identifiable 
     ![DD4BD8FE-811C-4E3A-B8B1-DF98466A57D6.jpeg](https://s2.loli.net/2022/03/08/p68ezvaP9ixWV3R.jpg)
### Some possible improving methods
- Expand the operator to a 5X5 matrix
- Try both ``erode()`` function and ``dilate()`` function
- Add the Gaussian blur operation with radius 1 again
## Date 3.9
### Progress
- Successfully traverse codes with OpenCV into OpenMV micro python codes
- However, the result shown in OpenMV is poor, and what we achieved using OpenCV could not be reached in OpenMV camera
### Several changes
- Set the kernel operator to 
$$
  \nabla=\begin{bmatrix} 0 & -1 & 0\\-1 & 8 & -1 \\0 & 1 & 0 \end{bmatrix}
$$
- Binarize the picture
  ```python
   img2.binary([(40,50,-5,5,-5,5)]) # Set LAB color space threshold as 40 to 50 for light intensity channel, -5 to 5 for both A and B color channel
  ```
- 
