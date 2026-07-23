import math;
import numpy;
import matplotlib.pyplot as plt;

def lambert_function_curve():
    x=numpy.linspace(-10,100,1000)
    power_part=numpy.exp(x)
    y=power_part*x
    plt.plot(x,y,label="Lambert function curve",linestyle="-",color="red")
    plt.legend()
    plt.show()
  

# lambert_function_curve()

def lambert_inverse(output_searched:float):
    y=0
    denseness=0.001
    x=0
    while(y<output_searched):
        x+=denseness
        pw=math.exp(x)
        y=x*pw
    return x

print(lambert_inverse(12))

         
         



    

