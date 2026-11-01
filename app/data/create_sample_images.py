"""Generates high-definition botanical sample images for 1-click testing of AI detection.
Creates realistic leaf patterns for healthy crops, fungal blights, bacterial spots,
pest infestations, and an unsupported out-of-distribution sample.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import math
import random

SAMPLE_DIR = Path(__file__).resolve().parent / "sample_images"
SAMPLE_DIR.mkdir(parents=True, exist_ok=True)


def create_rice_healthy():
    img = Image.new("RGB", (512, 512), (34, 139, 34))
    draw = ImageDraw.Draw(img)
    # Long parallel veins of monocot rice leaf
    for x in range(0, 512, 6):
        draw.line([(x, 0), (x, 512)], fill=(46, 160, 46), width=2)
    # Highlight midrib
    draw.line([(256, 0), (256, 512)], fill=(70, 190, 70), width=6)
    # Smooth organic gradient
    img = img.filter(ImageFilter.GaussianBlur(1.0))
    img.save(SAMPLE_DIR / "sample_rice_healthy.jpg", quality=95)
    print("Created sample_rice_healthy.jpg")


def create_potato_late_blight():
    img = Image.new("RGB", (512, 512), (40, 110, 40))
    draw = ImageDraw.Draw(img)
    # Solanaceous potato leaf network
    for i in range(10):
        y = 50 + i * 45
        draw.line([(256, y), (100, y - 30)], fill=(30, 95, 30), width=3)
        draw.line([(256, y), (412, y - 30)], fill=(30, 95, 30), width=3)
    # Large water-soaked irregular dark necrotic late blight lesions
    draw.ellipse([140, 150, 320, 310], fill=(45, 30, 20), outline=(180, 175, 165), width=8)
    draw.ellipse([280, 260, 440, 410], fill=(50, 32, 22), outline=(190, 185, 175), width=7)
    draw.ellipse([80, 330, 210, 440], fill=(42, 28, 18), outline=(175, 170, 160), width=6)
    img = img.filter(ImageFilter.GaussianBlur(1.5))
    img.save(SAMPLE_DIR / "sample_potato_late_blight.jpg", quality=95)
    print("Created sample_potato_late_blight.jpg")


def create_tomato_early_blight():
    img = Image.new("RGB", (512, 512), (55, 130, 45))
    draw = ImageDraw.Draw(img)
    # Distinctive concentric target rings (bullseye) of Alternaria solani
    center_x, center_y = 230, 240
    # Yellow chlorotic halo around lesion
    draw.ellipse([center_x - 140, center_y - 140, center_x + 140, center_y + 140], fill=(160, 155, 30))
    # Concentric rings
    colors = [(60, 40, 20), (100, 70, 35), (55, 35, 18), (110, 75, 40), (45, 25, 15)]
    for r, col in zip([110, 85, 60, 40, 20], colors):
        draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r], fill=col)
    
    # Secondary smaller target lesion
    c2_x, c2_y = 380, 360
    draw.ellipse([c2_x - 70, c2_y - 70, c2_x + 70, c2_y + 70], fill=(150, 145, 35))
    for r, col in zip([55, 40, 25, 12], colors):
        draw.ellipse([c2_x - r, c2_y - r, c2_x + r, c2_y + r], fill=col)

    img = img.filter(ImageFilter.GaussianBlur(1.2))
    img.save(SAMPLE_DIR / "sample_tomato_early_blight.jpg", quality=95)
    print("Created sample_tomato_early_blight.jpg")


def create_cotton_aphids():
    img = Image.new("RGB", (512, 512), (65, 135, 50))
    draw = ImageDraw.Draw(img)
    # Cotton palmate veins
    draw.line([(256, 512), (256, 50)], fill=(50, 110, 40), width=7)
    draw.line([(256, 350), (80, 120)], fill=(50, 110, 40), width=5)
    draw.line([(256, 350), (432, 120)], fill=(50, 110, 40), width=5)
    # Sticky honeydew sheen + cluster of hundreds of small yellowish-green aphids
    random.seed(101)
    for _ in range(250):
        ax = random.randint(180, 360) + int(random.gauss(0, 35))
        ay = random.randint(120, 380) + int(random.gauss(0, 35))
        # Tiny pear-shaped aphid body
        draw.ellipse([ax - 4, ay - 6, ax + 4, ay + 6], fill=(175, 195, 45), outline=(130, 150, 30))
        # Eyes
        draw.point((ax - 2, ay - 5), fill=(40, 20, 10))
        draw.point((ax + 2, ay - 5), fill=(40, 20, 10))
    # Black sooty mold patches
    draw.ellipse([300, 350, 420, 440], fill=(30, 35, 30))
    img = img.filter(ImageFilter.GaussianBlur(0.8))
    img.save(SAMPLE_DIR / "sample_cotton_aphids.jpg", quality=95)
    print("Created sample_cotton_aphids.jpg")


def create_maize_fall_armyworm():
    img = Image.new("RGB", (512, 512), (50, 130, 40))
    draw = ImageDraw.Draw(img)
    # Broad parallel corn leaf
    for x in range(0, 512, 8):
        draw.line([(x, 0), (x, 512)], fill=(58, 145, 48), width=2)
    draw.line([(256, 0), (256, 512)], fill=(90, 180, 80), width=10)
    # Ragged chewed shotgun holes
    draw.polygon([(150, 180), (220, 160), (240, 230), (180, 260), (130, 210)], fill=(30, 25, 20))
    draw.polygon([(290, 260), (380, 240), (390, 320), (330, 350), (280, 300)], fill=(30, 25, 20))
    # Coarse moist sawdust-like fecal frass clusters
    random.seed(42)
    for _ in range(80):
        fx = random.randint(160, 230)
        fy = random.randint(200, 270)
        draw.ellipse([fx - 3, fy - 3, fx + 3, fy + 3], fill=(130, 100, 50))
    # Feeding caterpillar body on leaf margin
    c_pts = [(160, 320), (180, 340), (205, 370), (225, 410)]
    draw.line(c_pts, fill=(70, 80, 50), width=16)
    # Head capsule with inverted Y
    draw.ellipse([220, 405, 238, 423], fill=(30, 25, 20))
    img = img.filter(ImageFilter.GaussianBlur(1.0))
    img.save(SAMPLE_DIR / "sample_maize_fall_armyworm.jpg", quality=95)
    print("Created sample_maize_fall_armyworm.jpg")


def create_rice_bacterial_leaf_blight():
    img = Image.new("RGB", (512, 512), (45, 135, 45))
    draw = ImageDraw.Draw(img)
    # Rice leaf parallel veins
    for x in range(0, 512, 6):
        draw.line([(x, 0), (x, 512)], fill=(55, 150, 55), width=2)
    # Wavy yellowish-white marginal blight lesions
    wavy_left = [(0, 0), (70, 80), (40, 160), (90, 260), (50, 360), (80, 460), (0, 512)]
    draw.polygon(wavy_left, fill=(210, 200, 130))
    wavy_right = [(512, 0), (440, 90), (470, 180), (420, 290), (460, 390), (430, 480), (512, 512)]
    draw.polygon(wavy_right, fill=(215, 205, 135))
    # Dried amber bacterial ooze droplets
    for ox, oy in [(85, 260), (415, 295), (65, 165), (445, 185)]:
        draw.ellipse([ox - 4, oy - 4, ox + 4, oy + 4], fill=(220, 140, 30))
    img = img.filter(ImageFilter.GaussianBlur(1.2))
    img.save(SAMPLE_DIR / "sample_rice_bacterial_blight.jpg", quality=95)
    print("Created sample_rice_bacterial_blight.jpg")


def create_unsupported_sample():
    # A non-plant, non-crop image: modern blue metallic keyboard/laptop surface
    img = Image.new("RGB", (512, 512), (28, 45, 75))
    draw = ImageDraw.Draw(img)
    # Metallic gradient lines and geometric keys
    for i in range(5):
        for j in range(5):
            x1, y1 = 50 + i * 85, 50 + j * 85
            draw.rectangle([x1, y1, x1 + 65, y1 + 65], fill=(45, 70, 110), outline=(70, 100, 160), width=2)
    img = img.filter(ImageFilter.GaussianBlur(0.8))
    img.save(SAMPLE_DIR / "sample_unsupported_object.jpg", quality=95)
    print("Created sample_unsupported_object.jpg")


if __name__ == "__main__":
    create_rice_healthy()
    create_potato_late_blight()
    create_tomato_early_blight()
    create_cotton_aphids()
    create_maize_fall_armyworm()
    create_rice_bacterial_leaf_blight()
    create_unsupported_sample()
    print("All sample images generated successfully in app/data/sample_images/")
