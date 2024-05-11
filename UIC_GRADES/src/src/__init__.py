import csv
import plotly.graph_objects as go

# Read the data from the CSV file
filename = '/Users/seyfal/Desktop/Datasets/UIC_GRADES/data/fall2023/fall2023_all.csv'
data = []

with open(filename, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
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

# Create the bubble chart
fig = go.Figure(data=[go.Scatter(
    x=perc_as,
    y=avg_gpas,
    text=courses,
    mode='markers',
    marker=dict(
        size=total_students,
        sizemode='area',
        sizeref=2.*max(total_students)/(40.**2),
        sizemin=4,
        color=perc_as,
        colorscale='Viridis',
        showscale=True
    ),
    hovertemplate='%{text}<br>Average GPA: %{y:.2f}<br>Percentage of As: %{x:.2f}%<br>Total Students: %{marker.size}'
)])

fig.update_layout(
    title='Course Performance',
    xaxis_title='Percentage of As',
    yaxis_title='Average GPA'
)

fig.show()