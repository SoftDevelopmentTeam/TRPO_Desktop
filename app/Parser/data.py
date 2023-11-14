class Data:
    platform = ''
    column_name_list = []
    table = []

    def get_column_name_list(self, string):
        self.column_name_list.append('№')
        for column_name in string.split('\n')[1:(-1)]:
            self.column_name_list.append(str(column_name.strip().removesuffix('\ue603')))

    def get_table_row_list(self, number, string):
        string_split = string.split('\n')
        self.table.append(list())

        self.table[-1].append(str(number))

        if number < 10:
            name = string_split[2][1:]
        else:
            name = string_split[2][2:]
        self.table[-1].append(str(name.strip()))

        for column_value in string_split[3:(-2)]:
            self.table[-1].append(str(column_value.strip()))
