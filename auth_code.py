from PIL import Image

im = Image.open('get_img.jpg')

imgry = im.convert('L')
# imgry.show()

threshold = 130
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
# out.show()

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
print(pytesseract.image_to_string(Image.open('get_img.jpg')))
print(pytesseract.image_to_string(Image.open('get_img.jpg'), lang='fra'))

# import pytesser
# # from PIL import pytesser
# print pytesser.image_file_to_string('get_img.jpg')
# print pytesser.image_to_string(im)

