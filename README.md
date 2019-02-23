# Pyramid Blending


This project is about pyramid blending pipeline that will allow you to combine separate images into a seamlessly blended image. The technique is based on the paper [“A multiresolution spline with application to image mosaics”](http://persci.mit.edu/pub_pdfs/spline83.pdf) (Burt and Adelson; ACM 1983) (see lessons Module 04-03 Pyramids, 04-04 Image Blends).


## How to use it

- Place your images in the `images/source/sample` directory. 

- Execute the blending pipeline by running `python main.py`. The script will look inside each subfolder under `images/source`, looking for folders that have images with filenames that end with 'white', 'black' and 'mask'. For each such folder it finds, it will apply the blending procedure to them, and save the output to a folder with the same name as the input in `images/output/`. 

- The blending procedure splits the input images into their blue, green, and red channels and blends each channel separately. You do not have to worry about dealing with three channels; you can assume your functions take in grayscale images.

- Along with the output blended image, main.py will create visualizations of the Gaussian and Laplacian pyramids for the blend. You may use or refer to these to explain your code in your report, but they are not required. 
