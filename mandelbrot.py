#!python
import png
import concurrent.futures
from datetime import datetime

nthreads = 4

minx = -2
maxx = 1
miny = -1.3
maxy = 1.3

resolutionx = 1000
resolutiony = 1000

png_data = []

def main():

    # Make the data structure and populate it with empty data
    for y in range(resolutiony):
        line_data = []
        for x in range(resolutionx) :
            line_data.append(0)
            line_data.append(0)
            line_data.append(0)
        png_data.append(line_data)

    # Set up an execution pool
    start_time = datetime.now()
    print("Started calculating")

    with concurrent.futures.ThreadPoolExecutor(max_workers=nthreads) as executor:
        executor.map(set_colour,get_coordinates(resolutionx,resolutiony))

    end_time = datetime.now()

    print(f"Using {nthreads} threads took {end_time-start_time} to calculate {resolutionx}x{resolutiony}")

    pngimage = png.from_array(png_data, mode="RGB")
    pngimage.save("test.png")


def get_coordinates(x_size,y_size):
    for x in range (x_size):
        for y in range(y_size):
            yield((x,y))





def set_colour(index_positions):

    x_index, y_index = index_positions

    x = minx + ((x_index/resolutionx) * (maxx-minx))
    y = miny + ((y_index/resolutiony) * (maxy-miny))

    limit=10
    real = x
    imag = y

    col=(0,0,0)
    for i in range(200):
        new_real = x + (real*real) - (imag*imag)
        new_imag = y + (imag*real) + (imag*real)

        if new_real > limit or new_imag > limit:
            col = (255-i,255-i,255-i)
            break
        
        real = new_real
        imag = new_imag
    
    
    png_data[y_index][x_index*3] = col[0]
    png_data[y_index][(x_index*3)+1] = col[1]
    png_data[y_index][(x_index*3)+2] = col[2]

        




if __name__ == "__main__":
    main()