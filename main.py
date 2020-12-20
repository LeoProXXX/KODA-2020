# scenariusz weruyikacji kodu Golomba
# - Przetestować algorytm na sztucznie wygenerowanych ciągach danych o rozkładzie równomiernym, normalnym, geometrycznym oraz obrazach testowych kodowanych różnicowo.
# - Wyznaczyć histogram i entropię danych wejściowych.
# - Porównać entropię ze średnią długością bitową kodu wyjściowego.
# - Ocenić efektywność algorytmu do kodowania obrazów naturalnych.

from codec import GolombCodec
from Loader import Loader
from Utils import calculate_average_length
from Utils import calculate_length
import numpy as np


def test_images(images):
    for img in images:
        # print(len(set(img.getdata())))
        # print(img.mode)
        w, h = img.size
        numpy_image = np.asarray(img)
        result = golomb_codec.encode_image(numpy_image)
        length = calculate_length(result)
        avg_len = calculate_average_length(result)
        # print(f'entropia: {loader.entropy(img)} średnia długoś wyjściowego kodu bitowego: {avg_len}')
        print(f'original length: {w * h * 8}, after compression: {length}, compression ratio: {length / (w * h * 8)}')


golomb_codec = GolombCodec(9)

loader = Loader(natural_images_dir="data/obrazy",
                artificial_images_dir="data/rozklady")
artificial_images = loader.getArtificialImages()


print('rozklady')
# test_images(loader.getArtificialImages())
print('obrazy naturalne\n')
test_images(loader.getNaturalImages())
