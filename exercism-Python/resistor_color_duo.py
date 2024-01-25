def value(colors):
    band_color = {"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9,}
    num = 0
    for i in range(2):
        num = num * 10 + band_color[colors[i]]
    return num

