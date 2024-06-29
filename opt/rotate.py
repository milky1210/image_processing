import cv2
import argparse
from shutil import copyfile
from pathlib import Path

# ArgumentParser オブジェクトの作成
parser = argparse.ArgumentParser(description='Process an image file.')

# コマンドライン引数の追加（'--input' はオプション名、helpはその説明）
parser.add_argument('--input', type=str, help='Path to the input image file.')
parser.add_argument('--id', type=int, help='id of output file.')

# 引数を解析
args = parser.parse_args()

# 入力ファイル名の取得
input_filename = args.input
id_ = args.id

# 入力がなければ終わり
if not input_filename:
    print('No input file provided.')

# ここで input_filename を使用して何らかの処理を行う
img = cv2.imread(input_filename)

if img is None:
    print('Load Err.')  

output_base_path = "outputs/GOPR"
# CSVファイルの元のパス
base_csv_path = Path('src/BASE.CSV')


# +0度回転させて保存
cv2.imwrite(output_base_path + f'{id_:04d}.JPG', img)
copyfile(base_csv_path, output_base_path + f'{id_:04d}.CSV')

if False:
    # +90度回転して保存
    rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(output_base_path + f'{id_+1:04d}.JPG', rotated_90)
    copyfile(base_csv_path, output_base_path + f'{id_+1:04d}.CSV')

    # +180度回転して保存
    rotated_180 = cv2.rotate(img, cv2.ROTATE_180)
    cv2.imwrite(output_base_path + f'{id_+2:04d}.JPG', rotated_180)
    copyfile(base_csv_path, output_base_path + f'{id_+2:04d}.CSV')

    # +270度（または-90度）回転して保存
    rotated_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imwrite(output_base_path + f'{id_+3:04d}.JPG', rotated_270)
    copyfile(base_csv_path, output_base_path + f'{id_+3:04d}.CSV')