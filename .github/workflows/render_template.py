import os
from jinja2 import Template

with open("email_template.html", "r") as f:
    template = Template(f.read())

# Render the template with the desired variables
rendered_template = template.render(
    job_status=os.environ["JOBSTATUS"],
    github_repository=os.environ["GITHUB_REPOSITORY"],
    github_run_number=os.environ["GITHUB_RUN_NUMBER"],
    github_ref=os.environ["GITHUB_REF"],
    github_head_commit_message=os.environ["GITHUB_HEAD_COMMIT_MESSAGE"],
)

# Write the rendered template back to the file
with open("email_template.html", "w") as f:
    f.write(rendered_template)

