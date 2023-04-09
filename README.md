# Julia set Python generator with a Shiny front end.

Julia set fractals are generated by generating a complex number `z = x + yi`  where `x` and `y` are image pixel coordinates. `z` is repeatedly calculated using the iterative function <code>f(z) = z<sup>2</sup> + c</code>  where `c` is a complex parameter that generates a unique Julia set. 

This is a simple Shiny app that generates a Julia set fractal by providing a complex number parameter.

To setup, create a virtual environment and install the required libraries.
```
# Create a virtual environment in the .venv subdirectory
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install shiny, numpy and matplotlib
pip install shiny numpy matplotlib

```

To run the application
```
shiny run --reload
```
Then open browser to http://localhost:8000