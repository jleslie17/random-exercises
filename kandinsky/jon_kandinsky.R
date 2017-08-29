library(kandinsky)
kandinsky()
df <- read.csv("/Users/jon/Desktop/DfE/DfE_Conditions_for_Success/data/processed/feature_matrix.csv",
               header = TRUE)
kandinsky(df)
