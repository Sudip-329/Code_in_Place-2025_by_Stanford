from graphics import Canvas
import math

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_cloud(canvas, 10, 20, 'pink')
    draw_cloud(canvas, 140, 10, 'salmon')
    draw_cloud(canvas, 270, 20, 'purple')

    draw_tree(canvas, 50, 'saddlebrown', 'green')
    draw_tree(canvas, 120, 'saddlebrown', 'red')
    draw_tree(canvas, 280, 'saddlebrown', 'orange')

def draw_tree(canvas, center_x, trunk_color, leaves_color):
    """
    Draws a single tree centered at the given x-coordinate.
    The tree consists of a rectangular trunk and circular leaves.
    """
    trunk_left_x = center_x - TRUNK_WIDTH / 2
    trunk_right_x = center_x + TRUNK_WIDTH / 2
    trunk_top_y = TREE_BOTTOM_Y - TRUNK_HEIGHT
    
    canvas.create_rectangle(
        trunk_left_x,
        trunk_top_y,
        trunk_right_x,
        TREE_BOTTOM_Y,
        trunk_color
    )

    leaves_left_x = center_x - LEAVES_SIZE / 2
    leaves_right_x = center_x + LEAVES_SIZE / 2
    leaves_top_y = trunk_top_y - LEAVES_SIZE
    
    canvas.create_oval(
        leaves_left_x,
        leaves_top_y,
        leaves_right_x,
        trunk_top_y, 
        leaves_color
    )

def draw_cloud(canvas, x, y, color):
    """
    This function draws one cloud. You can call it and pass in
    different values of x and y (the location of the cloud) and
    color (the color of the cloud).
    """
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH
    canvas.create_oval(
        x,
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH,
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )

if __name__ == '__main__':
    main()