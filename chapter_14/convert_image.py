from io import BytesIO
from PIL import Image
import sys

def data_to_img(data):
    """메모리 내의 <data>에서 PIL이미지 객체를 반환한다."""
    fp = BytesIO(data)
    return Image.open(fp)

def img_to_data(img, fmt=None):
    """<fmt> 형식의 PIL 이미지 <img>에서 이미지 데이터를 반환한다."""
    fp = BytesIO()
    if not fmt:
        fmt = img.format # 원본 형식을 유지한다.
        img.save(fp, fmt) # 메모리에 쓴다.
    return fp.getvalue()

def convert_image(data, fmt=None):
    """이미지 <data>를 PIL <fmt> 이미지 데이터로 변환한다."""
    img = data_to_img(data)
    return img_to_data(img, fmt)

def get_file_data(name: str):
    """이미지 파일 <name>에 대한 PIL 이미지 객체를 반환한다."""
    img = Image.open(name)
    print("img", img, img.format)
    return img_to_data(img)

if __name__ = "__main__"":
    for name in sys.argv[1:]:
        data = get_file_data(name)
        print("in", len(data), data[:10])
        for fmt in ("gif", "png", "jpeg"):
            out_data = convert_image(data, fmt)
            print("out", len(out_data), out_data[:10])