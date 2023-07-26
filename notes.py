what = input("c circle,p parabolas,t tangent line, e for eclipse, h for hyperboles").strip(" ")
if what == "c":
    print("Circles are (x - h)^2 + (y-k)^2 = r^2\nif you are given in standard form remember to use perfect squares "
          "to factor")
elif what == "p":
    print("y=x^2|(x-h)^2=4p(y-k),focus is p, and if y^2 then it is horizontal,to find det is y=k-p|x=h-p")
elif what == "t":
    print("tan line is first get the distance of focus from point then go to the vertex and subtract/add with the "
          "value found")
elif what == "e":
    print("Horizontal form is (x-h)^2/a^2 + (y-k)^2/b^2 = 1, remember a > b, a + vertex = focus, C^2= A^2-B^2 is for "
          "distance to end,to find Eccentricy do e = c/a")
elif what == "h":
    print("(y-k)^2/a^2-(x-h)^2/b^2=1 is for vertical,everything is simular to eclipse, to find asymptotes horizontal: "
          "y=k+-b/a(x-h) or y=k+-a/b(x-h)")
