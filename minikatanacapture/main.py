import cv2 

from cv2 import VideoCapture 
from os import path, makedirs
from typing import final

@final
class MiniCatanaCapture:
    @final
    def __init__(self, **kwargs) -> None:
        self.__video: str = kwargs.get('video')
        
        if (not self.check_path(self.__video)): raise Exception('video not found')
        
        self.__capture: VideoCapture = VideoCapture(self.__video)
        self.__output: str = kwargs.get('output')

    @final
    @staticmethod
    def check_path(location: str) -> bool:
        return path.exists(location)

    @final
    def main(self):
        name: str = self.__video.split('/')[-1].split('.')[0]
        self.__capture: VideoCapture = VideoCapture(self.__video)

        if(not self.check_path(output := f'{self.__output}/{name}')): 
            makedirs(output)

        count: int = 1
        while(data := self.__capture.read()):
            if(not data[0]): break

            cv2.imwrite(f"{output}/{name}_{count}.jpg", data[1])
            cv2.imshow(name, data[1])
            cv2.waitKey(1)

            count += 1

        self.__capture.release()

        cv2.destroyAllWindows()