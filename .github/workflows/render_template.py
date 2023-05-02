import jinja2
import sys

def main():
    template_path = sys.argv[1]
    with open(template_path, 'r') as f:
        template = jinja2.Template(f.read())
    rendered_template = template.render()
    with open('final-email.html', 'w') as f:
        f.write(rendered_template)

if __name__ == '__main__':
    main()
