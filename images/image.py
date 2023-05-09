import discord
from PIL import Image, ImageDraw, ImageFont

async def create_image(user_id):
    # Connect to Discord API and fetch user information
    client = discord.Client()
    await client.start('TOKEN') # Replace 'TOKEN' with your bot's token
    user = await client.fetch_user(user_id)
    username = user.name
    avatar_url = user.avatar_url_as(size=256)

    # Load images
    image1 = Image.open('puchar.png')
    response = await client.http.get(avatar_url)
    image2 = Image.open(BytesIO(response.content))

    # Resize images
    image1 = image1.resize((2048, 2048))
    image2 = image2.resize((300, 300))

    # Create circular mask for image2
    mask = Image.new('L', (300, 300), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 300, 300), fill=255)

    # Paste circular image2 onto image1
    new_image = Image.new('RGB', (2048, 2048))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (875, 545), mask)

    # Add username to image
    draw = ImageDraw.Draw(new_image)
    font = ImageFont.truetype('arial.ttf', 34)
    text_width, _ = draw.textsize(username, font=font)
    draw.text((1024-text_width/2, 1470), username, font=font, fill=(0, 0, 0))

    # Save and display image
    new_image.save("merged_image.jpg", "JPEG")
    new_image.show()

    # Disconnect from Discord API
    await client.close()