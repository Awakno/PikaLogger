import requests
import pydantic


class DataModel(pydantic.BaseModel):
    username: str
    wins: int=None
    losses: int=None
    kills: int=None
    gameplay: int=None
    final_kills: int=None
    beds_broken: int=None
    death: int=None
    kdr: float=None
    message: str = None


class GetData:
    async def get_stats(self, username):
        r = requests.get(
            f"https://stats.pika-network.net/api/profile/{username}/leaderboard?type=bedwars&interval=total&mode=ALL_MODES"
        )
        if r.status_code == 404:
            return DataModel.model_validate({"username": username, "message": "Nicked"})
        if r.status_code == 204:
            return DataModel.model_validate({"username": username, "message": "Hidden"})
        if r.status_code == 200:

            wins = (
                r.json()["Wins"]["entries"][0]["value"]
                if r.json().get("Wins").get("entries")
                else 0
            )
            losses = (
                r.json()["Losses"]["entries"][0]["value"]
                if r.json().get("Losses").get("entries")
                else 0
            )
            kills = (
                r.json()["Kills"]["entries"][0]["value"]
                if r.json().get("Kills").get("entries")
                else 0
            )
            gameplay = (
                r.json()["Games played"]["entries"][0]["value"]
                if r.json().get("Games played").get("entries")
                else 0
            )
            final_kills = (
                r.json()["Final kills"]["entries"][0]["value"]
                if r.json().get("Final kills").get("entries")
                else 0
            )
            beds_broken = (
                r.json()["Beds destroyed"]["entries"][0]["value"]
                if r.json().get("Beds destroyed").get("entries")
                else 0
            )
            death = (
                r.json()["Deaths"]["entries"][0]["value"]
                if r.json().get("Deaths").get("entries")
                else 0
            )
            kdr = round(int(kills) / int(death),1) if kills != 0 else 0
             

            return DataModel.model_validate(
                {
                    "username": username,
                    "wins": wins,
                    "losses": losses,
                    "kills": kills,
                    "gameplay": gameplay,
                    "final_kills": final_kills,
                    "beds_broken": beds_broken,
                    "kdr": kdr,
                    "death": death,
                }
            )
        else:
            return DataModel.model_validate({"username": username, "message": "Error"})
