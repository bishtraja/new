import os
from jinja2 import Environment, FileSystemLoader

TEMPLATE_FILE = "email_template.html"

templateLoader = FileSystemLoader(searchpath="./")
templateEnv = Environment(loader=templateLoader)

template = templateEnv.get_template(TEMPLATE_FILE)

templateVars = {
    "github_repository": os.environ["GITHUB_REPOSITORY"],
    "github_run_number": os.environ["GITHUB_RUN_NUMBER"],
    "github_ref": os.environ["GITHUB_REF"],
    "github_head_ref": os.environ.get("GITHUB_HEAD_REF", ""),
    "github_event_name": os.environ["GITHUB_EVENT_NAME"],
    "github_sha": os.environ["GITHUB_SHA"],
    "github_actor": os.environ["GITHUB_ACTOR"],
    "github_workflow": os.environ["GITHUB_WORKFLOW"],
}

outputText = template.render(templateVars)

