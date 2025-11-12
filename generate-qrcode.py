import qrcode
from PIL import Image
import sys

def generate_qrcode(url, output_file="game-qrcode.png"):
    """
    生成二维码图片
    
    Args:
        url: 要编码的URL
        output_file: 输出文件名
    """
    try:
        # 创建二维码对象
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        # 添加URL
        qr.add_data(url)
        qr.make(fit=True)
        
        # 创建二维码图片
        img = qr.make_image(fill_color="black", back_color="white")
        
        # 保存图片
        img.save(output_file)
        print(f"二维码已生成：{output_file}")
        
        return output_file
        
    except Exception as e:
        print(f"生成二维码时出错：{e}")
        return None

if __name__ == "__main__":
    # 默认URL（请替换为您实际部署游戏的网址）
    default_url = "http://localhost:8000"
    
    # 如果提供了命令行参数，则使用提供的URL
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = default_url
        print(f"未提供URL，使用默认值：{url}")
        print("提示：您可以运行 'python generate-qrcode.py 您的网址' 来生成自定义二维码")
    
    # 生成二维码
    generate_qrcode(url)
