from pathlib import Path
import cv2
import numpy as np

def main():
    for file in Path('src/').glob("*.png"):
        img = cv2.imread(file,-1)
        print(img.shape)
        # 投下している個所を白にする
        for i in range(3):
            img[:,:,i] = np.where(img[:,:,3] == 0, 255, img[:,:,i])
        cv2.imwrite(str(Path("outputs") / file.name), img[:,:,:3])
    return 




if __name__ == '__main__':
    main()