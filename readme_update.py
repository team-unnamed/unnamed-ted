import yaml
import os

if __name__ == "__main__":

    body = ""

    with open("README.md", "r", encoding="utf-8") as readme_md:
        origin = readme_md.readlines()

    for line in origin:
        body += line

    num = line.split('|')[1]    # 몇 번째 발표까지 update되었는지 확인용

    with open("presentation.yaml", "r", encoding="utf-8") as presentation_yaml:
        presentation = yaml.safe_load(presentation_yaml)

    with open("users.yaml", "r", encoding="utf-8") as users_yaml:
        user = yaml.safe_load(users_yaml)

    if num==':---':
        start=0
    else:
        start=int(num)

    for present in presentation[start:]:
        temp = f"|{present['num']}|{present['week']}|{present['presenter']}|"

        link = f"Week{present['week']}/{user[present['presenter']]['dir']}"

        temp += f"[{present['topic']}]({link})|"

        for cat in present['category'][:-1]:
            temp += f"{cat}</br>"
        
        temp += f"{present['category'][-1]}|"

        body += temp + '\n'

    with open("README.md", "w", encoding="utf-8") as md_out:
        md_out.write(body)

        
        
