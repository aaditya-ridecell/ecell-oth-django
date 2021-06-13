import os
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base_app.settings")
django.setup()

from treasurehunt.models import UserProfile, Score


def remove(string):
    return "".join(string.split())


def populate():
    df = pd.read_csv("hackathon.csv")
    print(len(df))
    # for i in range(len(data)):
    # u = AnswerChecker.objects.get_or_create(email=)[0]
    for ind in df.index[:1]:
        u = UserProfile.objects.get_or_create(
            email=remove(df["Email"][ind].lower().strip()),
            name=df["Name"][ind],
        )[0]
        u.save()
        u.set_password("ecell@12")
        u.save()
        score = Score()
        score.user = u
        score.save()


if __name__ == "__main__":
    print("populating script")
    populate()
    print("populating complete")
