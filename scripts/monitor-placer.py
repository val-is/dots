try:
    import argparse
    import os
    import subprocess
    import time
    import yaml

except Exception as e:
    print("ono")

# this is a super hardware specific method of setting my monitors the way I want
# really not portable at all tbh

def get_screens(disable_laptop: bool):
    """
    returns active screens in order from smallest to largest
    """
    # https://askubuntu.com/questions/639495/how-can-i-list-connected-monitors-with-xrandr
    screens_raw = [l for l in subprocess.check_output(["xrandr", "--listactivemonitors"]).decode("utf-8").splitlines()][1:]
    screens = []
    for screen in screens_raw:
        data = screen.split()
        name = "".join([c for c in data[-1] if c not in "+*"])
        res = [int(i.split('/')[0]) for i in data[-2].split('x')]
        # screen struct looks like
        # ["DP-1", [2560, 1440], disabled], ...
        if name == "eDP-1": # drop internal monitor
            continue
        screens.append([name, res, False])

    # sort displays to get ordering (largest on the left)
    screens = sorted(screens, key=lambda x: x[1][0])#[::-1]
    
    if len(screens) == 0:
        # external monitors not connected
        return [["eDP-1", [1920, 1080], False]]
    else:
        screens.append(["eDP-1", [1920, 1080], disable_laptop])

    return screens

def place_screens(screens) -> None:
    # generate xrandr command to order monitors if there are more than one
    enabled_screens = [i for i in screens if not i[2]][::-1]
    command = "xrandr"
    for screen in [i for i in screens if i[2]]:
        command += f" --output {screen[0]} --off"
    for idx in range(len(enabled_screens)-1):
        command += f" --output {enabled_screens[idx][0]} --left-of {enabled_screens[idx+1][0]}"
    # print(command)
    os.system(command)
    time.sleep(3) # give it a sec to propagate changes
    
    # set primary screen
    primary = {
            0: 0,
            1: 0,
            2: 1,
            3: 1,
            }[len(screens)]
    os.system(f"xrandr --output {screens[primary][0]} --primary")

def load_config(path: str) -> dict:
    with open(path, 'r') as f:
        config = yaml.safe_load(f)
    return config

def gen_wal(config: dict) -> None:
    path = config["paper"]
    os.system(f"wal -i {path} --saturate 0.5")
    time.sleep(2)

def launch_polybar(config: dict, screens) -> None:
    os.system("killall -q polybar")
    for m in screens:
        # pass in monitor, bar width, and offset
        monitor = m[0]
        scr_width = m[1][0]
        bar_width = int(scr_width * config["bar-size"])
        bar_offset = (scr_width - bar_width) / 2
        print(f"MONITOR={monitor} BAR_W={bar_width} BAR_OFF={bar_offset} polybar --reload main &")
        os.system(f"MONITOR={monitor} BAR_W={bar_width} BAR_OFF={bar_offset} polybar --reload main &")
    
def main(monitors_only: bool, disable_laptop: bool) -> None:
    screens = get_screens(disable_laptop)
    config = load_config("/home/valis/resources/scripts/config.yaml")
    place_screens(screens)

    if monitors_only:
        return

    gen_wal(config)
    launch_polybar(config, screens)

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--lightdm', dest='mode', action='store_const',
                const='monitor-only', default='all')
        parser.add_argument('--disable-laptop', dest='laptop', action='store_true')
        args = parser.parse_args()
    
        main(args.mode == "monitor-only", args.laptop)
    except Exception as e:
        print("ono")
