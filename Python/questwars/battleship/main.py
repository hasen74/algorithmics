def validate_battlefield(field):
    found_ships = []
    found_indexes = []
    cell_index = ''
    buffer_indexes = []
    prox_indexes_all = [-11, -1, 9, -10, 0, 10, -9, 1, 11]
    prox_indexes = []
    prox_counter = 0
    rows = field
    columns = [[], [], [], [], [], [], [], [], [], []]
    rows_or_columns = rows

    # Populates the columns 2D array with values from rows
    for row in field:
        for i, column in enumerate(columns):
            column.append(row[i])

    # Checks the board for ships from biggest to smallest
    for ship_size in reversed(range(1, 5)):
        # Alternates between rows and columns, starting from rows
        for is_column in range(0, 2):
            # Looks for ships in the row/column
            for i, row_or_column in enumerate(rows_or_columns):
                for j, cell in enumerate(row_or_column):
                    if cell == 1:
                        # Adapting checks from cell position on the board
                        match i if is_column else j:
                            case 0:
                                prox_indexes = prox_indexes_all[3:]
                            case 9:
                                prox_indexes = prox_indexes_all[:6]
                            case _:
                                prox_indexes = prox_indexes_all
                        # Storing the cell index
                        cell_index = (str(j+1)
                                      + str(i)
                                      if is_column else str(i+1) + str(j))
                        # Iterates through all surrounding cells' indexes
                        for prox_index in prox_indexes:
                            # If cell is not already validated,
                            # adds it to the buffer list
                            if (str(int(cell_index)
                                + prox_index)
                                    in found_indexes):
                                prox_counter += 1
                        if prox_counter == 0:
                            buffer_indexes.append(cell_index)
                        # At the end of the row/column or if next cell is 0
                        if j == 9 or row_or_column[j + 1] == 0:
                            # If the buffer list is of the right size,
                            # validates the ship and its indexes
                            # and clears buffer
                            if len(buffer_indexes) == int(ship_size):
                                found_indexes.extend(buffer_indexes)
                                found_ships.append(ship_size)
                            buffer_indexes.clear()
                    # Resets prox_counter for next cell check
                    prox_counter = 0
            # Switches between rows and columns for each ship check
            rows_or_columns = rows if is_column else columns

    # If right amount of ships is found, return true
    if found_ships == [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]:
        return True

    return False
