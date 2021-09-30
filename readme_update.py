import yaml
import os

if __name__ == "__main__":

    body = ""

    with open("header.md", "r", encoding="utf-8") as header_md:
        origin = header_md.read()

    body += origin

    with open("presentation.yaml", "r", encoding="utf-8") as presentation_yaml:
        presentation = yaml.safe_load(presentation_yaml)

    with open("users.yaml", "r", encoding="utf-8") as users_yaml:
        user = yaml.safe_load(users_yaml)

    for present in presentation:
        temp = f"|{present['week']}|{present['presenter']}|"

        link = f"Week{present['week']}/{user[present['presenter']]['dir']}"

        temp += f"[{present['topic']}]({link})|"

        for cat in present['category'][:-1]:
            temp += f"{cat}</br>"
        
        temp += f"{present['category'][-1]}|"

        body += temp + '\n'

    with open("README.md", "w", encoding="utf-8") as md_out:
        md_out.write(body)
