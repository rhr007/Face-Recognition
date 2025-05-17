# Face-Recognition
I implemented face recognition using opencv-python and face-recognition library.

## Problems I faced while using face-recognition library and Solutions:
1. To install face-recognition properly dlib file is mandatory.
      i) for linux and mac is easy and simple just read and follow the steps from <a href="https://pypi.org/project/face-recognition/">this link</a>
      ii) for windows downlaod appropriate .whl file according to your python version from <a href="https://github.com/z-mahmud22/Dlib_Windows_Python3.x">this website</a>

2. face-recognition does not support numpy of above version 2+. It shows <b><i>Unsupported image type, must be 8bit gray or RGB image.</i></b>. For this use lower version like 1.26.4.

## Demo Output
<b>Wait a bit, it needs 4 to 5 seconds to load</b>
![alt text](https://github.com/rhr007/Face-Recognition/blob/main/Demo.gif?raw=true)
