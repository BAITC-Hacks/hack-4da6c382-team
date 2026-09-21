from PIL import Image, ImageDraw

W, H = 400, 400


def base() -> Image.Image:
    img = Image.new("RGB", (W, H), (230, 230, 230))
    d = ImageDraw.Draw(img)
    d.ellipse((60, 60, 340, 340), fill=(120, 130, 140))
    d.ellipse((160, 160, 240, 240), fill=(230, 230, 230))
    return img


ok = base()
ok.save("ok.png")

defect = base()
d = ImageDraw.Draw(defect)
d.ellipse((220, 90, 300, 170), fill=(200, 20, 20))
d.line((110, 250, 200, 310), fill=(210, 30, 30), width=8)
defect.save("defect.png")

print("Созданы ok.png и defect.png")
