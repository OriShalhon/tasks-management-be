class task:
    def __init__(
        self,
        id: int,
        name: str,
        status: str,
        description: str,
        start_time: str,
        attachment: str,
        blocking_task_id: int,
        project_id: int,
    ):
        self.id = id
        self.name = name
        self.status = status
        self.description = description
        self.start_time = start_time
        self.attachment = attachment
        self.blocking_task_id = blocking_task_id
        self.project_id = project_id

    def to_dict(self) -> dict:
        """Converts the Task object to a dictionary.

        Returns:
            dict: A dictionary representation of the Task object.
        """

        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "description": self.description,
            "start_time": self.start_time,
            "attachment": self.attachment,
            "blocking_task_id": self.blocking_task_id,
            "project_id": self.project_id,
        }
