#
# Script to pipe John Fields mod_logcurve.exe
# output into a text file : mod_logcurve_C++.txt.
# And also pipe the output into sharkteeth_deep.exe 
# which also outputs to a text file : sharkteeth_deep.txt
# Tim Toliver 11/11/14

# mod_logcurve usage :
# r0 is the starting radius and is oriented in the direction of 
# angle0(degrees)
# the curve will be drawn in angle space from angle0 to angle1 and it will 
# be made up of [count] straight
# line segments. If for some reason you want to generate the curve with a 
# fixed offset normal to the curve, e.g. a cutter radius or something like 
# that, you can add a final parameter [offset] which will do that for you.

# usage of sharkteeth :
# -d is the total depth of the tooth from tip to trough.
# -x (the 'defect') is the amount that the tooth descends below the 
# profile and should therefore be smaller than -d
# -r is a radius formed on the tooth. You can experiment with that
# -o means that the teeth will be evenly spaced in length along the profile 
# -e instead of -o, the teeth will be spaced evenly in angle around the profile.
# -n is the number of teeth to put on th profile
# -f is an optional file to read the input profile from. If not specified, 
# the program expects the profile to come from stdin - e.g. as in a pipe 
# from the output of mod_logcurve as in : see below

from os import system

# for mod_logcurve
r = .110  # start radius
a0 = -180   # start angle
a1 = 340 # end angle
s = 30  # number of segments
o = 0.0  # offset of curve for cutter comp

# for sharkteeth_deep
t = 9    # number of teeth to put on the profile
x = .009  # the amount the tooth descends below the profile
tr = .135 # the radius formed on the tooth
d = .015  # the total depth of the tooth from tip to trough

try:
    with open("mod_logcurve_C++.txt","w") as f:
        f.write("\n")
        f.write("(mod_logcurve_C++.txt)\n")
        f.write("(starting radius %.4f)\n" % r)
    with open("sharkteeth_deep.txt", "w") as f:
        f.write("\n")
        f.write("(sharkteeth_deep.txt)\n")
        f.write("(starting radius of mod_logcurve %.4f)\n" % r)
        f.write("(number of teeth : %d)\n" % t)
        
    # This is for Windows  !!!!!!!!!!
    # >> will append the output from mod_logcurve_C++.exe to mod_logcurve_C++.txt
    # unlike > which over writes the file with the output from mod_logcurve.exe
    # using the | will pipe the output from one program to the other
    system("mod_logcurve_C++ %f %d %d %d %f >> mod_logcurve_C++.txt" % (r, a0, a1, s, o))
    system("mod_logcurve_C++ %f %d %d %d %f | sharkteeth_deep -o -n %d -x %f -r %f -d %f >> sharkteeth_deep.txt" % (r, a0, a1, s, o, t, x, tr, d))
    
    
except TypeError as err:
    print(err)   

except IOError as err:
    print(err)
    
finally:
    print("finished!")    
