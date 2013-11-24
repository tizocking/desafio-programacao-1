import csv
from models import FileData

def FileParser(up_file):
    """
    This method parses the csv file and saves every row into the model FileData
    """
    # Setup file and skips first row (header)
    arq = csv.reader(up_file, delimiter='\t')
    arq.next()

    grand_total = 0

    # Iterates into every row
    for row in arq:
        # Set and save this row into FileData
        data = FileData(
            purchaser_name=row[0],
            item_description=row[1],
            item_price=row[2],
            purchase_count=row[3],
            merchant_address=row[4],
            merchant_name=row[5])
        data.save()

        # Sums this row total price into grand total
        row_total = float(row[2]) * float(row[3])
        grand_total = grand_total + row_total

    return grand_total