import os

def split_file(input_file, output_dir, chunk_size=10*1024*1024):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r') as f:
        part_num = 1
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            output_file = os.path.join(output_dir, f'{os.path.basename(input_file)}_{part_num}.txt')
            with open(output_file, 'w') as part:
                part.write(chunk)
            part_num += 1
            log(f'Created file: {output_file}')

def log(message):
    with open('logfile.txt', 'a') as log_file:
        log_file.write(message + '\n')

if __name__ == "__main__":
    input_file = r"C:\Users\bergen\filezilla-server.log"
    output_dir = r"C:\Users\bergen\Work\FileZilla Log"

    split_file(input_file, output_dir)
    log(f'Split {input_file} into smaller files in {output_dir}')
