try:
    import asyncio
    from crawler import *
    from jsondata import *
    from models import *
except Exception as e:
    print("The following modules are missing: {}".format(e))

async def main():
    # instances
    crawler_obj = Crawler()

    # tasks
    task_athentication = asyncio.create_task(crawler_obj.authenticate())
    await task_athentication

    # retrieve the saved informations from data.json
    json_data_obj = JsonData()
    data = json_data_obj.open_json_file()

    # print the serialiazed to object (level 3) data
    models_obj = CallUserModel(data)
    models_obj.show_user_model()

if __name__ == "__main__":
    asyncio.run(main())



