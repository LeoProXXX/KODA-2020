import os
import glob
from PIL import Image

class Loader:
    def __init__(self, natural_images_dir: str = None, 
                 artificial_images_dir: str = None) -> None:

        self.natural_images = glob.glob(natural_images_dir + "/*.pgm", recursive=True)
        self.artificial_images = glob.glob(artificial_images_dir + "/*.pgm", recursive=True)
        
        image = Image.open(self.natural_images[0])
        image.show()
        
        

if __name__ == "__main__":
    loader = Loader(natural_images_dir="data/obrazy", 
                    artificial_images_dir="data/rozklady")