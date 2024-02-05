#!/bin/bash

# Directory containing CSV files
directory='../csv_files'
#directory='/c/Users/BBarsch.CSIR/css2024_day03/csv_files'

# List to store the sum of 'y' column values for each file
sum_list=()

# Loop through each CSV file in the directory
for filename in "$directory"/*.csv; do
    if [ -f "$filename" ]; then
        # Use awk to sum the 'y' column values
        echo $filename
        total_sum=$(awk -F',' 'NR > 1 {sum += $2} END {print sum}' "$filename")
        
        # Append the sum to the list
        sum_list+=("$total_sum")
    fi
done

# Print the list of sums
echo "Sum of 'y' column values for each file: ${sum_list[@]}"
