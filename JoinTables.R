if (!requireNamespace("dplyr")) {
  install.packages("dplyr")
}
library(dplyr)

# Change this data to match what you have
table1 <- read.csv("feature-table.csv", check.names = FALSE)
id1 <- "#OTU ID"
table2 <- read.csv("taxonomy.csv", check.names = FALSE)
id2 <- "Feature ID"
output.name <- "feature_table_taxonomy.csv"

table1 <- table1 %>% rename(ASV = !!id1)
table2 <- table2 %>% rename(ASV = !!id2)

joined.table <- inner_join(table1, table2, by = "ASV")

write.csv(joined.table, output.name, row.names = FALSE)

print("Tables merged!")
