from django import template
from django.utils.safestring import mark_safe
import json

register = template.Library()


@register.simple_tag(name="get_people_metadata")
def getFamousPeopleMetadata(people_obj):
    res = ""
    facts = json.loads(people_obj.facts)
    if facts.get("Education & Qualifications"):
        res += f"<small><b>Education & Qualifications :</b> {facts['Education & Qualifications']}</small><br>"
    if facts.get("Occupation"):
        res += f"<small><b>Occupation :</b> {facts['Occupation']}</small><br>"
    if facts.get("Net Worth"):
        res += f"<small><b>Net Worth :</b> {facts['Net Worth']}</small>"
    return mark_safe(res)
