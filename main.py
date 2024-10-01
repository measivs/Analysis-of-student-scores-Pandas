import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('student_scores_random_names.csv')

def list_students_failed(df):
    """
    გამოიტანეთ იმ სტუდენტთა სია, რომლებმაც არ ჩააბარეს რომელიმე საგანი
    (ქულა ნაკლებია 50-ზე)
    """
    df.fillna(0, inplace=True)
    failed = df[(df['Math'] < 50) | (df['Physics'] < 50) |
                (df['Chemistry'] < 50) | (df['Biology'] < 50) |
                (df['English'] < 50)]
    
    students = failed['Student'].unique()
    return students

failed_students = list_students_failed(df)
print(f'Students who failed any subject:')
for student in failed_students:
    print(student)


def avg_point_in_every_semester(df):
    """
    თითოეული საგნისთვის გამოთვალეთ 
    საშუალო ქულა თითო სემესტრში
    """
    semesters = df.groupby('Semester')[['Math', 'Physics', 'Chemistry', 'Biology', 'English']]
    averages = semesters.mean()
    return averages

average_point = avg_point_in_every_semester(df)
print("Average score per semester for each subject:")
print(average_point)


def students_with_max_points(df):
    """
    იპოვეთ ის სტუდენტი(ები), რომელთაც აქვთ ყველაზე მაღალი 
    საშუალო ქულა ყველა სემესტრსა და საგანში
    """
    df['Average'] = df[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean(axis=1)
    max_average = df['Average'].max()
    students_max = df[df['Average'] == max_average]
    return students_max[['Student', 'Average']]

top_students = students_with_max_points(df)
print(f'Student(s) with the highest average marks:')
print(top_students)


def most_difficult_subject(df):
    """
    იპოვეთ საგანი, რომელშიც სტუდენტებს ყველაზე მეტად გაუჭირდათ 
    (ყველაზე დაბალი საშუალო ქულა ყველა სემესტრში)
    """
    averages = df[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean()
    lowest_subject = averages.idxmin()
    lowest_average = averages.min()
    
    return lowest_subject, lowest_average

ls, la = most_difficult_subject(df)
print(f'Subject which was the most difficult for every student is {ls} with an average score of {la:.2f}.')


def average_in_excel(df, filename):
    """
    შექმენით ახალი დატაფრეიმი სადაც დააგენერირებთ საგნების საშუალო 
    ქულებს სემესტრის მიხედვით და შემდეგ შეინახავთ ექსელის ფაილში
    (ინდექსები შეუსაბამეთ სემესტრებს)
    """
    average_scores = df.groupby('Semester')[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean()
    average_scores.reset_index(inplace=True)
    average_scores.index = average_scores.index + 1
    average_scores.to_excel(filename, index=True)

average_in_excel(df, 'average_scores_by_semester.xlsx')


def bar_chart(df):
    """
    შექმენით სვეტების დიაგრამა, რომელიც აჩვენებს თითო საგნის 
    საშუალო ქულას ყველა სემესტრში
    """
    average_scores = df[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean()

    plt.figure(figsize=(10, 6))
    average_scores.plot(kind='bar', color=['pink', 'yellow', 'blue', 'purple', 'green'])
    plt.title('Average Score per Subject Across All Semesters')
    plt.xlabel('Subjects')
    plt.ylabel('Average Score')
    plt.xticks(rotation=45)
    plt.ylim(0, 100)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

b_chart = bar_chart(df)


def line_graph(df):
    """
    შექმენით ხაზოვანი გრაფიკი, რომელიც აჩვენებს საშუალო 
    საერთო ქულას სემესტრების მიხედვით
    """
    average_scores = df.groupby('Semester')[['Math', 'Physics', 'Chemistry', 'Biology', 'English']].mean()
    average_scores['Overall Average'] = average_scores.mean(axis=1)

    plt.figure(figsize=(10, 6))
    plt.plot(average_scores.index, average_scores['Overall Average'], marker='o', color='red', label='Overall Average')
    plt.title('Average Overall Score by Semester')
    plt.xlabel('Semester')
    plt.ylabel('Average Score')
    plt.ylim(0, 100)
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()

l_graph = line_graph(df)
print(l_graph)
