from Manager.GetData import GetData
from Manager.message import MessageManager
import asyncio
from colorama import init, Fore, Style
from prettytable import PrettyTable

init(autoreset=True)

async def main():
    messages_sent = MessageManager().follow()
    table = PrettyTable()
    table.field_names = ["Username", "Status", "Kills", "Wins", "Losses", "Deaths", "Game played", "Final Kills", "Beds Broken", "KDR"]

    print(table)

    for message in messages_sent:
        stats = await GetData().get_stats(message)
        if stats.message == "Nicked":
            status = Fore.RED + "Nicked" + Style.RESET_ALL
            row = [stats.username, status, "-", "-", "-", "-", "-", "-", "-", "-"]
        elif stats.message == "Hidden":
            status = Fore.YELLOW + "Hidden" + Style.RESET_ALL
            row = [stats.username, status, "-", "-", "-", "-", "-", "-", "-", "-"]
        elif stats.message == "Error":
            status = Fore.RED + "Error" + Style.RESET_ALL
            row = [stats.username, status, "-", "-", "-", "-", "-", "-", "-", "-"]
        else:
            status = Fore.GREEN + "Real" + Style.RESET_ALL
            row = [
                stats.username,
                status,
                stats.kills,
                stats.wins,
                stats.losses,
                stats.death,
                stats.gameplay,
                stats.final_kills,
                stats.beds_broken,
                stats.kdr,
            ]
        
        
        table.add_row(row)
        print("\033c", end="")
        print(table)

if __name__ == "__main__":
    asyncio.run(main())
