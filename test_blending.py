import cv2
import unittest

from os import path

from examples import blending as blend

"""
You can use this file as a starting point to write your own unit tests
for this assignment. You are encouraged to discuss testing with your
peers, but you may not share code directly. Your code is scored based
on test cases performed by the autograder upon submission -- these test
cases will not be released.

    DO NOT SHARE CODE (INCLUDING TEST CASES) WITH OTHER STUDENTS.
"""

IMG_FOLDER = "images/source/sample"


class Assignment6Test(unittest.TestCase):

    def setUp(self):
        self.black_img = cv2.imread(path.join(IMG_FOLDER, "black.jpg"))
        self.white_img = cv2.imread(path.join(IMG_FOLDER, "white.jpg"))
        self.mask_img = cv2.imread(path.join(IMG_FOLDER, "mask.jpg"))

        if any(map(lambda x: x is None,
                   [self.black_img, self.white_img, self.mask_img])):
            raise IOError("Error, samples image not found.")


    def test_reduce_layer(self):
        self.black_img = cv2.imread(path.join(IMG_FOLDER, "black.jpg"), cv2.IMREAD_GRAYSCALE)
        
        img = blend.reduce_layer(self.black_img)    
        img = blend.reduce_layer(self.black_img, blend.generatingKernel(0))    
        img = blend.reduce_layer(self.black_img, blend.generatingKernel(0.3))
        img = blend.reduce_layer(self.black_img, blend.generatingKernel(0.5))
        
    # def test_expand_layer(self): 
    #     self.black_img = cv2.imread(path.join(IMG_FOLDER, "black.jpg"), cv2.IMREAD_GRAYSCALE)
    #     self.white_img = cv2.imread(path.join(IMG_FOLDER, "white.jpg"), cv2.IMREAD_GRAYSCALE)
    #     img = blend.expand_layer(blend.reduce_layer(self.black_img))
    #     img = blend.expand_layer(blend.reduce_layer(self.white_img))

    # def test_gaussPyramid(self): 
    #     self.black_img = cv2.imread(path.join(IMG_FOLDER, "black.jpg"), cv2.IMREAD_GRAYSCALE)
    #     pyramid = blend.gaussPyramid(self.black_img, 5)

    #     self.white_img = cv2.imread(path.join(IMG_FOLDER, "white.jpg"), cv2.IMREAD_GRAYSCALE)
    #     pyramid = blend.gaussPyramid(self.white_img, 5)

    # def test_laplPyramid(self): 
    #     self.black_img = cv2.imread(path.join(IMG_FOLDER, "black.jpg"), cv2.IMREAD_GRAYSCALE)
    #     img = blend.laplPyramid(blend.gaussPyramid(self.black_img, 5))
        
    #     self.white_img = cv2.imread(path.join(IMG_FOLDER, "white.jpg"), cv2.IMREAD_GRAYSCALE)
    #     img = blend.laplPyramid(blend.gaussPyramid(self.white_img, 5))

    # def test_blend(self): 
    #     self.black_img = cv2.imread(path.join(IMG_FOLDER, "black.jpg"), cv2.IMREAD_GRAYSCALE)
    #     self.white_img = cv2.imread(path.join(IMG_FOLDER, "white.jpg"), cv2.IMREAD_GRAYSCALE)
    #     self.mask_img = cv2.imread(path.join(IMG_FOLDER, "mask.jpg"), cv2.IMREAD_GRAYSCALE)

        # imgBlack = blend.laplPyramid(blend.gaussPyramid(self.black_img, 5))
        # imgWhite = blend.laplPyramid(blend.gaussPyramid(self.white_img, 5))

        # blend.blend(imgBlack, imgWhite, self.mask_img)

    # def test_collapse(self): 



if __name__ == '__main__':
    unittest.main()
