import csv

# Specify the path to the input CSV file
input_file = "/Users/seyfal/Desktop/Datasets/UIC_GRADES/data/gened/geneds_all.csv"

# Create a dictionary to store the courses for each general education requirement category
gened_categories = {
    "Analyzing the Natural World": [],
    "Exploring World Cultures": [],
    "Understanding the Creative Arts": [],
    "Understanding the Individual and Society": [],
    "Understanding the Past": [],
    "Understanding U.S. Society": []
}

# Read the cleaned CSV file and process each row
with open(input_file, "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        course = row[0].strip()
        requirements = [req.strip() for req in row[1:]]

        # Add the course to the corresponding general education requirement category
        for requirement in requirements:
            if requirement in gened_categories:
                gened_categories[requirement].append(course)

# Save the courses for each general education requirement category to separate CSV files
for category, courses in gened_categories.items():
    output_file = f"/Users/seyfal/Desktop/Datasets/UIC_GRADES/data/{category}.csv"
    with open(output_file, "w") as file:
        csv_writer = csv.writer(file)
        for course in courses:
            csv_writer.writerow([course])

    print(f"Courses for {category} saved to {output_file}")