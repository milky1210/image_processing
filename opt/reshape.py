from pathlib import Path
import cv2
import numpy as np

def main():
    for file in Path('images/').glob("*.png"):
        img = cv2.imread(str(file),-1)
        print(img.shape)
        dst_path = Path("outputs") / file.name
        dst_path.parent.mkdir(exist_ok=True, parents=True)
        cv2.imwrite(str(dst_path), cv2.resize(img,(1242, 2208)))
    return 




if __name__ == '__main__':
    main()