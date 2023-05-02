import jinja2
import os

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)

templateVars = {
    "github_workflow": os.environ["GITHUB_WORKFLOW"],
    "github_repository": os.environ["GITHUB_REPOSITORY"],
    "github_run_number": os.environ["GITHUB_RUN_NUMBER"],
    "github_ref": os.environ["GITHUB_REF"],
    "github_head_commit_message": os.environ.get("GITHUB_HEAD_COMMIT_MESSAGE", ""),
}

TEMPLATE_FILE = "email-template.html"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(templateVars)

with open("email_body.txt", "w") as file:
    file.write(outputText)
