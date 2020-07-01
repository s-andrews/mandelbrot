#!python
import png

def main():
    minx = -2
    maxx = 1
    miny = -1.3
    maxy = 1.3

    resolutionx = 10000
    resolutiony = 10000

    png_data = []

    for y in range(resolutiony):
        print(f"Line {y}")
        line_data = []
        yvalue = miny + (maxy-miny)*(y/resolutiony)
        for x in range(resolutionx) :
            xvalue = minx + (maxx-minx)*(x/resolutionx)

            r, g, b = get_colour(xvalue,yvalue)

            line_data.append(r)
            line_data.append(g)
            line_data.append(b)

        png_data.append(line_data)

    pngimage = png.from_array(png_data, mode="RGB")
    pngimage.save("test.png")


def get_colour(x,y):
    limit=10
    real = x
    imag = y

    for i in range(200):
        new_real = x + (real*real) - (imag*imag)
        new_imag = y + (imag*real) + (imag*real)

        if new_real > limit or new_imag > limit:
            return(255-i,255-i,255-i)
        
        real = new_real
        imag = new_imag
    
    return(0,0,0)

        




if __name__ == "__main__":
    main()