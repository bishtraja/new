import os
from jinja2 import Template

# read the contents of the HTML file
with open("index.html", "r") as file:
    html_content = file.read()

# create a Jinja2 template from the HTML content
template = Template(html_content)

# render the template with the desired variables
rendered_template = template.render(var1="value1", var2="value2")

# write the rendered template back to the HTML file
with open("index.html", "w") as file:
    file.write(rendered_template)
