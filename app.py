# app.py

from flask import Flask, render_template, request
from forms import SubnetForm
import ipaddress
import os

app = Flask(__name__)
app.config.from_pyfile("config.py")


@app.route("/", methods=["GET", "POST"])
def index():
    form = SubnetForm(request.form)
    summary = {}
    if request.method == "POST" and form.validate():
        cidr_input = f"{form.ip.data}/{form.cidr.data}"
        net = ipaddress.ip_network(cidr_input, strict=False)

        # total usable hosts
        total = net.num_addresses
        # for /31 and /32, RFC says all are usable
        usable = total if net.prefixlen >= 31 else total - 2

        hosts = list(net.hosts()) if usable > 0 else []
        summary = {
            "network_addr":     str(net.network_address),
            "broadcast_addr":   str(net.broadcast_address),
            "first_host":       str(hosts[0]) if hosts else str(net.network_address),
            "last_host":        str(hosts[-1]) if hosts else str(net.broadcast_address),
            "total_hosts":      usable,
            # for Chart.js visualization
            "network_count":    1,
            "host_count":       usable,
            "broadcast_count":  1,
        }

    return render_template("index.html", form=form, summary=summary)


if __name__ == "__main__":
    app.run(debug=True)
