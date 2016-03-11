from PIL import Image, ImageDraw
import random


im = Image.new("RGB", (1024,1024), "white") #create 1024*1024 image
x = range (20)
y = range (20)
r = range (20)
for i in range (0,20):   #create 20 random circles (save in lists)
 x[i] = random.randint(1,1024)
 y[i] =random.randint(1,1024)
 r[i] = random.randint(10,500)

 
 draw = ImageDraw.Draw(im)
 draw.ellipse((x[i]-r[i], y[i]-r[i], x[i]+r[i], y[i]+r[i]), fill=(255,255,0), outline ='red')
 im.save("image.png","PNG")


count=0  
for i in range (0,20):  #check how many circles intersect
 for j in range (0,20):
  if (i==j): pass
  else:
      if ((r[i]-r[j])**2 <= ( (x[i]-x[j])**2 + (y[i]-y[j])**2) and ( (x[i]-x[j])**2 + (y[i]-y[j])**2) <= (r[i]+r[j])**2):
          count +=1
          break
      

im.show()

print count

