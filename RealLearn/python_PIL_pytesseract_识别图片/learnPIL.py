from PIL import Image, ImageFilter

im = Image.open('e:\Desktop\图片\原图.jpg')

# 图片尺寸
width,high = im.size
print(width)
print(high)

# 缩略
width_new = width/2
high_new = high/2
im.thumbnail((width_new, high_new))
print(width_new)
print(high_new)
# 保存
im.save('e:\Desktop\图片\缩略.jpg', 'jpeg')

# 模糊处理
im2 = im.filter(ImageFilter.BLUR)
# 保存
im2.save('e:\Desktop\图片\模糊.jpg', 'jpeg')
