"""

Config file for Streamlit App

"""

from streamlit_app.member import Member


TITLE = "My Awesome App"

TEAM_MEMBERS = [
    Member(
        name="Fayçal D",
        #linkedin_url="https://www.linkedin.com/in/charlessuttonprofile/",
        github_url="https://github.com/faycal77"
    ),
    Member("Jane Doe"),
    Member(
        name="Guillaume A",
        github_url="https://github.com/williamapc"
    ),
    Member("Jane Doe")
]

PROMOTION = "Promotion Bootcamp Data Scientist - April 2021"
