from ledstripcontroller import LedStripController
from encoder import Encoder

def main():

    enc = Encoder(pin_clk=13, pin_dt=12, pin_mode=Pin.PULL_UP,
                  min_val=40, max_val=1020, clicks=1, accel=5)
    enc._value = 1020

    controller = LedStripController(enc)
    controller.run()


if __name__ == '__main__':
    main()
