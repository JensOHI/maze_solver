import cv2
import numpy as np
import tkinter as tk

import utilities as utils
import settings
import zoom




def find_square_based_on_pixel(image, pixel):
    # This is in pixels.
    n = 2
    e = 2
    s = 2
    w = 2
    n_white = True
    e_white = True
    s_white = True
    w_white = True
    while n_white or e_white or s_white or w_white:
        x0 = pixel[0]-w
        y0 = pixel[1]-n
        x1 = pixel[0]+e
        y1 = pixel[1]+s
        print(x0, y0, x1, y1)
        sub_image = image[y0:y1, x0:x1]
        print(sub_image)
        n_white = True if np.mean(sub_image[0,1:-1]) >= 255 else False
        e_white = True if np.mean(sub_image[1:-1,-1]) >= 255 else False
        s_white = True if np.mean(sub_image[-1,1:-1]) >= 255 else False
        w_white = True if np.mean(sub_image[1:-1,0]) >= 255 else False
        print(n_white, e_white, s_white, w_white)
        n += 1 if n_white else 0
        e += 1 if e_white else 0
        s += 1 if s_white else 0
        w += 1 if w_white else 0


        if (not n_white and not s_white and (n+s) == (w+e)) or (not w_white and not e_white and (n+s) == (w+e)):
            break
        #if (not n_white and not s_white) or (not w_white and not e_white):
           # break
     
    print(n, e, s, w)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    image = cv2.circle(image, pixel, 2, (0,0,255), -1)
    return cv2.rectangle(image, (x0, y0), (x1, y1), (255,0,0), 1)
    




# Start and end location on image
START_PLACEMENT = [2000, 3252]#[98, 3515]
END_PLACEMENT = None

def main():
    settings.init()

    filename = "maze_page-0.png"
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    for i in range(10):
        START_PLACEMENT = [np.random.randint(image.shape[0]), np.random.randint(image.shape[1])]
        image_rgb = find_square_based_on_pixel(image, START_PLACEMENT) #cv2.circle(image, START_PLACEMENT, 2, (255,0,0), -1)

        temp_image_name = "temp.png"
        cv2.imwrite(temp_image_name, image_rgb)



        app = zoom.MainWindow(tk.Tk(), path=temp_image_name)
        app.mainloop()

    # image = cv2.circle(image, settings.START_PLACEMENT, 50, (0,0,255), -1)
    # image = cv2.circle(image, settings.END_PLACEMENT, 50, (0,0,255), -1)
    # resize_variable = np.floor(np.max(image.shape)/np.min([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT]))
    # cv2.imshow("Image", cv2.resize(image, (image.shape/resize_variable).astype(int)))
    # cv2.waitKey()






if __name__=="__main__":
    #utils.convert_pdf_to_image("maze.pdf")
    main()
    