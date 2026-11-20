from PIL import Image, ImageDraw, ImageFont
import os

def create_image():
    width, height = 1024, 1024
    bg_color = (18, 18, 18)  # Dark background
    text_color = (240, 240, 240)
    accent_color = (200, 200, 200)
    card_bg = (30, 30, 30)
    
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Fonts - reduced sizes to prevent clipping
    try:
        font_header = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 54)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
        font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
        font_footer = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
    except:
        font_header = font_title = font_body = font_footer = ImageFont.load_default()

    # Header
    header_text = "Wednesday 19 November 2026"
    draw.text((width//2, 80), header_text, fill=text_color, font=font_header, anchor="mm")
    draw.line([60, 140, 964, 140], fill=accent_color, width=3)

    # Story Cards (2x2 grid)
    stories = [
        {
            "title": "SHENZHEN SUMMIT",
            "body": "Trump, Xi, Putin hold first trilateral summit; 'Declaration toward peace' signed.",
            "icon": "summit"
        },
        {
            "title": "ICJ: MYANMAR GENOCIDE",
            "body": "UN top court finds Myanmar committed genocide against the Rohingya people.",
            "icon": "justice"
        },
        {
            "title": "KERCH BRIDGE STRUCK",
            "body": "Ukraine strikes Kerch bridge; Europe rejects 'Yalta 2.0' peace framework.",
            "icon": "war"
        },
        {
            "title": "ANTHROPIC IPO",
            "body": "Claude creator debuts at $111.50; largest IPO in history, nears $2T value.",
            "icon": "tech"
        }
    ]

    card_w, card_h = 440, 320
    # Adjusted positions for better margins
    positions = [(50, 180), (534, 180), (50, 540), (534, 540)]

    for i, story in enumerate(stories):
        x, y = positions[i]
        # Card Background
        draw.rounded_rectangle([x, y, x+card_w, y+card_h], radius=15, fill=card_bg)
        
        # Simple Icons
        icon_x, icon_y = x + 30, y + 30
        if story["icon"] == "summit":
            draw.ellipse([icon_x, icon_y, icon_x+40, icon_y+40], outline="white", width=3)
            draw.ellipse([icon_x+25, icon_y, icon_x+65, icon_y+40], outline="white", width=3)
            draw.ellipse([icon_x+12, icon_y+20, icon_x+52, icon_y+60], outline="white", width=3)
        elif story["icon"] == "justice":
            draw.line([icon_x, icon_y+40, icon_x+60, icon_y+40], fill="white", width=4)
            draw.line([icon_x+30, icon_y, icon_x+30, icon_y+50], fill="white", width=4)
            draw.line([icon_x+10, icon_y+10, icon_x+50, icon_y+10], fill="white", width=4)
        elif story["icon"] == "war":
            draw.line([icon_x, icon_y+40, icon_x+25, icon_y+40], fill="white", width=5)
            draw.line([icon_x+35, icon_y+40, icon_x+60, icon_y+40], fill="white", width=5)
            draw.polygon([icon_x+25, icon_y+40, icon_x+30, icon_y+20, icon_x+35, icon_y+40], fill="red")
        elif story["icon"] == "tech":
            draw.line([icon_x+10, icon_y+50, icon_x+30, icon_y+10, icon_x+50, icon_y+50], fill="white", width=5)
            draw.line([icon_x+20, icon_y+35, icon_x+40, icon_y+35], fill="white", width=5)

        # Title
        draw.text((x + 30, y + 100), story["title"], fill=text_color, font=font_title)
        
        # Body (wrapped manually)
        words = story["body"].split()
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            w = draw.textlength(test_line, font=font_body)
            if w < card_w - 60:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)
        
        for j, line in enumerate(lines[:3]):
            draw.text((x + 30, y + 150 + j*35), line.strip(), fill=accent_color, font=font_body)

    # Footer
    footer_text = "DIPLOMACY - JUSTICE - WAR - MARKETS"
    draw.text((width//2, 940), footer_text, fill=text_color, font=font_footer, anchor="mm")
    
    # Save image
    img.save("/home/agentuser/news19/entry.png", "PNG", optimize=True)

if __name__ == "__main__":
    create_image()
