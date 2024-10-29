#TODO create a test for this
def ado_epic_test(config):
    db_manager = DatabaseManager(config.db_collection, config.db_document)
    setup_database(config.spreadsheet_id, db_manager)
    epic = db_manager.fetch_database()
    token = access_secret_version(config.project_id, config.ado_secret_id, config.gh_version_id)
    az_epic = ado_epic("TrackPointDev", "TrackPoint", token, epic['title'], epic['problem'], epic['feature'], epic['value'])
    
    for task in epic['tasks']:
        az_epic.add_task(task)

    print("Creating issues")
    az_epic.create_issues()

    print("Getting issues")
    print(az_epic.get_issues())

    print("Getting tasks")
    print(az_epic.get_tasks())

    input("Press enter to update DB")
    db_manager.update_db(az_epic.get_epic())

    taskwithid = db_manager.get_task_with_id(70)
    print("f: Task with id: ", taskwithid)

    taskwithtitle = db_manager.get_task_with_title("TEST TEST TEST")
    print("f: Task with title: ", taskwithtitle)

    input("Press enter to continue")
    print("Deleting epic")
    db_manager.delete_epic()