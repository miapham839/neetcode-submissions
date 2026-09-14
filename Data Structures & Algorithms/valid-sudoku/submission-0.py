class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Duplicates --> Use Hash set for each of the 3 rules
        - One to check row
        - One to check cols
        - One to check 3x3 sub boxes --> Keep track of which rows/cols are borders (use the mod operator)
        """

            # enumerate... accessing each col is like row[i]. LOL not sure how to loop over 2D list
            # (#) Any way to incrementally store col values + detect duplicates of cols right inside this loop? Bc I don't want to loop through it once more. A dict with col-num: values. Can I do the same with rows??
        seen_col = defaultdict(list)
        seen_subbox = defaultdict(list)
        subbox_count = 0
        subbox_indx = 0 # Only apply minus index rule when j % 3 != 0
        new_subbox_row = False
        for j in range(9):
            if ((j % 3 == 0)):
                new_subbox_row = True
            else: 
                new_subbox_row = False
            seen_row = set()
            for i, row_entry in enumerate(board[j]):
                if ((new_subbox_row == True) and (i % 3 == 0)):
                    subbox_count += 1
                    subbox_indx = subbox_count
                if (new_subbox_row == False):
                    if i in range(3):
                        subbox_indx = subbox_count - 2
                    elif i in range(3, 6):
                        subbox_indx = subbox_count - 1
                    else:
                        subbox_indx = subbox_count
                if row_entry == ".":
                    continue
                if (
                    row_entry in seen_row
                    or row_entry in seen_col[i]
                    or row_entry in seen_subbox[subbox_indx]
                ):
                    return False
                seen_row.add(row_entry)
                seen_col[i].append(row_entry)
                seen_subbox[subbox_indx].append(row_entry)
        return True

        #### Debug, visualization skills