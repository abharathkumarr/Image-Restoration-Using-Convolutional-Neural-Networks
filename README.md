# IMage -colorization using simple Flask and caffe model:
Conversion of black and white images to color

Requriements:
==============
OS : Linux 

FrameWork - Flask

Model: Caffe

Lang: Python 

Pacakges: numpy, opencv

Frontend: Html,css

Running of project:
===================

1. Install flask and setup the environment
2. clone this code base into the folder which flask is present
3. Invoke flask env
4. Pip install all the required python packages
5. Run the project with te below command

Run command:

python3 upload_file.py --image imes/baby.jpeg --prototxt model/colorization_deploy_v2.prototxt --model model/colorization_release_v2.caffemodel --points model/pts_in_hull.npy


Note:
====
The image name should be given from the cmd prompt , upload file does not work w.r.t to multiple images. So each time 
when you want to colorize new image give the  image name seperately for example:


Ex1: 

python3 upload_file.py --image imes/image1.jpeg --prototxt model/colorization_deploy_v2.prototxt --model model/colorization_release_v2.caffemodel --points model/pts_in_hull.npy



Ex2:

python3 upload_file.py --image imes/image2.jpeg --prototxt model/colorization_deploy_v2.prototxt --model model/colorization_release_v2.caffemodel --points model/pts_in_hull.npy









