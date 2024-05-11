import csv
from django.shortcuts import render
from django.http import JsonResponse

def read_courses_from_file(filename):
    courses = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            courses.append(row[0].strip())
    return courses

def course_list(request):
    return render(request, 'course_list.html')

def filter_courses(request):
    gen_ed_req = request.GET.get('gen_ed_req')
    
    # Read the courses from the respective CSV files
    analyzing_natural_world = read_courses_from_file('/Users/seyfal/Desktop/Datasets/UIC_GRADES/data/gened/Analyzing the Natural World.csv')
    exploring_world_cultures = read_courses_from_file('/Users/seyfal/Desktop/Datasets/UIC_GRADES/data/gened/Exploring World Cultures.csv')
    understanding_creative_arts = read_courses_from_file('/Users/seyfal/Desktop/Datasets/UIC_GRADES/data/gened/Understanding the Creative Arts.csv')
    understanding_individual_society = read_courses_from_file('/Users/seyfal/Desktop/Datasets/UIC_GRADES/data/gened/Understanding the Individual and Society.csv')
    understanding_past = read_courses_from_file('/Users/seyfal/Desktop/Datasets/UIC_GRADES/data/gened/Understanding the Past.csv')
    understanding_us_society = read_courses_from_file('/Users/seyfal/Desktop/Datasets/UIC_GRADES/data/gened/Understanding U.S. Society.csv')

    # Read the data from the main course data CSV file
    filename = '/Users/seyfal/Desktop/Datasets/UIC_GRADES/data/fall2023/fall2023_all.csv'
    data = []

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            course_code = f"{row[0]} {row[1]}"
            if gen_ed_req == 'All' or (
                (gen_ed_req == 'Analyzing the Natural World' and course_code in analyzing_natural_world) or
                (gen_ed_req == 'Exploring World Cultures' and course_code in exploring_world_cultures) or
                (gen_ed_req == 'Understanding the Creative Arts' and course_code in understanding_creative_arts) or
                (gen_ed_req == 'Understanding the Individual and Society' and course_code in understanding_individual_society) or
                (gen_ed_req == 'Understanding the Past' and course_code in understanding_past) or
                (gen_ed_req == 'Understanding U.S. Society' and course_code in understanding_us_society)
            ):
                data.append(row)

    # Calculate the average GPA and percentage of As for each course
    courses = []
    avg_gpas = []
    perc_as = []
    total_students = []

    for row in data:
        course = f"{row[0]} {row[1]}: {row[2]}"
        grades = list(map(int, row[5:21]))
        total = sum(grades)
        
        if total != 0:
            avg_gpa = (grades[0]*4 + grades[1]*3 + grades[2]*2 + grades[3]*1) / total
            perc_a = grades[0] / total * 100
        else:
            avg_gpa = 0
            perc_a = 0
        
        courses.append(course)
        avg_gpas.append(avg_gpa)
        perc_as.append(perc_a)
        total_students.append(total)

    return JsonResponse({'courses': courses, 'avg_gpas': avg_gpas, 'perc_as': perc_as, 'total_students': total_students})