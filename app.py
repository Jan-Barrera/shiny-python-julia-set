from shiny import App, render, ui
import numpy as np
from matplotlib import pyplot as plt, cm

app_ui = ui.page_fluid(
    ui.h2('Julia Set Generator'),
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_numeric('real_number', 'Real number', value=0.1),
            ui.input_numeric('imaginary_number', 'Imaginary number', value=1),
        ),
        ui.panel_main(
            ui.output_plot('julia_set')
        ),
    ),    
)

def server(input, output, session):
    @output
    @render.plot()
    def julia_set():
        real_number = input.real_number()
        imaginary_number = input.imaginary_number()
        c = complex(real_number, imaginary_number)
        width, height = 500, 500
        z_max = 5
        max_iter = 500
        xmin, xmax = -2, 2
        xwidth = xmax - xmin
        ymin, ymax = -2, 2
        yheight = ymax - ymin

        julia = np.zeros((width, height))

        for x in range(width):
            for y in range(height):
                i = 0
                z = complex(x / width * xwidth + xmin, y / height * yheight + ymin)

                while abs(z) <= z_max and i < max_iter:
                    z = z**2 + c
                    i += 1
                julia[x,y] = i / max_iter

        plt.imshow(julia, cmap=cm.magma)
        plt.axis('off')
        plt.title(get_title(real_number, imaginary_number), loc='left')
    

    def get_title(real, imaginary):
        if imaginary == 1:
            inumber = '+ '
        elif imaginary == -1:
            inumber = '- '
        elif imaginary >= 0:
            inumber = '+' + str(imaginary)
        else:
            inumber = str(imaginary)
        
        return f"f(z) = $z^{2}$ + ({real} {inumber}i)"

app = App(app_ui, server)
