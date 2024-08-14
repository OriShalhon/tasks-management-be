class task:
    def __init__(self, id: int, name: str, status: str, description: str, start_time: str, attachment: str, blocking_task_id: int, project_id: int):
        self.id = id
        self.name = name
        self.status = status
        self.description = description
        self.start_time = start_time
        self.attachment = attachment
        self.blocking_task_id = blocking_task_id
        self.project_id = project_id