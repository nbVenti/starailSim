import yatta
import asyncio

async def main() -> None:
    async with yatta.YattaAPI() as client:
        character_details = await client.fetch_character_detail("1310")
        # print(character_details)
        f = open("file.txt", "w")
        # print(type(character_details))
        # for i in character_details:
            # print(i)
        # print(character_details)
        print(character_details.traces.main_skills[1].skill_list[1].params["1"])
        print(character_details.traces.main_skills[1].skill_list[1].description)
    

        f.write(character_details.name)

asyncio.run(main())


