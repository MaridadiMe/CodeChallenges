import csv

def combine_csv(*files):
    # get headers from all files
    all_headers = []
    for file in files:
        try:
            with open(file, newline='') as csv_file1:
                reader_1 = csv.DictReader(csv_file1)
                for row in reader_1:
                    headers = list(row.keys())
                    for header in  headers:
                        if header not in all_headers:
                            all_headers.append(header)
                    break
        except Exception as e:
            print(e)

    try:
        with open('combined.csv', 'w') as output:
            writer = csv.DictWriter(output, fieldnames=all_headers, restval='')
            writer.writeheader()
            for file in files:
                with open(file, newline='') as csv_file:
                    reader = csv.DictReader(csv_file)
                    for row in reader:
                        writer.writerow(row)
    except Exception as e:
        print(e)

    

    


if __name__ == '__main__':
    combine_csv('csv1.csv', 'csv2.csv')