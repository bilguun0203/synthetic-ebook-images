import os
import imageio
import imgaug as ia
from imgaug import augmenters as iaa
ia.seed(4)
import uuid
from PIL import Image

os.system("mkdir -p ./dataset/augmented")

seq = iaa.Sequential([
    iaa.AddToHueAndSaturation((-60, 60)),          # change their color
    iaa.ElasticTransformation(alpha=90, sigma=16), # water-like effect
    iaa.Affine(rotate=(-5, 5)),
    iaa.AdditiveGaussianNoise(scale=(10, 60)),
    iaa.Crop(percent=(0, 0.2))
], random_order=True)

def seq_augment(image, n_try=8):
    return [Image.fromarray(seq.augment_image(image)) for _ in range(n_try)]

for img_file in os.listdir("./dataset/images"):
    if img_file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        img_path     = os.path.join('dataset', 'images', img_file)
        image        = imageio.imread(img_path)

        for img in seq_augment(image):
            new_name    = str(uuid.uuid4())+".jpg"
            out_path    = os.path.join('dataset', 'augmented', new_name)
            img.save(out_path)
        pass

