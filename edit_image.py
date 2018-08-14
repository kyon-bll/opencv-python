import cv2
import os

import image

# 引数解析
args = image.parser.parse_args()

# 画像読み込み
img = cv2.imread(args.input_img)

# 画像処理
if args.subcommand == 'rotate':
    dst, suffix = image.rotate(img, args.degree)

# 出力
basename = os.path.basename(args.input_img)
name, ext = os.path.splitext(basename)
filename = name + suffix + ext
cv2.imwrite('output/image/'+filename, dst)
