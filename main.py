# scenariusz weryfikacji kodu Golomba
# - Przetestować algorytm na sztucznie wygenerowanych ciągach danych o rozkładzie równomiernym, normalnym, geometrycznym oraz obrazach testowych kodowanych różnicowo.
# - Wyznaczyć histogram i entropię danych wejściowych.
# - Porównać entropię ze średnią długością bitową kodu wyjściowego.
# - Ocenić efektywność algorytmu do kodowania obrazów naturalnych.

import os

import numpy as np

from codec import GolombCodec
from encoder import GolombEncoder
from loader import Loader
from utils import calculate_average_length
from utils import calculate_length


def run_test_images():
    # print('rozklady')
    # test_images(loader.getArtificialImagesAsNumpyArray())
    print('obrazy naturalne\n')
    test_natural_images_compression(loader.getNaturalImagesAsNumpyArray())


def test_natural_images_compression(images):
    for i in range(0, 9, 2):
        print(f'Golomb for i={i}')
        golomb_codec = GolombCodec(i)
        benchmarks = []
        for img_params in images:
            img = img_params[0]
            path = img_params[1]
            w, h = img.size
            numpy_image = np.asarray(img)
            result = golomb_codec.encode_image(numpy_image)
            length = calculate_length(result)
            avg_len = calculate_average_length(result)

            benchmarks.append({'name': os.path.basename(path),
                               'originalLength': w * h * 8,
                               'resultLength': length,
                               'avr_word_len': avg_len,
                               'entropy': loader.entropy(img),
                               'compressionRatio': length / (w * h * 8)})

        print("Name\t Original length\tAfter compression\tCompression ratio")
        for benchmark in benchmarks:
            print(
                f'{benchmark["name"]}\t{benchmark["originalLength"]}\t{benchmark["resultLength"]}\t{benchmark["compressionRatio"]}')

        print("\nName\t Entropy\t Avr word length")
        for benchmark in benchmarks:
            print(f'{benchmark["name"]}\t{benchmark["entropy"]}\t{benchmark["avr_word_len"]}')


def test_encoder():
    for i in range(0, 5):
        print('i:', i)
        for s in range(5):
            print(f's: {s} kod: {GolombEncoder(i).encode(s)}')


loader = Loader(natural_images_dir="data/obrazy",
                artificial_images_dir="data/rozklady")

run_test_images()
# test_encoder()

loader.generateHistograms()

naturalImages = loader.getNaturalImages()[:2]
artificialImages = loader.getArtificialImages()[:2]

i = [1, 2, 3, 4, 5]
for image in naturalImages:
    image = image.flatten().tolist()
    encodedImage = GolombEncoder(5).encodeImage(image)
