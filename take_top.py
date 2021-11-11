N = 5000
def take_top(N, metadata_path, output_path): 
    with open(f'{metadata_path}/metadata.txt') as metadata:
        header = metadata.readline()
        for line in metadata.readlines():
            line = line.split('\t')
            with open(f'{metadata_path}/{line[0]}') as file:
                with open(f'{output_path}/{line[0]}', 'w') as new_file:
                    header = file.readline()
                    new_file.write(header)
                    rows = file.readlines()
                    last_count = int(rows[N-1].split('\t')[0])
                    n = 0
                    last_count_rows = []
                    for row in rows:
                        count = int(row.split('\t')[0])
                        if count > last_count:
                            new_file.write(row)
                            n += 1
                        if count < last_count:
                            break;
                        if count == last_count:
                            last_count_rows.append(row)
                    if len(last_count_rows) != 1:
                        rand_rows = random.sample(last_count_rows, N-n)
                        for rand_row in rand_rows:
                            new_file.write(rand_row)
                    else:
                        new_file.write(last_count_rows[0])
