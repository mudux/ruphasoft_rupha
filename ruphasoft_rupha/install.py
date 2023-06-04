def before_install():
    print("Before Install")
    print("=====================================")
    print("adding icons to icons.svg")
    replacetext = "<symbol fill='none' viewBox='0 0 16.12 32' xmlns='http://www.w3.org/2000/svg' id='icon-rda-logo'>\
        <g>\
            <path fill='#1D4488' d='M8.07,17.44c1.93,0,3.86,0.01,5.79-0.01c0.4,0,0.56,0.07,0.55,0.52c-0.03,2.15,0,4.31-0.02,6.46\
                c-0.03,3.16-2.18,5.43-5.07,5.99c-2.2,0.43-4.18-0.08-5.81-1.6c-1.12-1.04-1.78-2.37-1.78-3.96c0-2.11,0-4.23,0-6.34\
                c0-1.07,0-1.07,1.04-1.07C4.54,17.44,6.3,17.44,8.07,17.44z'/>\
            <path fill='#1D4488' d='M8.01,2.22c0.16-0.25,0.28-0.48,0.43-0.68C8.64,1.26,8.9,1.3,9.13,1.48c0.23,0.17-0.02,0.3-0.09,0.41\
                C8.46,2.82,8.48,2.78,9.49,3.2c2.04,0.84,3.71,2.1,4.54,4.24c0.28,0.71,0.34,1.48,0.36,2.23c0.04,2.13,0,4.27,0.03,6.4\
                c0,0.43-0.12,0.54-0.54,0.53c-3.86-0.02-7.72-0.01-11.58,0c-0.4,0-0.57-0.06-0.57-0.52c0.02-2.42-0.04-4.84,0.01-7.26\
                c0.03-1.15,0.57-2.17,1.27-3.09c1.06-1.38,2.48-2.22,4.1-2.74c0.34-0.11,0.42-0.22,0.23-0.52C7.22,2.29,7.12,2.09,7.06,1.88\
                C7.02,1.75,6.68,1.61,7.05,1.44c0.26-0.12,0.47-0.14,0.62,0.11C7.8,1.75,7.89,1.97,8.01,2.22z M8.06,16.29\
                c1.81,0,3.62-0.01,5.42,0.01c0.45,0.01,0.58-0.1,0.58-0.57c-0.03-2.11-0.01-4.23-0.01-6.34c0-0.79-0.2-1.54-0.53-2.24\
                c-0.89-1.88-2.47-2.97-4.34-3.73c-0.7-0.28-1.35-0.44-2.1-0.12C6.01,3.75,4.97,4.25,4.11,5.02c-1.1,1-1.96,2.22-2.01,3.75\
                c-0.08,2.34-0.01,4.68-0.03,7.01c0,0.39,0.09,0.52,0.5,0.51C4.41,16.27,6.23,16.29,8.06,16.29z'/>\
            <path fill='#FFFFFF' d='M8.06,16.29c-1.83,0-3.66-0.01-5.48,0.01c-0.41,0-0.5-0.12-0.5-0.51c0.02-2.34-0.05-4.68,0.03-7.01\
                c0.05-1.53,0.91-2.75,2.01-3.75c0.86-0.77,1.9-1.28,2.97-1.73c0.75-0.32,1.4-0.16,2.1,0.12c1.87,0.76,3.45,1.84,4.34,3.73\
                c0.33,0.7,0.53,1.45,0.53,2.24c0.01,2.11-0.01,4.23,0.01,6.34c0.01,0.47-0.13,0.57-0.58,0.57C11.68,16.27,9.87,16.29,8.06,16.29z'\
                />\
        </g>\
    </symbol>\
    <symbol fill='none' viewBox='0 0 32 33.68' xmlns='http://www.w3.org/2000/svg' id='icon-rupha-logo'>\
        <g xmlns='http://www.w3.org/2000/svg'>\
            <path fill='#032E8D' d='M0.38,17.91c-0.13-1.1-0.07-2.21,0.24-3.85c0.45-2.35,1.19-4.22,2.6-6.24c4.82-6.91,14.13-8.34,21.03-4.2   c3.84,2.3,6.31,5.7,7.1,9.9c0.84,4.48,0.19,8.94-2.91,12.67c-2.49,2.99-5.54,5.04-9.5,5.86c-6.06,1.25-11.83-1.31-15.33-5.71   c-1.66-2.09-2.46-3.91-2.91-6.48 M30.17,16.77C30.61,8.83,23.84,2.73,15.9,2.71C7.73,2.69,1.82,8.7,1.63,16.58   c-0.2,7.98,6.84,14.57,14.41,14.47C23.58,30.95,30.53,24.58,30.17,16.77z'/>\
            <path fill='#FEFFFF' d='M30.17,16.77c0.36,7.81-6.6,14.18-14.13,14.27c-7.57,0.1-14.61-6.49-14.41-14.47   C1.82,8.7,7.73,2.69,15.9,2.71C23.84,2.73,30.61,8.83,30.17,16.77z M15.96,4.01C8.76,3.6,2.34,10.3,2.89,17.64   c0.43,5.73,5.81,12.33,13.23,12.08c7.28-0.24,13.05-6.24,12.96-12.95C28.98,9.67,23.64,3.93,15.96,4.01z'/>\
            <path fill='#032E8D' d='M15.96,4.01c7.68-0.09,13.02,5.66,13.12,12.76c0.1,6.71-5.68,12.71-12.96,12.95   C8.7,29.97,3.32,23.37,2.89,17.64C2.34,10.3,8.76,3.6,15.96,4.01z M22.17,17.05c0.37-0.16,0.18-0.29-0.03-0.41   c-1.06-3.1-3.79-4.68-5.98-6.41c-2.65,1.75-5.67,3.27-6.34,6.97C13.95,17.09,18.06,17.37,22.17,17.05z M16.13,17.82   c0,0,0,0.01,0,0.01c-1.34,0-2.69,0.03-4.03-0.01C11.35,17.8,10.98,18,11,18.84c0.05,1.77,0.01,3.55,0.02,5.32   c0,0.31-0.05,0.63,0.37,0.81c1.66,0.72,3.34-0.22,3.28-1.93c-0.03-0.96,0.18-1.61,1.23-1.7c1.16-0.1,1.3,0.79,1.47,1.6   c0.07,0.32,0.06,0.67,0.01,0.99c-0.14,0.93,0.32,1.15,1.14,1.06c0.5-0.05,1.01-0.06,1.51,0c0.88,0.1,1.19-0.24,1.17-1.12   c-0.05-1.61-0.06-3.22,0-4.82c0.03-0.91-0.23-1.31-1.22-1.26C18.71,17.88,17.42,17.82,16.13,17.82z'/>\
            <path fill='#FEFFFF' d='M16.13,17.82c1.29,0,2.58,0.05,3.86-0.02c0.99-0.06,1.25,0.34,1.22,1.26c-0.06,1.61-0.05,3.22,0,4.82   c0.03,0.87-0.28,1.21-1.17,1.12c-0.5-0.06-1.01-0.05-1.51,0c-0.82,0.08-1.29-0.14-1.14-1.06c0.05-0.32,0.06-0.68-0.01-0.99   c-0.17-0.8-0.31-1.69-1.47-1.6c-1.05,0.09-1.27,0.74-1.23,1.7c0.06,1.71-1.62,2.64-3.28,1.93c-0.42-0.18-0.37-0.5-0.37-0.81   c-0.01-1.77,0.03-3.55-0.02-5.32c-0.03-0.84,0.35-1.03,1.1-1.01c1.34,0.04,2.69,0.01,4.03,0.01   C16.13,17.83,16.13,17.83,16.13,17.82z'/>\
            <path fill='#FEFFFF' d='M22.17,17.05c-4.11,0.32-8.22,0.04-12.35,0.16c0.67-3.7,3.69-5.22,6.34-6.97c2.19,1.73,4.93,3.31,5.98,6.41   C22.15,16.78,22.16,16.91,22.17,17.05z'/>\
            <path fill='#889CC4' d='M22.17,17.05c-0.01-0.14-0.02-0.27-0.03-0.41C22.35,16.76,22.54,16.89,22.17,17.05z'/>\
        </g>\
    </symbol>\
    </svg>"
    data = ""
    with open("/home/frappe/frappe-bench/apps/frappe/frappe/public/icons/timeless/icons.svg", "r") as f:
        with open("/home/frappe/frappe-bench/apps/frappe/frappe/public/icons/timeless/icons.bak.svg", "w") as nf:
            svgf = f.read()
            nf.write(svgf)
            data = svgf.replace("</svg>", replacetext)
            nf.close()
            f.close()
    with open("/home/frappe/frappe-bench/apps/frappe/frappe/public/icons/timeless/icons.svg", "r+") as f:
        f.write(data)
        f.close()
    print("=====================================")
    print("Before Install DONE!")