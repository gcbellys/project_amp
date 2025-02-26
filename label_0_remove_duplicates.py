import sys
from collections import OrderedDict

def remove_duplicates(input_file, output_file):
    """
    去除FASTA文件中的重复序列
    :param input_file: 输入FASTA文件路径
    :param output_file: 输出FASTA文件路径
    """
    # 使用OrderedDict保持顺序，键为序列，值为header
    sequences = OrderedDict()
    
    with open(input_file, 'r') as f:
        current_header = None
        current_seq = []
        
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                # 遇到新header时处理前一个序列
                if current_header is not None:
                    seq = ''.join(current_seq).upper()  # 统一转大写（可选）
                    if seq not in sequences:
                        sequences[seq] = current_header
                    current_seq = []
                
                current_header = line
            else:
                current_seq.append(line)
        
        # 处理最后一个序列
        if current_header is not None:
            seq = ''.join(current_seq).upper()
            if seq not in sequences:
                sequences[seq] = current_header

    # 写入去重后的结果
    with open(output_file, 'w') as f:
        for seq, header in sequences.items():
            f.write(f"{header}\n")
            # 每行80字符换行（可选）
            for i in range(0, len(seq), 80):
                f.write(f"{seq[i:i+80]}\n")

    # 统计信息
    print(f"输入序列总数: {len(sequences) + sum(1 for k in sequences if sequences[k] is None)}")
    print(f"唯一序列数量: {len(sequences)}")

if __name__ == "__main__":
    # 直接定义路径（无需命令行参数）
    input_path = "/home/cdj/Project_Long/deduplicated.fasta"
    output_path = "/home/cdj/Project_Long/label_0.fasta"  # 输出文件名可自定义
    
    # 调用去重函数
    remove_duplicates(input_path, output_path)