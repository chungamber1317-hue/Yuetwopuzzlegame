from PIL import Image
import requests
from io import BytesIO

# 图片URL
IMAGE_URL = "https://p26-flow-imagex-download-sign.byteimg.com/tos-cn-i-a9rns2rl98/50e6c6fbe58e4c1a9d13233f04ec5bdd.png~tplv-a9rns2rl98-24:720:720.png?rcl=20251104160644A49CF6C05D6FC7D91ACC&rk3s=8e244e95&rrcfp=8a172a1a&x-expires=1762848404&x-signature=1LqMcyJPChwDqHhi0EpWtcgaSI4%3D"

# 拼图配置
ROWS = 3
COLS = 3

def download_image(url):
    """下载图片"""
    response = requests.get(url)
    response.raise_for_status()  # 如果请求失败，抛出异常
    return Image.open(BytesIO(response.content))

def generate_puzzle_pieces(image_path, rows, cols):
    """
    生成拼图碎片
    
    Args:
        image_path: 原始图片路径或URL
        rows: 行数
        cols: 列数
    """
    # 下载图片
    image = download_image(image_path)
    
    # 获取图片尺寸
    width, height = image.size
    
    # 计算每个碎片的大小
    piece_width = width // cols
    piece_height = height // rows
    
    # 创建碎片
    pieces = []
    for row in range(rows):
        for col in range(cols):
            # 计算碎片的坐标
            left = col * piece_width
            top = row * piece_height
            right = left + piece_width
            bottom = top + piece_height
            
            # 裁剪碎片
            piece = image.crop((left, top, right, bottom))
            
            # 保存碎片
            piece_filename = f"images/puzzle-piece-{row * cols + col}.png"
            piece.save(piece_filename)
            pieces.append(piece_filename)
            print(f"已生成碎片: {piece_filename}")
    
    return pieces

if __name__ == "__main__":
    print("开始生成拼图碎片...")
    try:
        generate_puzzle_pieces(IMAGE_URL, ROWS, COLS)
        print("拼图碎片生成完成！")
    except Exception as e:
        print(f"生成拼图碎片时出错: {e}")
