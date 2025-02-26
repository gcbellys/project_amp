from Bio import SeqIO
import pandas as pd

def fasta_to_csv(input_fasta, output_csv):
    # 读取FASTA文件
    records = []
    for seq_record in SeqIO.parse(input_fasta, "fasta"):
        records.append({
            "ID": seq_record.id,
            "Description": seq_record.description,
            "Sequence": str(seq_record.seq).replace("\n", "")  # 合并多行序列为单行
        })
    
    # 转换为DataFrame并保存CSV
    df = pd.DataFrame(records)
    df.to_csv(output_csv, index=False)

# 使用示例
fasta_to_csv("/home/cdj/Project_Long/label_0.fasta", "/home/cdj/Project_Long/label_0.csv")