#modulo gráfico
import turtle

def pintarTriangulo(coordenadas,miDibujo):
    # oculta el cursor
    miDibujo.hideturtle()
    miDibujo.up()
    miDibujo.goto(coordenadas[0][0],coordenadas[0][1])
    miDibujo.down()
    miDibujo.goto(coordenadas[1][0],coordenadas[1][1])
    miDibujo.goto(coordenadas[2][0],coordenadas[2][1])
    miDibujo.goto(coordenadas[0][0],coordenadas[0][1])

def dividirTriangulo(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def trianguloSierpinski(coordenadas,grado,miDibujo):
    # Aplica recursividad para realizar el fractal
    pintarTriangulo(coordenadas,miDibujo)
    if grado > 0:
        trianguloSierpinski([coordenadas[0],
                        dividirTriangulo(coordenadas[0], coordenadas[1]),
                        dividirTriangulo(coordenadas[0], coordenadas[2])],
                   grado-1, miDibujo)
        trianguloSierpinski([coordenadas[1],
                        dividirTriangulo(coordenadas[0], coordenadas[1]),
                        dividirTriangulo(coordenadas[1], coordenadas[2])],
                   grado-1, miDibujo)
        trianguloSierpinski([coordenadas[2],
                        dividirTriangulo(coordenadas[2], coordenadas[1]),
                        dividirTriangulo
                        (coordenadas[0], coordenadas[2])],
                   grado-1, miDibujo)

def main():
   #número de iteraciones
   print("Digite el numero de iteraciones del triangulo sierpinski")
   numero = int(input())

   miDibujo = turtle.Turtle()
   principal = turtle.Screen()
   
   #limitaciones del fractal en la ventana 
   misCoordenadas = [[-300,-150],[0,300],[300,-150]]
   trianguloSierpinski(misCoordenadas,numero,miDibujo)
   principal.exitonclick()

main()
