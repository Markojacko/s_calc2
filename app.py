import os
from flask import Flask, request, render_template, jsonify, Response
from forms import SubnetForm
from calculator import summarize_network, split_network
from config import AWS_AZ, AZURE_LOCATION, GCP_REGION, SECRET_KEY
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SubnetForm()
    result = None
    subnets = []
    tf_template = ''
    if form.validate_on_submit():
        ip = form.ip_address.data
        mask = form.cidr_mask.data
        cidr = f"{ip}/{mask}"
        split_mask = form.split_mask.data
        cloud = form.cloud_provider.data

        # Calculate network summary
        summary = summarize_network(ip, mask)
        result = summary['result']
        cloud_warnings = summary['cloud_warnings']
        result['Cloud Compatibility Warnings'] = cloud_warnings

        # Split subnets if requested
        if split_mask and split_mask > summary['network'].prefixlen:
            subnets = split_network(summary['network'], split_mask)

        # Render Terraform template
        tf_template = render_template(f"tf/{cloud}.tf.j2", cidr=cidr,
                                      AWS_AZ=AWS_AZ,
                                      AZURE_LOCATION=AZURE_LOCATION,
                                      GCP_REGION=GCP_REGION)
    return render_template('index.html', form=form, result=result,
                           subnets=subnets, tf_template=tf_template)

@app.route('/export')
def export():
    ip = request.args.get('ip')
    mask = request.args.get('cidr', type=int)
    fmt = request.args.get('format', 'csv')
    try:
        summary = summarize_network(ip, mask)
        result = summary['result']
        # Remove warnings for export
        result.pop('Cloud Compatibility Warnings', None)

        if fmt == 'json':
            data = jsonify(result)
            data.headers['Content-Disposition'] = 'attachment; filename=subnet_info.json'
            return data
        elif fmt == 'csv':
            import csv, io
            si = io.StringIO()
            writer = csv.writer(si)
            writer.writerow(result.keys())
            writer.writerow(result.values())
            output = si.getvalue()
            return Response(output, mimetype='text/csv',
                            headers={'Content-Disposition': 'attachment; filename=subnet_info.csv'})
        else:
            return "Invalid format", 400
    except Exception as e:
        return f"Error: {e}", 500

@app.route('/download_tf')
def download_tf():
    ip = request.args.get('ip')
    mask = request.args.get('cidr', type=int)
    cloud = request.args.get('provider', 'aws')
    cidr = f"{ip}/{mask}"
    from flask import render_template_string
    tf_data = render_template(f"tf/{cloud}.tf.j2", cidr=cidr,
                              AWS_AZ=AWS_AZ,
                              AZURE_LOCATION=AZURE_LOCATION,
                              GCP_REGION=GCP_REGION)
    return Response(tf_data, mimetype='text/plain',
                    headers={'Content-Disposition': 'attachment; filename=subnet.tf'})

if __name__ == '__main__':
    app.run(debug=True)
