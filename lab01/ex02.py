lights_mode_auto = True
is_day = False
is_rain = False
is_fog = False
lights = False


def checkLights():
    global lights
    if lights_mode_auto:
        if not is_day or is_rain or is_fog:
            lights = True


def lightsStatus(lights):
    if lights:
        print("LIGHTS ON")
    else:
        print("LIGHTS OFF")


checkLights()
lightsStatus(lights)
