from PIL import Image

# 入力画像と出力画像のパス
input_path = "src/og-image.jpg"
output_path = "output/og-image.jpg"

# 目標サイズ
target_width = 1200
target_height = 630
target_aspect_ratio = target_width / target_height

# 画像を開く
image = Image.open(input_path)
orig_width, orig_height = image.size
orig_aspect_ratio = orig_width / orig_height

# クロップ範囲を計算
if orig_aspect_ratio > target_aspect_ratio:
    # 横長の場合、左右をクロップ
    new_width = int(orig_height * target_aspect_ratio)
    offset = (orig_width - new_width) // 2
    crop_box = (offset, 0, offset + new_width, orig_height)
else:
    # 縦長の場合、上下をクロップ
    new_height = int(orig_width / target_aspect_ratio)
    offset = (orig_height - new_height) // 2
    crop_box = (0, offset, orig_width, offset + new_height)

# 画像をクロップしてリサイズ
cropped_image = image.crop(crop_box).resize((target_width, target_height), Image.LANCZOS)

# 保存
cropped_image.save(output_path, quality=95)
