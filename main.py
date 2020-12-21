# scenariusz weryfikacji kodu Golomba
# - Przetestować algorytm na sztucznie wygenerowanych ciągach danych o rozkładzie równomiernym, normalnym, geometrycznym oraz obrazach testowych kodowanych różnicowo.
# - Wyznaczyć histogram i entropię danych wejściowych.
# - Porównać entropię ze średnią długością bitową kodu wyjściowego.
# - Ocenić efektywność algorytmu do kodowania obrazów naturalnych.

from loader import Loader
from encoder import GolombEncoder

loader = Loader(natural_images_dir="data/obrazy", 
                artificial_images_dir="data/rozklady")
loader.generateHistograms()

naturalImages = loader.getNaturalImages()[:2]
artificialImages = loader.getArtificialImages()[:2]

i = [1, 2, 3, 4, 5]
for image in naturalImages:
    image = image.flatten().tolist()
    encodedImage = GolombEncoder(5).encodeImage(image)