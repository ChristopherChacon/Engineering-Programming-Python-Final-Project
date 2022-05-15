from PIL import Image
import numpy as np
import os


def load_dataset(fname=None):
    if fname is None:
        fname = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
        fname = os.path.join(fname, 'labels.csv')

    data = np.genfromtxt(fname, dtype=['|S19', '<f8', '|S4'], names=['path', 'probability'])
    image_fnames = np.char.decode(data['path'])
    probs = data['probability']

    def load_cell_image(fname):
        with Image.open(fname) as image:
            return np.asarray(image)

    dir = os.path.dirname(fname)

    images = np.array([load_cell_image(os.path.join(dir, fn))
                       for fn in image_fnames])

    return images, probs
