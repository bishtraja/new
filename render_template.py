import os
from jinja2 import Environment, FileSystemLoader

GITHUB_REPOSITORY = os.environ.get("GITHUB_REPOSITORY")
GITHUB_SHA = os.environ.get("GITHUB_SHA")
GITHUB_HEAD_REF = os.environ.get("GITHUB_HEAD_REF")
GITHUB_REF = os.environ.get("GITHUB_REF")
GITHUB_ACTOR = os.environ.get("GITHUB_ACTOR")
GITHUB_WORKFLOW = os.environ.get("GITHUB_WORKFLOW")
GITHUB_EVENT_NAME = os.environ.get("GITHUB_EVENT_NAME")
GITHUB_EVENT_PATH = os.environ.get("GITHUB_EVENT_PATH")
GITHUB_WORKSPACE = os.environ.get("GITHUB_WORKSPACE")
GITHUB_ACTION = os.environ.get("GITHUB_ACTION")
GITHUB_HEAD_COMMIT_MESSAGE = os.environ.get("GITHUB_HEAD_COMMIT_MESSAGE")

# Create jinja2 environment and load the template
templateLoader = FileSystemLoader(searchpath="./")
templateEnv = Environment(loader=templateLoader)
TEMPLATE_FILE = "email-template.html"
template = templateEnv.get_template(TEMPLATE_FILE)

# Define template variables
templateVars = {
    "repository": GITHUB_REPOSITORY,
    "sha": GITHUB_SHA,
    "head_ref": GITHUB_HEAD_REF,
    "ref": GITHUB_REF,
    "actor": GITHUB_ACTOR,
    "workflow": GITHUB_WORKFLOW,
    "event_name": GITHUB_EVENT_NAME,
    "event_path": GITHUB_EVENT_PATH,
    "workspace": GITHUB_WORKSPACE,
    "action": GITHUB_ACTION,
    "head_commit_message": GITHUB_HEAD_COMMIT_MESSAGE,
    "github": {
        "workflow": GITHUB_WORKFLOW
    }
}

# Render the template
outputText = template.render(templateVars)
print(outputText)
