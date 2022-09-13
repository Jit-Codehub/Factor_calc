import json
from django.utils.text import slugify
from .models import *

def saveDataInDB(json_data,filename):
    count = 0
    for row in json_data:
        famous_people_obj = FamousPeople.objects.filter(title=row["title"])
        if not famous_people_obj:
            famous_people_obj = FamousPeople()
            famous_people_obj.title = row["title"]
            famous_people_obj.subtitle = row["subtitle"]
            famous_people_obj.meta_description = row["meta_description"]
            famous_people_obj.jump_links = json.dumps(row["jump_links"])
            famous_people_obj.birthday_highlights = json.dumps(row["birthday_highlights"])
            famous_people_obj.facts = json.dumps(row["facts"])
            famous_people_obj.content = row["content"]
            famous_people_obj.image = f"/media/famous_people/images/{slugify(row['title'])}.png"
            famous_people_obj.save()
            count+=1

    res = f"{filename} => {count}/{len(json_data)} data has stored in DB <br>"
    return res