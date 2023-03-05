
class Query:
    def __init__(self, table):
        self.table: str = table
        self.selects: list = []
        self.where_conditions: list = []
        self.and_where_condition: str = ""
        self.where_condition: str = ""

    def add_select(self, attribute: str):
        self.selects.append(attribute)
        return self


    def add_condition(self, attribute: str):
        self.where_conditions.append(attribute)
        return self

    def and_where(self):
        conditions = []
        for cond in self.where_conditions:
            conditions.append(f"{cond} = :{cond}")
        self.and_where_condition = " AND ".join(conditions)
        return self

    def select_query(self) -> str:
        select = ", ".join(self.selects)
        return f"SELECT {select} FROM {self.table} WHERE {self.and_where_condition}"

    def insert_query(self, columns: list) -> str:
        cols = ", ".join(columns)
        values =  ", ".join(list(map(lambda x: ":" + x, columns)))
        return f"INSERT INTO {self.table}({cols}) VALUES ({values})"
    
    def update_query(self, columns: list) -> str:
        values =  ", ".join(list(map(lambda x: x + " = :" + x, columns)))
        return f"UPDATE {self.table} SET {values} WHERE id = :id"
    
    def delete_query(self) -> str:
        return f"DELETE FROM {self.table} WHERE id = :id"