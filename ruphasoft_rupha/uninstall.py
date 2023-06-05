import os

HOME = os.environ.get('HOME')


def before_uninstall():
    print("Before Uninstall")
    print("=====================================")
    print("removing icons from icons.svg")
    try:
        os.remove(HOME+"/frappe-bench/apps/frappe/frappe/public/icons/timeless/icons.svg")
        os.rename(HOME+"/frappe-bench/apps/frappe/frappe/public/icons/timeless/icons.bak.svg", "/home/"+HOME+"/frappe-bench/apps/frappe/frappe/public/icons/timeless/icons.svg")
    except Exception as e:
        print("============ERROR==================")
        print(e)
    print("=====================================")
    print("Before Uninstall DONE!")
