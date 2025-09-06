from pathlib import Path
import cv2
import numpy as np

def process_image(file_path, output_dir):
    # 画像を読み込む（アルファチャンネルを含む）
    image = cv2.imread(str(file_path), cv2.IMREAD_UNCHANGED)
    
    # 画像がRGBAでない場合、RGBAに変換
    if image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    
    # 各チャンネルを取得
    b, g, r, a = cv2.split(image)
    
    # 白い部分（しきい値を設定）
    white_mask = (r > 200) & (g > 200) & (b > 200)
    
    # 白を透過（アルファを0に）
    a[white_mask] = 0
    
    # 黒い部分をカラーコード #D4AF37 に変更
    black_mask = (r < 50) & (g < 50) & (b < 50)
    r[black_mask] = 212
    g[black_mask] = 175
    b[black_mask] = 55
    
    # 画像を再構成
    new_image = cv2.merge((b, g, r, a))
    
    # 出力パスを設定
    output_path = output_dir / file_path.name
    cv2.imwrite(str(output_path), new_image)

def main():
    src_dir = Path('src')
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)
    
    for file in src_dir.glob("*.png"):
        process_image(file, output_dir)
    
if __name__ == '__main__':
    main()