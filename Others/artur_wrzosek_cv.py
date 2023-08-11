"""
    Hello my fellow!
    This is CV of me - for better reading just run this script ;)
    Hope seeing soon!
"""
ARTUR_WRZOSEK_DATA = {
    "personal_data":
        [
            {
                "name": "Artur Wrzosek",
                "field": "Backend Development",
                "link": "https://www.linkedin.com/in/arturwrzosek/",
                "age": 37,
                "email": "wrzosek.artur@gmail.com",
                "mobile":"+48 666 692 293",
            }
        ],
    "experience":
        [
            {
                "name": "Szkoła w Chmurze",
                "field": "Backend Development",
                "link": "https://szkolawchmurze.org/",
                "period": [(2022, 7, 1), ()],
                "skills": {
                    "Python": 5, "Django": 4, "DRF": 3, "Postgres": 3, "SQL": 3, "PyCharm": 4,
                    "Linux": 2, "HTTP": 2, "Git": 3, "pytest": 2, "GitLab": 3, "Bitbucket": 3,
                    "Jira": 3, "Docker": 2,
                },
            },
            {
                "name": "Self-employment",
                "field": "Backend Development",
                "link": "https://arturwrzosek.pythonanywhere.com/",
                "period": [(2022, 1, 1), (2022, 7, 1)],
                "skills": {
                    "Mathematics": 3, "Python": 3, "Django": 2, "HTML": 2, "CSS": 2,
                    "SQL": 2, "SQLite": 2, "PyCharm": 3, "C++": 1,
                },
            },
            {
                "name": "Accenture",
                "field": "Data Science",
                "link": "https://www.accenture.com/",
                "period": [(2021, 10, 1), (2022, 2, 1)],
                "skills": {
                    "Python": 3, "Postgres": 2, "SQL": 2, "PyCharm": 2, "Git": 1, "English": 3,
                },
            },
            {
                "name": "SoftKraft",
                "field": "Data Science",
                "link": "https://www.softkraft.co/",
                "period": [(2021, 7, 1), (2021, 11, 1)],
                "skills": {
                    "Python": 3, "Pandas": 3, "Plotly": 3, "Dash": 3, "HTML": 2,
                    "PyCharm": 2, "GitLab": 2, "Git": 2, "English": 3, "Jira": 2,
                },
            },
            {
                "name": "Non-IT firms",
                "field": "Finances & Spedition firms",
                "link": "https://www.linkedin.com/in/arturwrzosek/",
                "period": [(2006, 7, 1), (2021, 4, 1)],
                "skills": {"Management": 4, "Finances": 4, "Sales": 5, "English": 4},
            },
        ],
    "education":
        [
            {
                "name": "UAM - Uniwersytet im. Adama Mickiewicza w Poznaniu",
                "field": "Data Science",
                "link": "https://wmi.amu.edu.pl/dla-kandydata/studia-ii-stopnia/analiza-i-przetwarzanie-danych",
                "period": [(2020, 10, 1), (2022, 6, 1)],
                "skills": {
                    "Python": 3, "SQL": 2, "Pandas": 2, "NumPy": 2, "Mathematics": 3, "English": 4,
                },
            },
            {
                "name": "Uczelnia Łazarskiego w Warszawie",
                "field": "MBA - Master of Business Administration",
                "link": "https://www.asbiro.pl/studia-mba-2/przedsiebiorczosc/",
                "period": [(2015, 10, 1), (2017, 6, 1)],
                "skills": {"Management": 5, "Finances": 4},
            },
            {
                "name": "PUT - Poznan University of Technology",
                "field": "Automation and Robotics",
                "link": "https://www.put.poznan.pl/en/Faculty-of-Automatic-Control-Robotics-and-Electrical-Engineering",
                "period": [(2005, 10, 1), (2010, 6, 1)],
                "skills": {"Mathematics": 5, "C++": 2},
            },
        ],
    "certificates":
        [
            {
                "name": "PCAP – Certified Associate in Python Programming",
                "field": "Backend Development",
                "link": "https://verify.openedg.org/?id=TqPs.PqNu.89jM",
                "period": [(2022, 2, 1), (2022, 3, 1)],
                "skills": {"Python": 4},
            },
            {
                "name": "AWS - Certified Cloud Practitioner",
                "field": "Cloud",
                "link": "https://www.credly.com/badges/0a760c94-f6eb-4a5b-9adb-7cef2b9e2d6e",
                "period": [(2021, 12, 1), (2022, 2, 1)],
                "skills": {"AWS": 2},
            },
            {
                "name": "PCEP – Certified Entry-Level Python Programmer",
                "field": "Data Science",
                "link": "https://verify.openedg.org/?id=ByU4.Ws80.M6e4",
                "period": [(2021, 7, 1), (2021, 8, 1)],
                "skills": {"Python": 2},
            },
            {
                "name": "Django 3.0 - Fundamentals",
                "field": "Backend Development",
                "link": "https://www.udemy.com/certificate/UC-ab4be72e-8d27-4b2e-8e43-ab99a913e26d/",
                "period": [(2021, 3, 1), (2021, 4, 1)],
                "skills": {"Django": 2},
            },
            {
                "name": "GCP - Google Cloud Skills Boost",
                "field": "Cloud",
                "link": "https://www.cloudskillsboost.google/public_profiles/2310bed6-de1c-4692-8b2e-bf82a009660d",
                "period": [(2020, 12, 1), (2021, 2, 1)],
                "skills": {"GCP": 2},
            },
            {
                "name": "TOEIC - Test of English for International Communication 900/990",
                "field": "Other",
                "link": "https://ef.com/wwen/english-tests/toeic/score/",
                "period": [(2011, 5, 1), (2011, 6, 1)],
                "skills": {"English": 4},
            },
        ]
}



class UserProfile:
    def __init__(self, data: dict = None):
        self._data = {}
        self._menu = {"0": "exit", str(len(data)+1): "skills_summary"}
        for k, v in data.items():
            self._data[f"{k}"] =  v
            if k not in self._menu: self._menu[str(len(self._menu)-1)] = k
        self._skills()

    def _skills(self):
        exp_list = [x for x in self._data.values() for x in x]
        summary = {}
        for exp in exp_list[1:]:
            time = delta(exp["period"])
            for skill, rate in exp["skills"].items():
                if skill in summary: summary[skill].append((time, rate))
                else: summary[skill] = [(time, rate)]
        self._data["skills_summary"] = [{s: [
            w := sum([z[0] for z in d]), sum([z[0] * z[1] for z in d]) / w] for s, d in summary.items()}]

    def _unpack(self, option):
        for n, record in enumerate(self._data[self._menu[option]]):
            print(f"\n{n+1}. ", end="")
            for k, v in record.items():
                if self._menu[option] == "skills_summary":
                    print(f"- {k}: {round(v[1])*'★'}{(5-round(v[1]))*'☆'} ({round(v[1], 2)} / {v[0]//365}y{v[0]%365//30}m)")
                    continue
                if k == "period":
                    print(f"From: {date(*v[0])} to: {date(*v[1]) if v[1] else 'still'}")
                    continue
                print(f"{k.capitalize()}: {', '.join(v.keys()) if type(v) is dict else v}")

    def _print_menu(self):
        for n in range(len(self._menu)):
            print(f"{n}. {' '.join(self._menu[str(n)].capitalize().split(sep='_'))}")

    def cv(self):
        while True:
            clear()
            self._print_menu()
            if (option:= input("\nChoose an option: ")) == "0": break
            if option.isdigit() and int(option)<=len(self._menu): self._unpack(option)
            if input("\nBack? [y/n]: ") == "n": break


if __name__ == "__main__":
    import os
    from datetime import date

    def delta(period: list):
        if period[1] == (): return (date.today() - date(*period[0])).days
        return (date(*period[1]) - date(*period[0])).days

    def clear():
        os.system('cls||clear')

    artur = UserProfile(data=ARTUR_WRZOSEK_DATA)
    artur.cv()