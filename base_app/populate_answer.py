import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base_app.settings")
django.setup()

from treasurehunt.models import AnswerChecker

answer = [
    "iiitpune",
    "entrepreneurship",
    "opendyslexic",
    "stephenking",
    "376",
    "arunvaidya",
    "franzbeckenbauer",
    "athens",
    "retiopening",
    "tomhanks",
    "scandinavia",
    "lodovicoferrari",
    "maxplanck",
    "wakanda",
    "lalande21185",
    "jarasandha",
]


def populate(N=5):
    for i in range(N):

        u = AnswerChecker.objects.get_or_create(index=i, answer=answer[i])[0]


if __name__ == "__main__":
    print("populating script")
    populate(16)
    print("populating complete")
