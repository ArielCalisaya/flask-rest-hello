from random import randint

class Family:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": 1,
                "first_name": "Jhon Doe",
                "gender": "male",
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 2,
                "first_name": "Jane Doe",
                "gender": "female",
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": 3,
                "first_name": "Jimmy Doe",
                "gender": "male",
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = self._generateId()
        return self._members.append(member)
        # filled method and updated the return


    def delete_member(self, id):
        new_members = list(filter(lambda member: member["id"] != id, self._members))
        self._members = new_members
        return self._members

        # filled method and updated


    def update_member(self, id, member):
        members = self._delete_member(id)
        member = id
        members.append(member)
        return members
        # filled method and updated

    def get_member(self, id):
        member = list(filtert(lambda member: member["id"] == id, self._members))
        return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members