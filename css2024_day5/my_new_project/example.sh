#!bin/bash

directory = "C:/Users/tjmah/Documents/CodingSummerSchool_2024/Day5/css2024_day5/my_new_project"

if [-d "$directory"]; then
	echo "Processing file in: $directory"
	
	for file in "$directory", do
		if [-f "$file"];then
			echo "Processing file: $file"

			# Add your processing logic here
			# Print contents of file

			cat "$file"

			echo "Processing complete for: $file"
			echo "---------------"
		fi
	done

	echo "All files processed successfully."

fi
