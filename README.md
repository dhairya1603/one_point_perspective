the python file attached here should work for any sort of picture that can work with CV2 library. 

the way it works is. 

1. it converts picture into grayscale.
2. it applies gaussian deblurring filter over it
3. it detacts the edges
4. finds contours in the edge image
5. Filter potential points based on size and circularity
