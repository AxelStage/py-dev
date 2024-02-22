#!python3

import http.server

ip = "127.0.0.1"
port = 8000
bash_commands = {
    "datetime": "date --utc +%Y-%m-%d' '%H:%M:%S",
    "hostname": "hostname -f",
    "ipv4": "ip -4 addr show eth0 | awk '/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/ {print $2}'",
    "ipv6": "ip -6 addr show eth0 | awk '/....:....:....:/' | awk 'NR==1 {print $2}'",
    "last1": "last -a --limit 10  | awk '! /reboot/ && ! /still logged in/' | awk 'NR==1 {print $1}'",
    "last2": "last -a --limit 10  | awk '! /reboot/ && ! /still logged in/' | awk 'NR==1 {print $10}'",
    "last3": "last -a --limit 10  | awk '! /reboot/ && ! /still logged in/' | awk 'NR==1 {print $3,$4,$5,$6,$7,$8,$9}'",
    "uptime": "cut -d. -f1 /proc/uptime",
    "cpu1": "cat /proc/loadavg | awk '{print $1}'",
    "cpu5": "cat /proc/loadavg | awk '{print $2}'",
    "cpu15": "cat /proc/loadavg | awk '{print $3}'",
    "ramtotal": "free -h | grep 'Mem' | awk '{print $2}'",
    "ramused": "free -h | grep 'Mem' | awk '{print $3}'",
    "ramfree": "free -h | grep 'Mem' | awk '{print $4}'",
    "ramswap": "free -h | grep 'Swap' | awk '{print $3}'",
}


def time_scale(scale, time_measure):

    outcome = 0
    if scale == "day":
        outcome = int(time_measure) / 86400
    elif scale == "hour":
        outcome = int(time_measure) / 3600 % 24
    elif scale == "minute":
        outcome = int(time_measure) / 60 % 60
    elif scale == "second":
        outcome = int(time_measure) % 60

    outcome = int(outcome)

    return outcome


def bash_shell_wrapper(commands):

    import subprocess

    keyslist = []
    valueslist = []

    for key, command in commands.items():
        keyslist.append(key)
        process_run = subprocess.run(command, capture_output=True, shell=True)
        valueslist.append(process_run.stdout.decode())

    return dict(zip(keyslist, valueslist))


def prepare_html(sys_output):

    html = r"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>System Info</title>
        </head>
        <body>
            <h1>System Info</h1>
            <table>
                <tr>
                    <th>Parameter</th>
                    <th>Value</th>
                </tr>
                <tr>
                    <td>Datetime</td>
                    <td>{datetime} (UTC)</td>
                </tr>
                <tr>
                    <td>Hostname</td>
                    <td>{hostname}</td>
                </tr>
                <tr>                        
                    <td>IPv4</td>
                    <td>{ipv4}</td>
                </tr>
                <tr>                        
                    <td>IPv6</td>
                    <td>{ipv6}</td>
                </tr>
                <tr>                        
                    <td>Last Login</td>
                    <td>{last1}@{last2} | {last3}</td>
                </tr>
                <tr>                        
                    <td>Uptime</td>
                    <td>{up_days} day(s), {up_hours}:{up_minutes}:{up_seconds}</td>
                </tr>
                <tr>                        
                    <td>CPU load</td>
                    <td>{cpu1} (1 Min.) | {cpu5} (5 Min.) | {cpu15} (15 Min.)</td>
                </tr>
                <tr>                        
                    <td>RAM</td>
                    <td>Total: {ramtotal} | USED: {ramused} | Free: {ramfree} | Used Swap: {ramswap}</td>
                </tr>
            </table>
        </body>
    </html>""".format(
        datetime=sys_output.get("datetime", "?"),
        hostname=sys_output.get("hostname", "?"),
        ipv4=sys_output.get("ipv4", "?"),
        ipv6=sys_output.get("ipv6", "?"),
        last1=sys_output.get("last1", "?"),
        last2=sys_output.get("last2", "?"),
        last3=sys_output.get("last3", "?"),
        up_days=time_scale("day", sys_output.get("uptime")),
        up_hours=time_scale("hour", sys_output.get("uptime")),
        up_minutes=time_scale("minute", sys_output.get("uptime")),
        up_seconds=time_scale("second", sys_output.get("uptime")),
        cpu1=sys_output.get("cpu1", "?"),
        cpu5=sys_output.get("cpu5", "?"),
        cpu15=sys_output.get("cpu15", "?"),
        ramtotal=sys_output.get("ramtotal", "?"),
        ramused=sys_output.get("ramused", "?"),
        ramfree=sys_output.get("ramfree", "?"),
        ramswap=sys_output.get("ramswap", "?"),
    )

    return html


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        # print(self.command)
        # print(self.path)
        # print(self.request_version)

        # get sys data
        sys_output = bash_shell_wrapper(bash_commands)
        # build html
        html = prepare_html(sys_output)
        # send get response
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))


if __name__ == "__main__":
    webServer = http.server.HTTPServer((ip, port), Handler)
    print("Server started http://%s:%s" % (ip, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("\nServer stopped.")
