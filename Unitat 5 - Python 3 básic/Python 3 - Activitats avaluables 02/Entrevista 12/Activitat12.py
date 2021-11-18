# adds image processing capabilities
from PIL import Image
# will convert the image to text string
import pytesseract

# assigning an image from the source path
# ADD PIC
img = Image.open('image_test/virginia-quote.jpg')
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)

with open('text_result.txt', mode ='w') as file:
 file.write(result)
 print("ready!")

