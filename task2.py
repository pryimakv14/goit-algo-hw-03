import turtle
import argparse


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 2 / 3**0.5)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

    window.mainloop()


def parse_argv():
    parser = argparse.ArgumentParser(description="Малює сніжинку Коха")
    parser.add_argument(
        "-d", "--depth", type=int, default=2, help="Глибина сніжинки"
    )
    return parser.parse_args()


def run():
    args = parse_argv()
    draw_koch_snowflake(args.depth)


if __name__ == "__main__":
    run()
