from Bio import SeqIO

def filter_short_sequences(input_file, output_file, max_length=300):
    """
    过滤FASTA文件，保留长度小于max_length的序列
    :param input_file: 输入FASTA文件路径
    :param output_file: 输出文件路径
    :param max_length: 最大允许长度（默认300）
    """
    # 统计计数器
    total = 0
    passed = 0
    
    with open(output_file, "w") as out_handle:
        for record in SeqIO.parse(input_file, "fasta"):
            total += 1
            seq_length = len(record.seq)
            
            if seq_length < max_length:
                passed += 1
                # 保留原始header和序列格式
                SeqIO.write(record, out_handle, "fasta")
    
    # 打印统计信息
    print(f"总序列数: {total}")
    print(f"保留序列数: {passed} (长度 < {max_length} AA)")
    print(f"过滤率: {passed/total:.1%}")

if __name__ == "__main__":
    # 直接定义路径（无需命令行参数）
    input_path = "/home/cdj/Project_Long/deduplicated.fasta"
    output_path = "/home/cdj/Project_Long/label_0.fasta"  # 输出文件名可自定义
    
    # 调用去重函数
    filter_short_sequences(input_path, output_path)