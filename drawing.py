from turtle import Screen, Turtle
from pixart_start import initialization,draw_line_from_string,draw_shape_from_string,draw_shape_from_file
turta = Turtle()
PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'
TURN = 90
turta.speed(0)

def main():
    initialization(turta)
    draw_line_from_string('01A753421', turta)
    turta.hideturtle()
    input("Press Enter to clear: ")
    turta.clear()
    input("Press any key to continue the process: ")
    initialization(turta)
    draw_shape_from_string(turta)
    turta.hideturtle()
    turta.clear()
    initialization(turta)
    file_name = input("Enter file path with the color codes: ")
    draw_shape_from_file(file_name)
    turta.hideturtle()
    input("Press any key to exit: ")
if __name__ == "__main__":
    main()
#Color code for the first row is: 02020202020202020202. Then on the second row: 20202020202020202020