import random

def on_heads_click():
    global background_color, text_display
    text_display = "you chose heads"
    background_color = "#ff0000"
    print(text_display, background_color)

def on_tails_click():
    global background_color, text_display
    text_display = "you chose tails"
    background_color = "#00ff00"
    print(text_display, background_color)

heads = "heads"
tails = "tails"

background_color = "#ffffff"
text_display = "choose heads or tails"

heads_button = {
    "text": "heads",
    "on_click": on_heads_click
}

tails_button = {
    "text": "tails",
    "on_click": on_tails_click
}

r1 = random.randint(1, 2)

if r1 == 1:
    text_display = "the coin landed on heads"
    background_color = "#ff0000"
else:
    text_display = "the coin landed on tails"
    background_color = "#00ff00"

print(text_display)
