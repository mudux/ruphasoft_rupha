import os

HOME = os.environ.get('HOME')

def before_uninstall():
    print("Before Uninstall")
    print("=====================================")
    print("removing icons from icons.svg")
    os.remove("/home/"+HOME+"/frappe-bench/apps/frappe/frappe/public/icons/timeless/icons.svg")
    os.rename("/home/"+HOME+"/frappe-bench/apps/frappe/frappe/public/icons/timeless/icons.bak.svg", "/home/"+HOME+"/frappe-bench/apps/frappe/frappe/public/icons/timeless/icons.svg")
    print("=====================================")
    print("Before Uninstall DONE!")