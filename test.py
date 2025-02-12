import ddddocr

# # 识别
# ocr = ddddocr.DdddOcr(old=True)
#
# with open('test.jpg', 'rb') as f:
#     img_bytes = f.read()
#
# res = ocr.classification(img_bytes)
# print(res)

# 目标检测
# det = ddddocr.DdddOcr(det=True)
#
# with open('微信图片_20220123122537.jpg', 'rb') as f:
#     img_bytes = f.read()
#
# res = det.detection(img_bytes)
# print(res)

# 滑块模板匹配方式
import cv2

im = cv2.imread("b.jpg")
det = ddddocr.DdddOcr(det=False, ocr=False)

with open('a.jpg', 'rb') as f:
    target_bytes = f.read()

with open('b.jpg', 'rb') as f:
    background_bytes = f.read()

res = det.slide_match(target_bytes, background_bytes, simple_target=True)
print(res)
x = res["target"]
print(x)
im = cv2.line(im, (int(x[0]), 0), (int(x[0]), 300), color=(0, 0, 255), thickness=2)
cv2.imwrite("res.jpg", im)

# det = ddddocr.DdddOcr(det=False, ocr=False)
#
# with open('bg.jpg', 'rb') as f:
#     target_bytes = f.read()
#
# with open('fullpage.jpg', 'rb') as f:
#     background_bytes = f.read()
#
#
# res = det.slide_comparison(target_bytes, background_bytes)
#
# print(res)
