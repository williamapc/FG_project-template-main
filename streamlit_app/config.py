"""

Config file for Streamlit App

"""

from streamlit_app.member import Member


TITLE = "Classification de Plants"

TEAM_MEMBERS = [
    Member(
        name="Fayçal D",
        #linkedin_url="https://www.linkedin.com/in/charlessuttonprofile/",
        github_url="https://github.com/faycal77"
    ),
    Member("Fayçal A"),
    Member(
        name="Guillaume A",
        github_url="https://github.com/williamapc"
    ),
    Member("Guillaume As")
]

PROMOTION = "Promotion  Data Scientist - Mars 2026"
