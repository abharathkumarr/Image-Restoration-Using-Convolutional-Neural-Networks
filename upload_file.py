from flask import Flask, render_template, request,make_response
import cv2
from flask import jsonify
import argparse
import numpy as np
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('template.html')
@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['file']
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input black and white image")
    ap.add_argument("-p", "--prototxt", type=str, required=True,
	help="path to Caffe prototxt file")
    ap.add_argument("-m", "--model", type=str, required=True,
	help="path to Caffe pre-trained model")
    ap.add_argument("-c", "--points", type=str, required=True,
	help="path to cluster center points")
    args = ap.parse_args()
    net = cv2.dnn.readNetFromCaffe(args.prototxt, args.model)
    pts = np.load(args.points)
    class8 = net.getLayerId("class8_ab")
    conv8 = net.getLayerId("conv8_313_rh")
    pts = pts.transpose().reshape(2, 313, 1, 1)
    net.getLayer(class8).blobs = [pts.astype("float32")]
    net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]
    image = cv2.imread(args.image)
    scaled = image.astype("float32") / 255.0
    lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
    resized = cv2.resize(lab, (224, 224))
    L = cv2.split(resized)[0]
    L -= 50
    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))


    ab = cv2.resize(ab, (image.shape[1], image.shape[0]))


    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)

    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized, 0, 1)

    colorized = (255 * colorized).astype("uint8")

    retval, buffer = cv2.imencode('.jpeg', colorized)
    response = make_response(buffer.tobytes())
    response.headers['Content-Type'] = 'image/png'
    return response
   
if __name__ == '__main__':
    app.run()
