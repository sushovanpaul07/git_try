#importing required librarie(S)
import pyautogui as pg


available_colors=[[0, 0, 0, 'black'], [0, 0, 128, 'navy'], [0, 0, 139, 'darkblue'], [0, 0, 205, 'mediumblue'], [0, 0, 255, 'blue'], [0, 100, 0, 'darkgreen'], [0, 128, 0, 'green'], [0, 128, 128, 'teal'], [0, 139, 139, 'darkcyan'], [0, 191, 255, 'deepskyblue'], [0, 206, 209, 'darkturquoise'], [0, 250, 154, 'mediumspringgreen'], [0, 255, 0, 'lime'], [0, 255, 127, 'springgreen'], [0, 255, 255, 'cyan'], [25, 25, 112, 'midnightblue'], [30, 144, 255, 'dodgerblue'], [32, 178, 170, 'lightseagreen'], [34, 139, 34, 'forestgreen'], [46, 139, 87, 'seagreen'], [47, 79, 79, 'darkslategrey'], [50, 205, 50, 'limegreen'], [60, 179, 113, 'mediumseagreen'], [64, 224, 208, 'turquoise'], [65, 105, 225, 'royalblue'], [70, 130, 180, 'steelblue'], [72, 61, 139, 'darkslateblue'], [72, 209, 204, 'mediumturquoise'], [75, 0, 130, 'indigo'], [85, 107, 47, 'darkolivegreen'], [95, 158, 160, 'cadetblue'], [100, 149, 237, 'cornflowerblue'], [102, 205, 170, 'mediumaquamarine'], [105, 105, 105, 'dimgrey'], [106, 90, 205, 'slateblue'], [107, 142, 35, 'olivedrab'], [112, 128, 144, 'slategrey'], [119, 136, 153, 'lightslategrey'], [123, 104, 238, 'mediumslateblue'], [124, 252, 0, 'lawngreen'], [127, 255, 0, 'chartreuse'], [127, 255, 212, 'aquamarine'], [128, 0, 0, 'maroon'], [128, 0, 128, 'purple'], [128, 128, 0, 'olive'], [128, 128, 128, 'grey'], [135, 206, 235, 'skyblue'], [135, 206, 250, 'lightskyblue'], [138, 43, 226, 'blueviolet'], [139, 0, 0, 'darkred'], [139, 0, 139, 'darkmagenta'], [139, 69, 19, 'saddlebrown'], [143, 188, 143, 'darkseagreen'], [144, 238, 144, 'lightgreen'], [147, 112, 216, 'mediumpurple'], [148, 0, 211, 'darkviolet'], [152, 251, 152, 'palegreen'], [153, 50, 204, 'darkorchid'], [154, 205, 50, 'yellowgreen'], [160, 82, 45, 'sienna'], [165, 42, 42, 'brown'], [169, 169, 169, 'darkgrey'], [173, 216, 230, 'lightblue'], [173, 255, 47, 'greenyellow'], [175, 238, 238, 'paleturquoise'], [176, 196, 222, 'lightsteelblue'], [176, 224, 230, 'powderblue'], [178, 34, 34, 'firebrick'], [184, 134, 11, 'darkgoldenrod'], [186, 85, 211, 'mediumorchid'], [188, 143, 143, 'rosybrown'], [189, 183, 107, 'darkkhaki'], [192, 192, 192, 'silver'], [199, 21, 133, 'mediumvioletred'], [205, 92, 92, 'indianred'], [205, 133, 63, 'peru'], [210, 105, 30, 'chocolate'], [210, 180, 140, 'tan'], [211, 211, 211, 'lightgrey'], [216, 112, 147, 'palevioletred'], [216, 191, 216, 'thistle'], [218, 112, 214, 'orchid'], [218, 165, 32, 'goldenrod'], [220, 20, 60, 'crimson'], [220, 220, 220, 'gainsboro'], [221, 160, 221, 'plum'], [222, 184, 135, 'burlywood'], [224, 255, 255, 'lightcyan'], [230, 230, 250, 'lavender'], [233, 150, 122, 'darksalmon'], [238, 130, 238, 'violet'], [238, 232, 170, 'palegoldenrod'], [240, 128, 128, 'lightcoral'], [240, 230, 140, 'khaki'], [240, 248, 255, 'aliceblue'], [240, 255, 240, 'honeydew'], [240, 255, 255, 'azure'], [244, 164, 96, 'sandybrown'], [245, 222, 179, 'wheat'], [245, 245, 220, 'beige'], [245, 245, 245, 'whitesmoke'], [245, 255, 250, 'mintcream'], [248, 248, 255, 'ghostwhite'], [250, 128, 114, 'salmon'], [250, 235, 215, 'antiquewhite'], [250, 240, 230, 'linen'], [250, 250, 210, 'lightgoldenrodyellow'], [253, 245, 230, 'oldlace'], [255, 0, 0, 'red'], [255, 0, 255, 'magenta'], [255, 20, 147, 'deeppink'], [255, 69, 0, 'orangered'], [255, 99, 71, 'tomato'], [255, 105, 180, 'hotpink'], [255, 127, 80, 'coral'], [255, 140, 0, 'darkorange'], [255, 160, 122, 'lightsalmon'], [255, 165, 0, 'orange'], [255, 182, 193, 'lightpink'], [255, 192, 203, 'pink'], [255, 215, 0, 'gold'], [255, 218, 185, 'peachpuff'], [255, 222, 173, 'navajowhite'], [255, 228, 181, 'moccasin'], [255, 228, 196, 'bisque'], [255, 228, 225, 'mistyrose'], [255, 235, 205, 'blanchedalmond'], [255, 239, 213, 'papayawhip'], [255, 240, 245, 'lavenderblush'], [255, 245, 238, 'seashell'], [255, 248, 220, 'cornsilk'], [255, 250, 205, 'lemonchiffon'], [255, 250, 240, 'floralwhite'], [255, 250, 250, 'snow'], [255, 255, 0, 'yellow'], [255, 255, 224, 'lightyellow'], [255, 255, 240, 'ivory'], [255, 255, 255, 'white']]



# Function to detect the nearest possible color name
# form the array of available colors

def nearest_color(r,g,b):
    index=0
    color=""
    for i in available_colors:
        index+=1
        if i[0]>=r:
            break
    g_ar=available_colors[index-1:]
    index1=0
    for j in g_ar:
        index1+=1
        if j[1]>=g:
            break
    b_ar=g_ar[index1-1:]
    index2=0
    for k in b_ar:
        index2+=1
        if k[2]>=b:
            color=k[3]
            break
    return b_ar[index2-1]

# Loop to continuously detect the position of
# mouse pointer and return the co-ordinates
# then call the pixel method to get the RGB
# value of the color of the respective pixel
# then pass it to the nearest finding method
# to get the name of the nearest color


while True:
    xval,yval=pg.position()
    try:
        r,g,b=pg.pixel(xval,yval)
        requested_colour = nearest_color(r,g,b)
        print(requested_colour[3])
    except:
        print("Not Found")