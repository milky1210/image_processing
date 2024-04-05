import cv2
import argparse
from pathlib import Path

# ArgumentParser オブジェクトの作成
parser = argparse.ArgumentParser(description='Process an image file.')

# コマンドライン引数の追加（'--input' はオプション名、helpはその説明）
parser.add_argument('--input', type=str, help='Path to the input image file.')

# 引数を解析
args = parser.parse_args()

# 入力ファイル名の取得
input_filename = args.input

# 入力がなければ終わり
if not input_filename:
    print('No input file provided.')

# ここで input_filename を使用して何らかの処理を行う
img = cv2.imread(input_filename)

if img is None:
    print('Load Err.')  

output_base_path = str(Path(input_filename).with_suffix(""))

# +90度回転して保存
rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite(output_base_path + '_90.jpg', rotated_90)

# +180度回転して保存
rotated_180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imwrite(output_base_path + '_180.jpg', rotated_180)

# +270度（または-90度）回転して保存
rotated_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite(output_base_path + '_270.jpg', rotated_270)