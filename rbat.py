from spmf import Spmf

spmf = Spmf("PrefixSpan", input_filename="BMS1_spmf.txt",
            output_filename="output.txt", arguments=[0.7, 5])
spmf.run()
print(spmf.to_pandas_dataframe(pickle=True))
spmf.to_csv("output.csv")
